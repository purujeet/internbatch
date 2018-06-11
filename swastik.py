import time
n=int(input("Enter a number:"))
times=n//2+1
if(n%2!=0):
    for i in range(1,n+1):
        #time.sleep(1)
        if(i<times):
            print('*',end="")
            for j in range(0,times-2):
                print(' ',end="")
            if(i==1):
                for k in range(0,times):
                    print('*',end="")
                print('')        
            else:
                print('*')
        elif(i>times):
            if(i!=n):
                for j in range(0,times-1):
                    print(' ',end="")
                print('*',end='')
            else:
                for k in range(0,times):
                    print('*',end="")
         
            for k in range(0,times-2):
                print(' ',end='')
            print('*')
        
        else:
            for j in range(0,n):
                print('*',end='')
                
            print('')
else:
    print('Enter a odd number')

