# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000
from decimal import Decimal
def accuracy(n:float,acc:float):
    num = Decimal(f'{n}')
    num = num.quantize(Decimal(f'{acc}'))
    return num
print(accuracy(float(input('Enter real number')),float(input('Enter accuracy that you want -> 0.0001:'))))
