num=int(input('Enter a number:'))
c=65
for n in range(1,num+1):
    for col in range(1,n+1):
        print(chr(c),end='')
        c+=1
    print()


