import random
num=random.randint(1,51)

c=6

while c:
    x=int(input('Guess number(1,50):'))

    if(c==1):
        print('You are a looser:',num)
        break

    if(x<num):
        print('Think bigger')
        c=c-1
    elif(x>num):
        print('Think small')
        c=c-1
    else:
        print('congrats.The number was:',num)
        y=input('Press Y to continue:')
        if(y=='y'or y=='Y'):
            c=5
        else:
            break
