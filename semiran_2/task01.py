# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# n = int(input('Enter your number:'))
# m=1
# for i in range(n):
#     print(m,end=' ')
#     m*=-3

n = int(input('Enter your number:'))
for i in range(n):
    print((-3)**i,end=' ')