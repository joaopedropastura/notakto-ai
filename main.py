import random



values = [[0,1,2] , [3,4,5] , [6,7,8] , [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
totalgames = []



def createTables(qtt):
    table = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0], False]
    for i in range(qtt):
        totalgames.append(table)
        
    
def gameTurn(position,game):
    tableGame = totalgames[game][1]
    resultGame = totalgames[game][0]
    win = totalgames[game][2]
    
    if(win):
        return win
    
    
    if(tableGame[position] == 1):
        print("posição ja selecionada")
    else:
        tableGame[position] += 1
        
    
    for i in range(len(values)-1):
        if(position in values[i]):
            resultGame[i] += 1
    
    
    for i in range(len(resultGame)):
        if(resultGame[i] >= 3):
            return True
        
    return False
                


createTables(3)
game = 2

while True:
    while True:
        computer = random.randint(0, 8)
        print(computer)
        if(totalgames[game][1][computer] == 0):
            break
        
    totalgames[2][2] = gameTurn(computer,game)
    print(totalgames[game][1][0], totalgames[game][1][1], totalgames[game][1][2])
    print(totalgames[game][1][3], totalgames[game][1][4], totalgames[game][1][5])
    print(totalgames[game][1][6], totalgames[game][1][7], totalgames[game][1][8])
    
    posicao = int(input("escolha sua posicao: "))
    totalgames[2][2] = gameTurn(posicao,game)
    
