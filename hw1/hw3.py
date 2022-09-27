x = int(input('Enter x:'))
y = int(input('Enter y:'))
if x>0 and y>0:
    print('1 четверть')
elif x<0 and y>0:
    print('2 четверть')
elif x<0 and y<0:
    print('3 четверть')
elif x>0 and y<0:
    print('4 четверть')
else:
    print('error')