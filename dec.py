def hello(name,design):
    return 'Welcome '+name

def dec(old_fun):
    def make_up(x,y):
        s=''
        for i in range(0,20):
            s=s+y
        s=s+'\n'

            
        s+=old_fun(x,y)
        
        s=s+'\n'
        for i in range(0,20):
            s=s+y
        return s
    return make_up
hello=dec(hello)

name=input("Enter your name:")
design=input("Enter your design:")

k=hello(name,design)
print(k)
