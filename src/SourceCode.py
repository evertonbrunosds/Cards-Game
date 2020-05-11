'''
/*******************************************************************************
Autor: Everton Bruno Silva dos Santos
Componente Curricular: MI - ALGORITMOS
Concluido em:09/09/2019
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código e estou ciente que estes trechos não serão considerados para fins de avaliação.
/*******************************************************************************
'''
import random
import os

def ClearScreen():#LIMPA A TELA
    if(os.name == 'posix'):#SE O SISTEMA FOR O LINUX USA CLEAR
        os.system('clear')
    elif(os.name == 'nt'):#SE O SISTEMA FOR O WINDOWS USA CLS
        os.system('cls')

def GameDataDir():#RETORNA O DIRETÓRIO DE ARQUIVOS ONDE ESTÃO OS DADOS DO JOGO
    if (os.name == 'posix'):#SE O SISTEMA FOR O LINUX, RETORNA ESTRUTURA DE DIRETÓRIOS ADEQUADA
        return('GameData/')
    elif (os.name == 'nt'):#SE O SISTEMA FOR O WINDOWS, RETORNA ESTRUTURA DE DIRETÓRIOS ADEQUADA
        return('GameData\\')

def LoadFromFile(fileName):#RETORNA ARQUIVO NA MEMÓRIA TEMPORÁRIA
    fileToMatrix = []
    if (os.path.isfile(GameDataDir()+fileName) == True):#VERIFICA SE O ARQUIVO SOLICITADO EXISTE
        with open((GameDataDir()+fileName),'r',encoding='UTF-8') as fileStream:#EXISTINDO, INSERE NA MEMÓRIA
            for fileElement in fileStream:#PERCORRE CADA ELEMENTO DO ARQUIVO PARA TRANSFORMA-LO EM MATRIZ
                fileToMatrix.append(fileElement[:-1].split(';'))
            return(fileToMatrix)#RETORNA ARQUIVO COMO MATRIZ
    else:#NO CASO DO ARQUIVO NÃO EXISTIR:
        return(None)#RETORNA "NONE" PARA INFORMAR QUE O MESMO NÃO EXISTE

def RandomizeData(dataBase):#RANDOMIZA OS ÍNDICES DE UMA LISTA
    randomizedList = []
    while (len(dataBase) != 0):
        randomIndex = random.randint(0,(len(dataBase)-1))
        randomizedList.append(dataBase.pop(randomIndex))
    return(randomizedList)

def SortData(dataBase,inIndex):             #FUNÇÃO DE ORDENAÇÃO E RANDOMIZAÇÃO DE DADOS
    sorting = True
    while (sorting == True):
        sorting = False
        if (0<= inIndex <=3):               #ORDENAÇÃO ALFABÉTICA, DE VALOR, FORÇA E ENERGIA
            for i in range(len(dataBase)):
                if ((i+1) < len(dataBase)):
                    if (0 == inIndex):      #PARA ORDENAÇÃO ALFABÉTICA
                        if (dataBase[i][inIndex] > dataBase[i+1][inIndex]):
                            dataBase[i],dataBase[i+1] = dataBase[i+1],dataBase[i]
                            sorting = True
                    elif (1<= inIndex <=3): #PARA ORDENAÇÃO NUMÉRICA
                        if (float(dataBase[i][inIndex]) > float(dataBase[i+1][inIndex])):
                            dataBase[i],dataBase[i+1] = dataBase[i+1],dataBase[i]
                            sorting = True
        elif(inIndex==4):                   #RANDOMIZAÇÃO DE ITENS
            dataBase = RandomizeData(dataBase)
    return(dataBase)                        #RETORNO DE DADOS PROCESSADOS

def SearchInBase(dataBase,searchData,inIndex):#FUNÇÃO DE BUSCA DE DADOS
    for i in range(len(dataBase)):       
        if (dataBase[i][inIndex] == searchData):
            return(i)#SE O DADO FOR ECONTRADO RETORNA A POSIÇÃO
    return(None)#SE O DADO NÃO FOR ENCONTRADO RETORNA "NONE"

def OnCenterOneData(data,length):#RETORNA UM DADO CENTRALIZADO
    lenChar=int((len(data))/2)
    if (lenChar<=int(length/2)):
        DataFormated=('|'+' '*(int(length/2)-1-lenChar)+data)
        if (len(DataFormated) < length):
        	DataFormated+=(' '*(length-1-len(DataFormated))+'|')
        	return(DataFormated)
    return(data)

def OnCenterTwoData(data,length,centerChar):#RETORNA UM DOIS DADOS CENTRALIZADOS EM 70 CARACTERES, EX: |---DADO1 | DADO2---|
    for i in range(len(data)):
        if (data[i] == centerChar):
            break
    if (i<=int(length/2)):
        DataFormated=('|'+' '*(int(length/2)-i-1)+data)
        if (len(DataFormated) < length):
        	DataFormated+=(' '*(length-1-len(DataFormated))+'|')
        	return(DataFormated)
    return(data)

def AutomaticMode(userName):#SELEÇÃO DE MODO DE JOGO
    while True:
        ClearScreen()
        print('|'+'-'*68+'|')
        print(OnCenterOneData(userName+', ESCOLHA O MODO DE JOGO',70))
        print('|'+'-'*68+'|')
        print(OnCenterOneData('    1) MANUAL                                               ',70))
        print(OnCenterOneData('    2) AUTOMÁTICO                                           ',70))
        automaticMode=input('|'+'-'*68+'|\n\nINFORME O MODO DE JOGO: ')
        if (automaticMode == '1'):
            return (False)
        elif (automaticMode == '2'):
            return (True)

def NicknameFilter(msg):#FILTRO DE NOME DE JOGADOR
    while True:
        ClearScreen()
        invalidChar = False
        nickname = input(msg).upper()
        if ((nickname!='') and (len(nickname)<=10)):
            for element in nickname:#BUSCA POR CARACTERES INVÁLIDOS NA STRING
                if ((element==';') or (element==':') or (element=='|') or (element=='-')):
                    invalidChar = True
                    break
            if (invalidChar == False):
                return(nickname)
            else:
                print('VOCÊ NÃO PODE USAR CARACTERES ESPECIAIS COMO: ( ; : | - )')
        else:
            print('VOCÊ NÃO PODE CRIAR UM NICKNAME NULO OU COM MAIS DE 10 LETRAS...')
        pause = input('PRESSIONE [ENTER] PARA CONTINUAR...')

def SaveFromFile(fileName,allPlayes):#SALVA DADOS DA MEMÓRIA RAM NO HD
    with open(GameDataDir()+fileName,'w',encoding='UTF-8') as fileStream:
        for element in allPlayes:
            fileStream.write(element[0]+';'+str(element[1])+';'+str(element[2])+';'+str(element[3])+'\n')

def LogIn():#FUNÇÃO DE LOGUIN
    class GameData:
            def __init__(self,deckAll,deckOne,deckTwo,allPlayes,position):
                self.deckAll = deckAll                          #TODAS AS CARTAS
                self.deckOne = deckOne                          #BARALHO 1
                self.deckTwo = deckTwo                          #BARALHO 2
                self.allPlayes = allPlayes                      #DADOS DE TODOS OS JOGADORES
                self.position = position                        #AS POSIÇÕES DOS JOGADORES NA LISTA
            def Player(self,index):                             #PARA PEGAR DADOS DO JOGADOR 1 DA PARTIDA
                return(self.allPlayes[self.position[index]])    #RETORNA OS DADOS DO JOGADOR 1
            def AddCard(self,num):                              #ADICIONA CARTAS AS MÃOS DOS USUÁRIOS
                for i in range(num):                            #NÚMERO DE CARTAS A ADICIONAR
                    self.deckOne.append(self.deckAll.pop())     #ADICIONA CARTAS AO USUÁRIO 1
                    self.deckTwo.append(self.deckAll.pop())     #ADICIONA CARTAS AO USUÁRIO 2
            def UpdateRate(self,index):                         #ATUALIZA A TAXA DE SUCESSO DO JOGADOR
                self.allPlayes[self.position[index]][3] = (int(self.Player(index)[2])/int(self.Player(index)[1])*100)#SE JÁ JOGOU, CALCULA O PERCENTUAL DE SUCESSO
    deckAll = RandomizeData(LoadFromFile('Cartas.txt'))         #CARREGA AS CARTAS E AS TORNAM ALEATÓRIAS
    selectedPlayers = [[]]                                      #POSIÇÃO DOS JOGADORES SELECIONADOS PARA A PARTIDA
    while len(selectedPlayers) != 3:                            #AGUARDA A CHEGADA DE DPOS JOGADORES
        allPlayes = LoadFromFile('PlayerData.txt')              #CARREGA OS DADOS DOS JOGADORES
        nickname = NicknameFilter('DIGITE O NICKNAME DO %iº JOGADOR: '%len(selectedPlayers))
        if (allPlayes == None):                                 #SE O ARQUIVO DE JOGADORES NÃO FOI CRIADO
            allPlayes = []                                      #CRIA UMA LISTA
            selectedPlayers.append(0)                           #GUARDA A POSIÇÃO DO JOGADOR
            allPlayes.append([nickname,0,0,0])                  #INSERE O NOVO JOGADOR NA LISTA
            SaveFromFile('PlayerData.txt',allPlayes)            #CRIA O ARQUIVO COM OS DADOS DO PRIMEIRO JOGADOR
        else:                                                   #SE O ARQUIVO DE JOGADORES FOI ENCONTRADO
            playerPosition = SearchInBase(allPlayes,nickname,0) #BUSCA A POSIÇÃO DO JOGADOR INFORMADO
            if(playerPosition == None):                         #SE O USUÁRIO NÃO EXISTIR
                selectedPlayers.append(len(allPlayes))          #ARMAZENA A POSIÇÃO DO NOVO JOGADOR
                allPlayes.append([nickname,0,0,0])               #INSERE O NOVO JOGADOR NA LISTA
                SaveFromFile('PlayerData.txt',allPlayes)        #CRIA O ARQUIVO COM OS DADOS DO JOGADOR
            elif (playerPosition!=selectedPlayers[-1]):         #VERIFICA SE A POSIÇÃO JÁ NÃO ESTÁ SENDO USADA
                selectedPlayers.append(playerPosition)          #SE NÃO GUARDA A POSIÇÃO
            else:
                pause=input('VOCÊ NÃO PODE JOGAR CONTRA SÍ MESMO...\nPRESSIONE [ENTER] PARA CONTINUAR...')
    return(GameData(deckAll,[],[],LoadFromFile('PlayerData.txt'),selectedPlayers))

def ShowScore(gameData):
    label = {0:'NICKNAME:   ',1:'PARTIDAS:   ',2:'VITÓRIAS:   ',3:'SUCESSO:   %.2f'}
    ClearScreen()
    print('|'+'-'*28+'|')
    for x in range(1,3):
        for i in range(3):
            print(OnCenterTwoData(label[i]+gameData.Player(x)[i],30,':'))
        print(OnCenterTwoData(label[i+1]%float(gameData.Player(x)[i+1])+'%',30,':'))
        print('|'+'-'*28+'|')
    pause = input('\n\nPRESSIONE [ENTER] PARA CONTINUAR...')
        
def ShowDecks(gameData,tupleDecks,roundWin):
    label = {0:'PERSONAGEM:   ',1:'VALOR:   ',2:'FORÇA:   ',3:'ENERGIA:   ',4:'JOKEMPÔ:   '}
    for X in range(2):#USUÁRIO
        ClearScreen()
        print('|'+'-'*68+'|')
        print(OnCenterTwoData('JOGADOR: '+gameData.Player(X+1)[0]+'   |   VITÓRIAS DE DISPUTA: %i'%roundWin[X],70,'|'))
        for Y in range(0,len(tupleDecks[X]),2):#CARTA
            print('|'+'-'*68+'|')
            for Z in range(len(tupleDecks[X][Y])):#ELEMENTO
                if ((Y+1)<len(tupleDecks[X])):
                    print(OnCenterTwoData((label[Z]+tupleDecks[X][Y][Z])+'   |   '+(label[Z]+tupleDecks[X][Y+1][Z]),70,'|'))
                else:
                    print(OnCenterTwoData((label[Z]+tupleDecks[X][Y][Z]+'   |'),70,'|'))
        print('|'+'-'*68+'|')
        pause=input('\nPRESSIONE [ENTER] PARA CONTINUAR....')
    ClearScreen()

def RandomizeRange(tupleCards):#SORTEIA AS CARTAS DA DISPUTA PARA AMBOS OS USUÁRIOS
    return((random.randint(0,len(tupleCards[0])-1),random.randint(0,len(tupleCards[1])-1)))

def IntegerVaule(msgQuest,maxValue):#ACEITA APENAS NÚMEROS INTEIROS
    while True:
        try:
            numInt = int(input(msgQuest))
            assert isinstance (numInt,int) and (0 <= numInt <= maxValue)
        except:
            print('DEVE SER UM VALOR ALGÉBRICO INTEIRO ENTRE 1 E %i'%maxValue)
        else:
            return(numInt-1)#SE TUDO OCORRER BEM, RETORNA VALOR INTEIRO

def SelectRange(gameData):#PERMITE QUE AMBOS OS USUÁRIOS SELECIONEM AS CARTAS DA DISPUTA
    numCardOne = IntegerVaule((gameData.Player(1)[0]+', SELECIONE UMA DE SUAS %i CARTAS NUMÉRICAMENTE: '
        %len(gameData.deckOne)),len(gameData.deckOne))
    numCardTwo = IntegerVaule((gameData.Player(2)[0]+', SELECIONE UMA DE SUAS %i CARTAS NUMÉRICAMENTE: '
        %len(gameData.deckTwo)),len(gameData.deckTwo))
    return((numCardOne,numCardTwo))

def DisputeMode(nickname,rounds):
    while True:
        ClearScreen()
        print('|'+'-'*68+'|')
        print (OnCenterOneData(nickname+', SELECIONE O MODO DE DISPUTA',70))
        print('|'+'-'*68+'|')
        print(OnCenterOneData('    1) VALOR                                                ',70))
        print(OnCenterOneData('    2) FORÇA                                                ',70))
        print(OnCenterOneData('    3) ENERGIA                                              ',70))
        print(OnCenterOneData('    4) JOKEMPÔ                                              ',70))
        disputeMode=input('|'+'-'*68+'|\n\n%iª PARTIDA, INFORME O MODO DE DISPUTA: '%rounds)
        if (disputeMode == '1'):#DISPUTA DE VALOR
            return(1)
        elif (disputeMode == '2'):#DISPUTA DE FORÇA
            return(2)
        elif (disputeMode == '3'):#DISPUTA DE ENERGIA
            return(3)
        elif (disputeMode == '4'):#DISPUTA DE JOKEMPÔ
            return(4)

def DisputeRound(gameData,randomizeCard,inIndex,roundWin):
    jokCase = {'PedraPedra':(True,True),'PedraPapel':(False,True),'PedraTesoura':(True,False),'PapelPedra':(True,False),
        'PapelPapel':(True,True),'PapelTesoura':(False,True),'TesouraPedra':(False,True),'TesouraPapel':(True,False),
        'TesouraTesoura':(True,True)}#DEFINE QUEM VENCE NO JOKEMPÔ
    if (1<=inIndex<=3):#DISPUTA DE VALOR, FORÇA E ENERGIA
        if (float(gameData.deckOne[randomizeCard[0]][inIndex]) < float(gameData.deckTwo[randomizeCard[1]][inIndex])): #O JOGADOR 1 PERDE
            gameData.deckOne.append(gameData.deckAll.pop())#O JOGADOR 1 PEGA OUTRA CARTA
            roundWin[1]+=1#O JOGADOR 2 GANHA PONTOS
        elif (float(gameData.deckOne[randomizeCard[0]][inIndex]) > float(gameData.deckTwo[randomizeCard[1]][inIndex])):#O JOGADOR 2 PERDE
            gameData.deckTwo.append(gameData.deckAll.pop())#O JOGADOR 2 PEGA OUTRA CARTA
            roundWin[0]+=1#O JOGADOR 1 GANHA PONTOS
        elif (float(gameData.deckOne[randomizeCard[0]][inIndex]) == float(gameData.deckTwo[randomizeCard[1]][inIndex])):#EMPATE DE DISPUTA
            gameData.AddCard(1)#ADICIONA CARTAS PARA AMBOS OS JOGADORES
    elif(inIndex==4):#DISPUTA DE JOKEMPÔ
        jokResult = jokCase[gameData.deckOne[randomizeCard[0]][inIndex]+gameData.deckTwo[randomizeCard[1]][inIndex]]
        if (jokResult == (True,True)):#PARA O CASO DE EMPATE DE JOKEMPÔ
            gameData.AddCard(1)#ADICIONA CARTAS PARA AMBOS OS JOGADORES            
        elif(jokResult == (True,False)):#O JOGADOR 2 PERDE
            gameData.deckTwo.append(gameData.deckAll.pop())#O JOGADOR 2 PEGA OUTRA CARTA
            roundWin[0]+=1#O JOGADOR 1 GANHA PONTOS
        elif(jokResult == (False,True)):#O JOGADOR 1 PERDE
            gameData.deckOne.append(gameData.deckAll.pop())#O JOGADOR 1 PEGA OUTRA CARTA
            roundWin[1]+=1#O JOGADOR 2 GANHA PONTOS            
    gameData.deckOne.pop(randomizeCard[0])#O JOGADOR 1 DESCARTA A CARTA USADA NA DISPUTA
    gameData.deckTwo.pop(randomizeCard[1])#O JOGADOR 2 DESCARTA A CARTA USADA NA DISPUTA

def SomeElement(gameData,propertyValue,inIndex):#EFETUA A SOMA DE VALOR, FORÇA E ENERGIA
    for element in gameData.deckOne:#PERCORRE CADA ELEMENTO DO BARALHO DO JOGADOR 1
        propertyValue[0]+=float(element[inIndex])#SOMA OS VALORES DO JOGADOR 1
    for element in gameData.deckTwo:#PERCORRE CADA ELEMENTO DO BARALHO DO JOGADOR 2
        propertyValue[1]+=float(element[inIndex])#XOMA OS VALORES DO JOGADOR 2

def ShowWinner(msg):
    print('|'+'-'*68+'|')
    print(msg)
    print('|'+'-'*68+'|')
    pause=input('\nPRESSIONE [ENTER] PARA SAIR DO JOGO....')

def UpdateScore(gameData,playerOneWin):#ATUALIZA O SCORE DOS JOGADORES
    ClearScreen()
    if (playerOneWin == True):#SE O JOGADOR 1 VENCEU
        gameData.allPlayes[gameData.position[1]][1] = (int(gameData.Player(1)[1])+1)#ACRESCENTA PARTIDA JOGADA AO JOGADOR 1
        gameData.allPlayes[gameData.position[2]][1] = (int(gameData.Player(2)[1])+1)#ACRESCENTA PARTIDA JOGADA AO JOGADOR 2
        gameData.allPlayes[gameData.position[1]][2] = (int(gameData.Player(1)[2])+1)#ACRESCENTA VITÓRIA AO JOGADOR 1
        gameData.UpdateRate(1)#ATUALIZA O PERCENTUAL DE VITÓRIAS DO JOGADOR 1
        ShowWinner(OnCenterOneData(('JOGADOR VENCEDOR: '+gameData.Player(1)[0]),70))
    elif(playerOneWin == False):#SE O JOGADOR 2 VENCEU
        gameData.allPlayes[gameData.position[1]][1] = (int(gameData.Player(1)[1])+1)#ACRESCENTA PARTIDA JOGADA AO JOGADOR 1
        gameData.allPlayes[gameData.position[2]][1] = (int(gameData.Player(2)[1])+1)#ACRESCENTA PARTIDA JOGADA AO JOGADOR 2
        gameData.allPlayes[gameData.position[2]][2] = (int(gameData.Player(2)[2])+1)#ACRESCENTA VITÓRIA AO JOGADOR 2
        gameData.UpdateRate(2)#ATUALIZA O PERCENTUAL DE VITÓRIAS DO JOGADOR 2
        ShowWinner(OnCenterOneData(('JOGADOR VENCEDOR: '+gameData.Player(2)[0]),70))
    SaveFromFile('PlayerData.txt',gameData.allPlayes)#SALVA AS ALTERAÇÕES NO REGISTRO DOS JOGADORES

def MainMenu():#MENU PRINCIPAL
    gameData = LogIn()      #APÓS OBITER AS INFORMAÇÕES NECESSÁRIAS CRIA OBJETO
    ShowScore(gameData)     #EXIBE OS DADOS OS JOGADORES DA PARTIDA
    gameData.AddCard(5)     #DISTRIBUE 5 CARTAS PARA CADA
    automaticMode = AutomaticMode(gameData.Player(1)[0])#SELECIONA O MODO DE JOGO
    roundWin = [0,0]        #VITÓRIAS DA DISPUTA
    ShowDecks(gameData,((gameData.deckOne,gameData.deckTwo)),roundWin)
    rounds = 0#CONTADOR USADO PARA EXIBIR A QUANTIDADE DE PARTIDAS
    endGame = False#USADO PARA INTERROMPER O LAÇO PRINCIPAL
    for i in range(5):#ESSE FOR RODA 5 VEZES E PARA CADA UMA DELAS AMBOS OS JOGADORES JOGAM, LOGO SÃO 10 PARTIDAS
        if (endGame == True):#VERIFICA DE É O MOMENTO DE PARAR O JOGO
            break#INTERROMPE O LAÇO PRINCIPAL
        for x in range(1,3):#ESQUEMA DE DUAS DISPUTAS POR RODADA
            rounds+=1
            if (len(gameData.deckOne)==0):#VERIFICA SE O JOGADOR 1 FICOU SEM CARTAS
                UpdateScore(gameData,True)#ATUALIZA O SCORE DO JOGADOR 1
                endGame = True
                break#INTERROMPE O LAÇO INTERNO
            elif (len(gameData.deckTwo)==0):#VERIFICA SE O JOGADOR 2 FICOU SEM CARTAS
                UpdateScore(gameData,False)#ATUALIZA O SCORE DO JOGADOR 2
                endGame = True
                break#INTERROMPE O LAÇO INTERNO
            disputeMode = DisputeMode(gameData.Player(x)[0],rounds)#SELECIONA O MODO DE DISPUTA
            if(automaticMode == True):#PARA O MODO AUTOMÁTICO
                gameData.deckOne,gameData.deckTwo = SortData(gameData.deckOne,disputeMode),SortData(gameData.deckTwo,disputeMode)#ORDENA AS CARTAS DE ACORDO O MODO
                randomizeRange = RandomizeRange((gameData.deckOne,gameData.deckTwo))#SORTEIA CARTAS PARA AMBOS OS JOGADORES
                DisputeRound(gameData,randomizeRange,disputeMode,roundWin)
                gameData.deckOne,gameData.deckTwo = SortData(gameData.deckOne,disputeMode),SortData(gameData.deckTwo,disputeMode)#ORDENA AS CARTAS DE ACORDO O MODO
            elif(automaticMode == False):#PARA O MODO MANUAL
                gameData.deckOne,gameData.deckTwo = SortData(gameData.deckOne,0),SortData(gameData.deckTwo,0)#ORDENA AS CARTAS EM ORDEM ALFABÉTICA
                selectRange = SelectRange(gameData)#OS JOGADORES ESCOLHEM COM QUAIS CARTAS IRÃO JOGAR
                DisputeRound(gameData,selectRange,disputeMode,roundWin)
                gameData.deckOne,gameData.deckTwo = SortData(gameData.deckOne,0),SortData(gameData.deckTwo,0)#ORDENA AS CARTAS EM ORDEM ALFABÉTICA
            ShowDecks(gameData,((gameData.deckOne,gameData.deckTwo)),roundWin)
    if (endGame == False):#SE O JOGO ACABOU POR RODADAS CORRIDAS
        propertyValue = [0,0]#RECEBE AS SOMAS DE VALOR, FORÇA E ENERGIA    
        for i in range(1,4):#PARA SOMAR VALOR, FORÇA E ENERGIA
            SomeElement(gameData,propertyValue,i)#PARA SOMAR VALORES
            if (propertyValue[0] < propertyValue[1]):#SE O JOGADOR 1 VENCEU
                UpdateScore(gameData,True)#ATUALIZA O SCORE DO JOGADOR 1
                break
            elif(propertyValue[0] > propertyValue[1]):#SE O JOGADOR 2 VENCEU
                UpdateScore(gameData,False)#ATUALIZA O SCORE DO JOGADOR 2
                break
        if (propertyValue[0] == propertyValue[1]):
            ShowWinner(OnCenterOneData(('ROLOU UM EMPATE DESSA VEZ, MAS VOCÊS JOGARAM BRAVAMENTE'),70))

MainMenu()