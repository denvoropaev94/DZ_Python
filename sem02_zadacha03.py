#Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
num = int(input('Введите число: '))
list=[]
summa=0
for i in range(1, num + 1):
    list.append((1 + 1/i)**i)

list=[round(v) for v in list]
summa=sum(list)
print(f'Список{list},Сумма-{summa}')