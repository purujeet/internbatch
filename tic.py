import random
import time
ls=[0,1,2,3,4,5,6,7,8]

count=0
dic={
        0:'00',
        1:'01',
        2:'02',
        3:'10',
        4:'11',
        5:'12',
        6:'20',
        7:'21',
        8:'22',

        }

mat=[['_','_','_'],['_','_','_'],['_','_','_']]

def play(y):
    global i1,i2,ls
    i1=int(dic[y][0])
    i2=int(dic[y][1])
    ls.remove(y)




def complay():
    global ls
    x=random.choice(ls)
    play(x)
    
    mat[i1][i2]='O'

    print('COMPUTER TURN:',x)

    for var in mat:
        print(*var)
   


def usrplay():
    
    n=int(input('Your Turn:'))
    
    if n in ls:
        play(n)
        mat[i1][i2]='X'
        for var in mat:
            print(*var) 

    else:
        print('This number is already taken')
        usrplay()

    

def check(z):
    global count

    count+=1

    
    if(mat[0][0]==z and mat[0][1]==z and mat[0][2]==z):
        print('\nYou Won the Match');main()
    elif(mat[1][0]==z and mat[1][1]==z and mat[1][2]==z):
        print('\nYou Won the Match');main()
    elif(mat[2][0]==z and mat[2][1]==z and mat[2][2]==z):
        print('\nYou Won the Match');main()
    
    elif(mat[0][0]==z and mat[1][1]==z and mat[2][2]==z):
        print('\nYou Won the Match');main()
    elif(mat[2][0]==z and mat[1][1]==z and mat[0][2]==z):
        print('\nYou Won the Match');main()
     
    elif(mat[0][0]==z and mat[1][0]==z and mat[2][0]==z):
        print('\nYou Won the Match');main()
    elif(mat[0][1]==z and mat[1][1]==z and mat[2][1]==z):
        print('\nYou Won the Match');main()
    elif(mat[0][2]==z and mat[1][2]==z and mat[2][2]==z):
        print('\nYou Won the Match');main()
    
    
    if count==9:
        print('This is a draw')
        main()
    
    

def main():
    global ls
    global count
    
    ch = input('\n\nWanna play Tic Tac Toe(y/n)? - > ')
    if ch =='y' or ch=='Y':
        while True:
            
            complay()
            check('O')

            usrplay()
            check('X')
            
            if(len(ls)==0):
                break   
            
    elif ch=='n' or ch=='N':
        exit(0)
    else:
        print('Invalid input')
        main()
main()
   

