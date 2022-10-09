# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# in
# 54

# out
# [2, 3, 3, 3]

def num_mult(n: int):
    numbers = []
    for i in range(2, n):
        while n % i == 0 and n >= 0:
            numbers.append(i)
            n /= i
    return numbers


print(num_mult(int(input('Enter number:'))))
