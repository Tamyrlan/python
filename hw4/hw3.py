# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности в том же порядке.

# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
from random import randrange
from collections import Counter
def random_num_list(number:int):
    if number <0:
        print('Wrong value, number can not be less than 0!')
        return []
    num_list = []
    for i in range(number):
        num_list.append(randrange(number))
    return num_list

def unique_num_list(num_list : list):
    new_list =[]
    count_list = Counter(num_list)
    for n, count in count_list.items():
        if count ==1:
            new_list.append(n)
    return new_list

rnd_list = random_num_list(int(input('Number of numbers:')))
print(rnd_list)
print(unique_num_list(rnd_list))
