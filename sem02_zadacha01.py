# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
num = input("Введите число: ")
summa = 0

if num.isdigit() == True :
    a=int(num)
    while (a != 0): 
     summa = summa + (a % 10)
     a = a // 10
else:
    x = num.split(".") 
    a = int(x[0]) # целая часть
    b = int(x[1]) # дробная часть
    while (a != 0): 
        summa = summa + (a % 10)
        a = a // 10
    while (b != 0):
        summa = summa + (b % 10)
        b = b // 10
print("Сумма цифр равно:", summa)