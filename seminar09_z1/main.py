# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from isOdd import isOdd
import emoji

n = int(input("Введите количество элементов: "))
spisok = []
sum = 0
for i in range(n):
    spisok.append(int(input(f'Введите {i + 1} элемент ')))
    if isOdd(i):
        sum+=spisok[i]
print(emoji.emojize(f'Список элементов - {spisok} :red_heart:,\nСумма на нечётных позициях - {sum} :thumbs_up:'))
print(emoji.emojize('Задача решена на :thumbs_up:'))