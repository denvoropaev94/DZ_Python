number1 = int(input('Введите позицию 1: '))
number2 = int(input('Введите позицию 2: ')) 
n = int(input('Введите число n'))
list = []
for i in range(-n,n+1):
    list.append(i)
p = list[number1] * list[number2]    
print(f'Список {list},Прозведение равно {p}')
