# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

from random import sample
def create_word_list(size : int):
    if size > 0:
        word_list = [''.join(sample('абв', k=3)) for _ in range(size)]
    else:
        word_list =[]
    return word_list

def sort_list(word_list:list):
    new_list = [word_list[i] for i in range(len(word_list)) if word_list[i]!='абв']
    return new_list
my_list = create_word_list(int(input('Enter the number of words thay u want :')))
print(my_list)
print(sort_list(my_list))