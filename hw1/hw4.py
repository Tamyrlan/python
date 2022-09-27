quarter = int(input('Enter quarter:'))
if quarter ==1:
    print('x>0,y>0')
elif quarter ==2:
    print('x<0,y>0')
elif quarter ==3:
    print('x<0,y<0')
elif quarter ==4:
    print('x>0,y<0')
else:
    print('There is no such quarter!')