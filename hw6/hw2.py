from audioop import mul


def multiplicity(n:int):
    if n>20:
        li = [i for i in range(20, n) if not(i % 20) or not(i % 21)]
        return li
    else:
        return 'Wrong number'
mtp = multiplicity(int(input('Enter a number of elemnts(it has to be greater than 20):')))
print(mtp)