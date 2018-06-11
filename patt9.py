n=int(input("Enter a number:"))
p=n-1
ff=1
for i in range(0,n):
    print('')
    for j in range(0,p):
        print('*',end='')
    for k in range(1,ff+1):
        print(' ',end='')
    for l in range(0,p):
        print('*',end='')
    ff=ff+2    
    p=p-1
   

size=n
ss=2*size-1

for i in range(0,size):
    for j in range(0,i):
        print('*',end='')
    for k in range(0,ss):
        print(' ',end='')
    for l in range(0,i):
        print('*',end='')
    ss=ss-2
    print('')



