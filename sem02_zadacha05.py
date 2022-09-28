#Реализуйте алгоритм перемешивания списка.
import random
n = int(input())
a = []
for i in range(n):
    a.append(i)
b = a[:]

random.shuffle(b)
print(a)
print(b)       