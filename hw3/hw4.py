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
from random import randrange, uniform
num = int(input(':'))
n=[]
for i in range(1,num):
    n.append(round(uniform(1.0,99.9),2))
print(n)
for i in n:
    max=0
    min=0
    if max<n[i]:
        max=n[i]
    elif max>n[i]:
        min=n[i]
print(min,max)