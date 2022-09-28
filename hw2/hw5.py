# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
num = int(input())
numbers = list(range(num))
print(numbers)
for i in numbers:
    j = random.randrange(numbers[0],len(numbers))
    numbers[i] = numbers[j]
    k = random.randrange(numbers[0],len(numbers))
    numbers[i-1] = numbers[k]
print(numbers)
