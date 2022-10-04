# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
from random import sample
def check_num_in_list(size,number):
    if number<0:
        return "Error"
    numbers = sample(range(1,size*2),size)
    print(numbers)
    if number in numbers:
        return "Yes"
    return "No"

print(check_num_in_list(int(input('Enter the size:')),int(input('Enter number:'))))

