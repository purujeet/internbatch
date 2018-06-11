def prime(num):
    i=2
    prime='Prime'
    while(i<=(num//2+1)):
        if(num%i==0):
            prime='Not Prime'
            break
        i=i+1
    print('\n\n',prime)


while(input("\n\nType something to continue:")):
    num=list(map(input('enter a seq').split()))
    prime(num)


