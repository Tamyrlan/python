# 1. Задайте список, состоящий из произвольных чисел,
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22
from random import sample


def list_of_numbers(size,summ):
    my_list = []
    if size < 0:
        return "Wrong number"
    my_list = sample(range(1, size*2), size)
    print(my_list)
    for i in range(0, len(my_list), 2):
        summ+=my_list[i]
    return f'the sum of elem => {summ}'

print(list_of_numbers(int(input()),0))
