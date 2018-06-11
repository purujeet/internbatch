n=lambda x:1 if x == 1 else x+n(x-1) 

print(n(int(input())))

