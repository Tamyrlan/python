# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import sample


def list_of_numbers(size):
    my_list = []
    if size < 0:
        return "Wrong number"
    my_list = sample(range(1, size*2), size)
    print(my_list)
    mult = []
    for i in range(int(len(my_list)/2)):
        multi = my_list[i]*my_list[i-1]
        mult.append(multi)
    return mult


print(list_of_numbers(int(input(':'))))
