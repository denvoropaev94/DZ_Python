#Реализуйте алгоритм перемешивания списка.
import random
n = int(input("Введите количество элементов в списке "))
a = []
for i in range(n):
    a.append(i)
b = a[:]

random.shuffle(b)
print(f'Первый список {a}')
print(f'Перемешанный список {b}')       