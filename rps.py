import random
l=['r','p','s']

while (input("Press any key to continue:")):
    k=random.choice(l)
    user=input('Enter r,p,s:')

    if user==k:
        print('You are the winner')
    else:
        print('You are the looser')


