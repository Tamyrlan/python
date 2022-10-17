from random import randrange as rr
# def rand_list(num:int):
#     new_list = [rr(0,20) for i in range(num)]
#     return new_list

# def unique_elem(new_list:list):
#     unique_list = [new_list[i] for i in range(1,len(new_list)) if new_list[i]>new_list[i-1]]
#     return unique_list
# rnd_list = rand_list(int(input('Enter number:')))
# print(rnd_list)
# my_list = unique_elem(rnd_list)
# print(my_list)
def main(num):
    ls = [rr(0, 20) for i in range(num)]
    print(ls)

    res_ls = [ls[i] for i in range(1, num) if ls[i] > ls[i - 1]]
    print(res_ls)


n = int(input())
main(n)