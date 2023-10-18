import sys
import os
    
player = sys.argv[1]
tables = sys.argv[2]

files = ['m1.txt', 'm2.txt']

old_name = r"C:/Users/disrct/Desktop/AIcsharpJp/notakto-ai/front/m2 last.txt"
new_name = r"C:/Users/disrct/Desktop/AIcsharpJp/notakto-ai/front/m1.txt"


def UpdateFileValue(file_name):
    f = open(file_name, "r")
    print(f.read())


def GetFileValue():
    print('')



def GetFileName():
    for f_name in os.listdir('front'):
        if f_name.endswith('last.txt'):
            return f'./front/{f_name}'
        else:
            return open("./front/m1.txt", "a").write('0 1')
        

def FileManipulation():
    file_name = GetFileName()
    if(player == 'm1'):
        os.rename(file_name,'./front/m1.txt')
    else:
        os.rename(file_name,'./front/m2.txt')
    UpdateFileValue(file_name)
        # for f_name in os.listdir('./front'):
        #     file = f_name.endswith('.txt')
        # os.rename(f'./front/{file}.txt','./front/m1.txt')

        # f = open("./front/m1.txt", "a").truncate(0)
        # f.write("Now the file has more content!")
        # f.close()
    # else:
    #     os.rename('./front/m1 last.txt','./front/m2.txt')
    #     f = open("./front/m1.txt", "a")
    #     f.write("Now the file has more content!")
    #     f.close()


FileManipulation()
