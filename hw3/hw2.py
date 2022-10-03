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
    if size%2==0:
        for i in range(int(size/2)):
            multi = my_list[i]*my_list[-1-i]
            mult.append(multi)
    elif size%2!=0:
          for i in range(int(size/2)):
            multi = my_list[i]*my_list[-1-i]
            mult.append(multi)      
          mult.append(my_list[int(size/2)])
    return mult


print(list_of_numbers(int(input(':'))))
