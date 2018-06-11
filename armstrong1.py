k1=int(input('Enter starting number:'))
k2=int(input('Enter ending number:'))

for i in range (k1,k2+1):
    n=i
    num=n

    c=0

    while n>0:
        n=n//10
        c=c+1
    n=num
    s=0
    while n:
        r=n%10
        n=n//10
        s=s+r**c
    if s==num:
        print(s,end='\t')
 
