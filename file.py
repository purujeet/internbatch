name=input('Enter filename:')
filepath=input('Enter path where file to be saved:')
filepath+='\\'
filepath+=name
filepath+='.txt'
mode=input('Enter mode:')
fp=open(filepath,mode)

while True:
    if input('Wanna enter more data to quit press(!wq): ')!='!wq':

        fp.write(input('Give data:'))


    else:
        
        fp.seek(0)
        print(fp.read())

        break

