n=int(input("Enter a number:"))
length=0
while n>0:
    n=n//10
    length=length+1
print('length',length)

num=n
sum1=0
while num:
    r=num%10
    n=n//10
    sum1=sum1+r**length
    

if(sum1==n):
    print('This is armstrong number')
else:
    print('This is not a armstrong number')
