m,n=list(map(int,input('Row and column:').split()))


A=[]
B=[]
s=[]

for i in range(0,m):

    A.append(list(map(int,input('Enter A matrix').split())))
    B.append(list(map(int,input('Enter B matrix').split())))



print(A)

print(B)

for i in range(0,m):
    for j in range(0,n):
      s.append( A[i][j]+B[i][j])



print(s)

print('Transpose of matrix:')

print('A=')
for i in range(0,n):
    for j in range(0,m):
        print('',A[j][i],end='')
    print()

print('B=')
for i in range(0,n):
    for j in range(0,m):
        print('',B[j][i],end='')
    print()



'''for i in range(0,x[0]):
    print('A',A[i],end='')
    print('B',B[i],end='')
    print('A+B',A[i]+B[i],end='')
'''




