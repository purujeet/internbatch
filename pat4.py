n=int(input('Numb:'))
k=0
p=n
for i in range(0,n+1):
    for j in range(0,k):
        k=j
        print(' ',end='')
    for k in range(0,p):
        print('*',end='')
    print()
    p=p-i
