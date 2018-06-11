n=int(input("Enter a number:"))
p=n-1
ff=1
for i in range(0,n):
    for j in range(0,p):
        print(' ',end='')
    for k in range(1,ff+1):
        print('*',end='')
    ff=ff+2    
    p=p-1
    print('')


