num=int(input('Enter a number:'))
for n in range(65,num):
    for col in range(65,n+1):
        print(chr(col),end='')
    print()


