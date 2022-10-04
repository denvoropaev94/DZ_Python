# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import sample
import math

num = int(input("Number: "))
list_nums = sample(range(1, num * 2), num)
print(list_nums)
new_list = []
for i in range(math.ceil(len(list_nums)/2)):
    b = (list_nums[i]*list_nums[-i-1])
    new_list.append(b)
print(new_list)