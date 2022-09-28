# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
num = float(input('Enter your number:'))
n = len(str(num))-1
summ = 0
num = int(num*10**n)
while num > 0:
    digit = num % 10
    summ = summ + digit
    num = num // 10
print(summ)
