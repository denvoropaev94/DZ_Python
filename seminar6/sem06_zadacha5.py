# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.

# 1 способ
kombination = [x**2 for x in range(10,100) if not x%9]
print(sum(kombination))


# 2 способ
# l = [i for i in range(10, 100)]
# l1 = list(filter(lambda x: x % 9 == 0, l))
# l2 = sum(list(map(lambda x: x**2, l1)))
# print(l2)