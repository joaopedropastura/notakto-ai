import random



plays = [[0,1,2] , [3,4,5] , [6,7,8] , [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
totalgames = []
aval = 0

def createTables(qtt):
    table = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0], False]
    for i in range(qtt):
        totalgames.append(table)
        
        


def minimax(ismax, table):
    result = Eval(ismax);
    
    if(result != 0):
        return result
    
    if(ismax):
        biggestScore = -1000
        for i in range(len(totalgames)):
            if not totalgames[i][2]:
                
                for position in totalgames[i][1]:
                    if position == 0:
                        position = 1
                        totalgames[i][2] = verifyTableEnd(i)
                        score = minimax(True, totalgames[i][1], False)
                        position = 0
                        biggestScore = max(score, biggestScore)        
        return biggestScore
    
    else:
        biggestScore = 1000
        for i in range(len(totalgames)):
            if totalgames[i][2]:
                
                for position in totalgames[i][1]:
                    if position == 0:
                        position = 1
                        totalgames[i][2] = verifyTableEnd(i)
                        score = minimax(True, totalgames[i][1], True)
                        position = 0
                        biggestScore = min(score, biggestScore)
                        
        return biggestScore
        
                        
        
    
    
    
def Eval(myturn):
    for table in totalgames:
        for isend in table[2]:
            if(myturn and isend):
                return -1
            elif(not myturn and isend):
                return 1
            else:
                return 0
        
    
    
def verifyTableEnd(game):
    resultGame = totalgames[game][0]
    for i in range(len(resultGame)):
        if(resultGame[i] >= 3):
            return True
    return False
    
    
def gameTurn(position,game):
    tableGame = totalgames[game][1]
    resultGame = totalgames[game][0]
    
    if(tableGame[position] == 1):
        print("posição ja selecionada")
    else:
        tableGame[position] += 1
        
        
    for i in range(len(plays)-1):
        if(position in plays[i]):
            resultGame[i] += 1

    





createTables(3)
game = 2
while True:
    
    
    gameTurn(computer, game)
    totalgames[2][2] = verifyTableEnd(game)
    

    print(totalgames[game][1][0], totalgames[game][1][1], totalgames[game][1][2])
    print(totalgames[game][1][3], totalgames[game][1][4], totalgames[game][1][5])
    print(totalgames[game][1][6], totalgames[game][1][7], totalgames[game][1][8])
    
    posicao = int(input("escolha sua posicao: "))
    gameTurn(posicao, game)
    totalgames[2][2] = verifyTableEnd(game)
    
    print(totalgames[game][1][0], totalgames[game][1][1], totalgames[game][1][2])
    print(totalgames[game][1][3], totalgames[game][1][4], totalgames[game][1][5])
    print(totalgames[game][1][6], totalgames[game][1][7], totalgames[game][1][8])
    
