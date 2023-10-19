import sys
import os
import random

random.seed(8)

player = sys.argv[1]
tables = sys.argv[2]

files = ['m1.txt', 'm2.txt']


def UpdateFileValue(file_name):
    f = open(file_name, 'w')
    f.write('0 ' + str(round(random.random() * 1)))
    f.close()

def GetFileValue():
    print('')

def GetFileName():
    file_name = ''
    for f_name in os.listdir('front'):
        if f_name.endswith('.txt'):
            file_name = f'./front/{f_name}'
    
    if(file_name == '' and player == 'm1'):
        f = open("./front/m1.txt", "w")
        f.write('0 ' + str(round(random.random() * 10)))
        f.close()
        file_name = "./front/m1.txt"
    return file_name

def FileManipulation():
    file_name = GetFileName()
    if ('m1 last' in file_name):
        if (player == 'm1'):
            print(file_name)
            os.remove(file_name)
            file_name = "./front/m1.txt"
            UpdateFileValue(file_name)

    elif ('m2 last' in file_name):
        if(player == 'm2'):
            os.remove(file_name)
            file_name = "./front/m2.txt"
            UpdateFileValue(file_name)
            


while(True):
    FileManipulation()
