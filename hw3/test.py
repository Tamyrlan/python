size = int(input())
my_list = []
for i in range(size):
    my_list.append(i)
print(my_list)
summ =0
for i in range(len(my_list)):
    summ = summ+ my_list[i]
print(summ)