#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

x1, y1 = map(int, input('Координаты первой точки (x, y): ').split())
x2, y2 = map(int, input('Координаты второй точки (x, y): ').split())

def FindDistanse(x1,y1,x2,y2):
    S = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    return S

result = FindDistanse(x1,y1,x2,y2)
print(('{:.2f}'.format(result)))