k=(var**2 for var in range(10000) if var%2==0)
for i in k:
    print(next(k))
