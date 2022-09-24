#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def checkNumberQuarter(n):
    if n == 1:
        print('x>0 and y>0')
    elif n == 2:
        print('x>0 and y<0')
    elif n == 3:
        print('x<0 and y<0')
    elif n==4:
        print('x<0 and y>0')
    else:
        print('Вы ввели неверные данные')

num = InputNumbers("Введите номер четверти: ")
checkNumberQuarter(num)    
