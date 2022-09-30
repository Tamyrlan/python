# * 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
num = int(input('Enter Number of elements that you want:'))
numbers = []
for i in range(-num, num+1):
    numbers.append(i)
print(numbers)
position1 = int(input('Enter first position of elem:'))
position2 = int(input('Enter second position of elem:'))
if 0 <= position1 <= len(numbers) and 0 <= position2 <= len(numbers):
    position_one = numbers[position1-1]
    position_two = numbers[position2 - 1]
    summ = position_one+position_two
    print(f"The summ of numbers in those positions = {summ}")
else:
    print('Wrong number')
