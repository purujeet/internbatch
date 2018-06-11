n,m,k=map(int,input('Row and column:').split())

A=[]
print('Enter matrix A:')
for i in range(n):
    x=list(map(int,input().split()))
    A.append(x)

print(A)
B=[]
print('Enter matrix B:')
for i in range(m):
    x=list(map(int,input().split()))
    B.append(x)

print(B)
res=0
for i in range(n):
    for j in range(k):
        for z in range(m):
            
            res+=A[i][z]*B[z][j]
            
            
        print(res,end='')
        res=0
        
    print()
        
