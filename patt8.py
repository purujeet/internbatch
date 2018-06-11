size=int(input('Enter a number:'))
ss=2*size-1

for i in range(0,size):
    for j in range(0,i):
        print(' ',end='')
    for k in range(0,ss):
        print('*',end='')
    ss=ss-2
    print('')



        
