s='1,2,3,4'

ls=s.split(',')
ls1=[]
for i in range(0,len(ls)):
    ls1.append(int(ls[i]))
    
print(ls1)
