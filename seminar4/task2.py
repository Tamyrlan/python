from math import sqrt


def sqr_roots(a, b, c):
    d = b**2-4*a*c
    if a==0:
        return 'error'
    with open('sqr.txt', 'a', encoding='utf-8') as my_file:
        my_file.write(f' {a}x² + {b}x + {c} = 0 \n')
        if d > 0:
            my_file.write(f'{(-b+sqrt(d))/(2*a)}\n')
            my_file.write(f'{(-b-sqrt(d))/(2*a)}\n')
        elif d == 0:
            my_file.write(f'{-b/(2*a)}\n')
        else:
            my_file.write('No root\n')


for i in range(3):
    sqr_roots(int(input('a:')), int(input('b:')), int(input('c:')))
    print()
