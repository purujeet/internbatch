n = int(input("Number :"))
import math

k = int(math.sqrt(n) + 1)
f = 1
for var in range(2,k+1) :

    if n % var == 0 and var !=2 :
        
        f = 0 
        break
if f==0:
    print('Not prime')
else:
    print('prime')
    
