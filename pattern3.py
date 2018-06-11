n=int(input("Enter a number:"))
p=n
for i in range(1,n+1):
    for j in range(p,0,-1):
        print(' ',end="")
    for k in range(0,i):
        print('*',end='')
    print('')
    p=n-i

