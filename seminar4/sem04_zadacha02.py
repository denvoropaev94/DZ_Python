# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def Factor(n):
    spisok_mnoj = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            spisok_mnoj.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        spisok_mnoj.append(n)
    return spisok_mnoj

num = InputNumbers("Введите число: ")
print(Factor(num))