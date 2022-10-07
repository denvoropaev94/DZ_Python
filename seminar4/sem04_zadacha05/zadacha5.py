# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
with open("file4sem.txt","r") as file:
    data1 = file.read()
with open("file42sem.txt","r") as file:
    data2 = file.read()

st = data1.split(" = ")
result = st[0] + " + " + data2

print(result)
with open("file55.txt", "w") as file55:
    file55.write(result)
