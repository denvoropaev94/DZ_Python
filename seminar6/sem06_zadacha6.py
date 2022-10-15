# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
spisok=list(map(int,input().split()))
new_list = [i for i in spisok if spisok.count(i) == 1]
print(new_list)