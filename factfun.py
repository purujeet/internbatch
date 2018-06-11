def fact(num):
    fact=1
    '''if(num==1):
        return 1
    else:
        return num*fact(num-1)'''
    while(num>1):
        fact=fact*num
        num=num-1
    return fact

if __name__=='__main__':
    print('__name__',__name__)
    res=fact(int(input('Enter any number:')))
    print('res=',res)
        
