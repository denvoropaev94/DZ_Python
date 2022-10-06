# Вычислить число c заданной точностью d
from decimal import Decimal

number = float(input("Введите число: "))
a = Decimal(number)
a = a.quantize(Decimal(input("Введите точность: ")))
print(a)