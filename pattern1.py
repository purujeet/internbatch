i=1
num=int(input('Enter the number'))
k=num
while(num >= i):
    while(i<=num):
        print('*',end="")
        i=i+1
    print("")
    i=1
    num=num-1

print()
num=k-1
for row in range(0,num+1):
    for col in range(0,num-row+2):
        print('*',end='')
    print(' ')
