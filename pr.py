M=input('')
x=M.split(' ')
N=int(x[1])
M=int(x[0])
s='.|.'
s1='welcome'
k=N//2
j=N
for i in range(0,N):
    for n in range(0,M):
        if(n==k):
            print(s1.center(N,'-'),end='')
        elif(n<k):
            print(s.center(N,'-'),end='')
        else:
            print(s.center(N,'-'),end='')
    print('')
