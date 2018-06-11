s=list(map(int,input('Enter a string').split()))
print(*s)
s1=list(map(int,input('Enter a string').split()))
print(*s1)
s2=[]
s2=list(map(lambda x,y:x+y,s,s1))

'''for i in range(0,len(s)):
    s2.append(s[i]+s1[i])'''
print(*s2)
