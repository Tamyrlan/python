# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
from random import choices
def word_list(size,word):
    new_list =[]
    for i in range(size):
        word_1 = choices(word,k=3)
        new_list.append(''.join(word_1))
    return new_list

def count_word_in_list(my_list,word_2):
    if my_list.count(word_2)>1:
        print('Yes')
        n = my_list.index(word_2)
        print(my_list.index(word_2,n+1))
    else:
        print(-1)
result = word_list(20,'xyz')
print(result)
count_word_in_list(result,input())