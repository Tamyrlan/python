print('Введите день недели в цифре от 1 до 7:')
num = int(input())
if 1<=num<6:
    print('нет, сегодня рабочий день:(')
elif 6<=num<=7:
    print('да, сегодня выходной :)')
else:
    print('Такого дня недели не сущетсвует')