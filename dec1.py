def hello(name):
    return 'hello '+name

def dec(old_fun):
    def make_up(x):
        s='Hello world welcome to python'
        s+=old_fun(x)
        s+="\nHi this is a decorator"
        return s
    return make_up
hello=dec(hello)


k=hello('purujeet')
print(k)

    
