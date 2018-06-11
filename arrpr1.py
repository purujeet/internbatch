m,n=list(map(int,input('Row and column:').split()))
A=[]
B=[]

#A.append(map(int,input('Enter matrix A').split())) for i in range(m)
#B.append(map(int,input('Enter matrix B').split())) for i in range(m)

print('Enter matrix:')
for i in range(m):
    ls=list(map(int,input().split()))
    A.append(ls)
print('Enter matrix')
for j in range(m):
    ls=list(map(int,input().split()))
    B.append(ls)


print('Matrix A:',A)

print('Matrix B:',B)


s=[]
print('\n\nSum of the matrix\n')
for i in range(m):
    ls=[]
    for j in range(n):
        ls.append(A[i][j]+B[i][j])
    s.append(ls)

print(*s)
d=[]
print('\n\nDifference of the matrix\n')
for i in range(m):
    ls=[]
    for j in range(n):
        ls.append(A[i][j]-B[i][j])
    d.append(ls)
print(*d)

print('\n\nMultiplication of the matrix\n')


dic={
        1:[0,0],
        2:[0,1],
        3:[1,0],
        4:[1,1],  
        
        
        }

mul=[]

x=m*n

for i in range(1,x,2):
    
    for j in range(1,n+1):
        
        e1=dic[i][0]
        e2=dic[i][1]

        e3=dic[j][0]
        e4=dic[j][1]

        e5=dic[i+1][0]
        e6=dic[i+1][1]

        e7=dic[j+2][0]
        e8=dic[j+2][1]

        #print('op:',A[e1][e2]*B[e3][e4]+A[e5][e6]*B[e7][e8])

        print('{}{}*{}{}+{}{}*{}{}={}'.format(e1,e2,e3,e4,e5,e6,e7,e8,A[e1][e2]*B[e3][e4]+A[e5][e6]*B[e7][e8]))

        #print('{}*{}+{}*{}'.format(dic[i],dic[j],dic[i+1],dic[j+2]))
        
        
        #print(A[dic[i][0]][[dic[i][1]]])
        
        #print(A[dic[i]]*B[dic[j]]+A[dic[i+1]]*B[dic[j+2]])


    print()








'''

for i in range(m):
    ls1=[]
    ls=[]

    for j in range(n):
        
        ls.append(A[i][j]*B[j][i])
        ls.append()
       
    print(ls)
    print(sum(ls))
    ls1.append(sum(ls))

    mul.append(ls1)
print(mul)
'''

