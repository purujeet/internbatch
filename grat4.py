w=int(input('w:'))
x=int(input('X:'))
y=int(input('y:'))
z=int(input('z:'))


if w>=x and w>=y and w>=z:
    print('w is greater')

elif x>=w and x>=y and x>=z:
    print('x is greater')

elif y>=w and y>=x and y>=z:
    print('y is greater')

else:
    print('z is greater')


