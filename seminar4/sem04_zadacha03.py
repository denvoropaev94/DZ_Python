# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# 1Вариант
# a=list(map(int,input().split()))
# new_list = []
# for i in a:
#    if a.count(i) == 1:
#         new_list.append(i)
# print(new_list)

# 2Вариант

a=list(map(int,input().split()))
num_list = []
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        # print(a[i], end=' ')
        num_list.append(a[i])
print(num_list)
