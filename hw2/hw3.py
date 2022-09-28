# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
numbers = []
n = int(input('Enter n:'))
summ = 0
for i in range(1, n+1):
    num = (1+1/i)**i
    numbers.append(round(num))
    summ = summ + round(num)
print(numbers)
print(f"the sum of numbers = {summ}")
