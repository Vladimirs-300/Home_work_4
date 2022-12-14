# 1. Вычислить число c заданной точностью d

from decimal import Decimal


def accuracy(num, acc):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{acc}"))


print(accuracy(float(input("Введите натуральное число: ")), float(input("Введите точность 0.001: "))))
