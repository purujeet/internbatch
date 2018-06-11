import getpass
rec={
        'name':['John','Rohan','Mohan'],
        'acc':[1001,1002,1003],
        'bal':[5000,10000,20000],
        'pass':['abc','bcd','123']

        
        }




while(input('Press any key to continue:')):
    print('\n\n1.Login \n2.SignUp')
    ch=int(input('Enter your choice:'))
    if (ch==1):
        acc=int(input('Enter account number:'))
        
        if acc in rec['acc']:
            passwd=getpass.getpass()
            i=rec['acc'].index(acc)
            if(rec['pass'][i]==passwd):
                print('Welcome to our bank')
            else:
                print('Password Mismatch! You need to sign up again')

        else:
            print('No such user exist')


    elif ch==2:
        name=input('Enter your name')
        rec['name'].append(name)

        bal=int(input('Enter your bal'))
        rec['bal'].append(bal)

        acc=rec['acc'][-1]+1
        rec['acc'].append(acc)

        password=getpass.getpass()
        rec['pass'].append(password)

        print('Kindly note down your acc no:',acc)
    

    else:
        print('Invalid choice')

