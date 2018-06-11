def add(num):

    if num==1:
        return 1
    else:
        
        return num+add(num-1)
n=int(input('Enter any number:'))
print(add(n))
