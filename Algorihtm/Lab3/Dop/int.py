import numpy as np

#Задаю данные x0, x1, x2
x_points = [2.9, 3.5, 3.9]
#Задаю y0, y1, y2
y_points = [-0.13, 5.6e-3, 0.05]

#Формула Лагранжа
def Lagrang(x_val):
    #Вычисляем каждый член
    def l(k, x_val):
        result = 1
        for i in range(len(x_points)):
            if i != k:
                result *=(x_val - x_points[i])/(x_points[k] - x_points[i])
        return result
    #Просумерием все члены
    result = 0
    for k in range(len(x_points)):
        result += y_points[k] * l(k, x_val)
    return result

#Вывод результата
#Контрольный результат
x_test = 3.4
print(f"ОТвет: {Lagrang(x_test)}")