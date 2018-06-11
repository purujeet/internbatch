import time
num=int(input("Enter any number:"))
z=0
i=1
while(i<=num):
    while(z<i):
        print('*',end="")
        z=z+1
        time.sleep(1)
    z=0
    i=i+1
    print('')

print()

for n in range(1,num+1):
    for col in range(1,n+1):
        print('*',end='')
    print()

