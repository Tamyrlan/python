# 4.* Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
from random import uniform
def random_list(n):
    a_list=[]
    if n<=0:
        print('error,wrong number')
        return 0
    
    for i in range(n):
        a_list.append(round(uniform(1,n),2))
    return a_list

def max_min_diff(a_list):
    max_num = a_list[0]%1
    min_num = a_list[0]%1
    for j in range(1,len(a_list)):
        num = round(a_list[j]%1,2)
        if num>max_num:
            max_num=num
        elif num<min_num:
            min_num=num
    result = round(max_num-min_num,2)
    return (f'min_elem={min_num} max_elem = {max_num} The difference between them = {result}')

result = random_list(int(input('x:')))
print(result)
print(max_min_diff(result))