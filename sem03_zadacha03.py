# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import sample

num = int(input("Number: "))
list_nums = [num / 100 for num in sample(range(1, num * 80), num)]
print(list_nums)
new_list=[]
for i in range(len(list_nums)):
    a = list_nums[i]
    d=(('{:.2f}'.format((a%1))))
    new_list.append(d)
maks = float(max(new_list))
mins = float(min(new_list))
result = maks - mins
print(f'Максимальная дробная часть - {maks}, Минимальная дробная часть - {mins}, Разница - {result}')