import numpy as np

#Ввод данных
x0, x1, x2 = map(float, input("Введи через пробел приближенные x0, x1, x2: ").split())

#Заданная функция
def Function(x):
    return (np.log(10)/np.log(x) - 7/(2*x + 6))
    #Аварийное число
    if (x==-3):
        print("Ошибка! На ноль делить нельзя!")