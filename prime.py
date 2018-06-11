while(input("\n\nType something to continue:")):
    num=int(input('Enter a number:'))
    i=2
    prime='Prime'
    while(i<=(num//2+1)):
        if(num%i==0):
            prime='Not Prime'
            break
        i=i+1
    print('\n\n',prime)


