num=int(input('Enter a number:'))
for n in range(65,num+1):
    for col in range(65,n+1):
        print(chr(n),end='')
    print()


