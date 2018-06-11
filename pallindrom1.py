n=int(input('Enter a number:'))
num=n
s=0
while(n>0):
    r=n%10
    n=n//10
    s=s*10+r
if s==num:
    print('Pallindrom')
else:
    print('Not pallindrom')
