print('Введите день недели в цифре от 1 до 7:')
num = int(input())
if num<6:
    print('нет, сегодня рабочий день:(')
elif num>=6:
    print('да, сегодня выходной :)')