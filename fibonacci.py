i=int(input("Enter the fibonnaci:"))
num1 = 0
num2 = 1
num3 = 0
print(num1)
while(num2<i):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num2)
