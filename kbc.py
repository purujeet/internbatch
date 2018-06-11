import random
questions={
        '1':['Q.2+3=?','a:4','b:5','c:6','b'],
        '2':['Q.5+3/3','a:4','b:5','c:6','c'],
        '3':['Q.Highest peak of world','a:Mount Everest','b:Mount Baton','c:MountValley','a'],
                
        }
ls=['1','2','3']


marks=0
name=input('Enter your name:')
print('\n\nWelcome to the trivia game\nRule #1:Right Score +10\nRule #2:Wrong Score -5')
random.shuffle(ls)
if input('\n\nPress any key if you wanna start:'):
    for i in range(0,len(ls)):
        print("\n\n",questions[ls[i]][0])
        print("",questions[ls[i]][1])
        print("",questions[ls[i]][2])
        print("",questions[ls[i]][3])
        x=input(' Enter your choice:')
        if(x==questions[ls[i]][4]):
            marks=marks+10
        else:
            marks=marks-5

    print('\n\n{},Your score is:{}'.format(name,marks))
else:
    print('You should have confident in yourself')


