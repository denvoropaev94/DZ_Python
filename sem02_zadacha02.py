# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до n
num = int(input('Введите число: '))
p=1
num_list=[]

for i in range(1,num+1):
    p = p*i
    num_list.append(p)
    

print(num_list)