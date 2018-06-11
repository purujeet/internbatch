tags=[]
tags1=[]

def x():
    global tags,tags1
    
    while(input('Press y to add tag:')=='y'):
        k='<'
        x=input('Tag:')
        k+=x
        k+='>'
        tags.append(k)
        tags1.append(x)
   

    body=input('Enter description:')
    tags.append(body)
    print(tags)
    tg=tags1[-1]

    while(input('Want to close {}(y/n)?:'.format(tg))=='y'):
        k='</'
        k+=tags1[-1]
        k+='>'
        tags.append(k)
        print(tags)
        tags1.pop()
        
        if len(tags1)!=0:
            tg=tags1[-1]
        else:
            break
        
    s=''
    for i in range(0,len(tags)):
        
        s+=tags[i]
        s+='\n'

    return s
        

def dec(old_fun):
    def makeup():
        global ls,tag,body
        s='\n\n\n<html>\n<head>\n'
        s+='\n<title>\n'
        s+=input('Enter title:')
        s+='\n</title>\n</head>\n'
        s+=old_fun()
        s+='\n</html>'
        return s
    return makeup

        
while(input('Press any key to make a webpage:')):    
    x=dec(x)
    print(x())


