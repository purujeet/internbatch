n=int(input("Enter a number:"))
p=n
for i  in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(0,p):
        print("*",end="")
    print("")
    p=n-i
