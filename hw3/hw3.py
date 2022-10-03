# 3. Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Без использования встроенной функции преобразования,
# без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011
def decimal_to_binary(n):
    a = []
    while (n > 0):
        dig = n % 2
        a.append(dig)
        n = n//2
    a.reverse()
    print("Binary Equivalent is: ")
    for i in a:
        print(i,end='')
    return ' '
print(decimal_to_binary(int(input('Enter decimal number:'))))