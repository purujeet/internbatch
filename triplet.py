def solve(a, b):
    alice=0
    bob=0
    print(len(a))
    for i in range(0,len(a)+1):
        print('hello')
        if(a[i]>b[i]):
            alice=alice+1
        
        elif(b[i]>a[i]):
            bob=bob+1
        
        else:
            pass
        
    return alice,bob

    
a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = solve(a, b)

print(' '.join(map(str, result)))

