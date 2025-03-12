import numpy as np

# задём уравнение
def f(x):
    return np.exp(-x) + x**2 - 2

#Интервал, где функция меняет знак
def change(f, start, end, step = 0.1):
    x = start
    while x < end:
        if f(x) * f(x + step) < 0:
            return x, x + step
        x += step
    return None  

#Метод Дихотомии
def Dichotomy(f, a, b, eps = 1e-4, delt = 1e-6):
    if f(a) * f(b) > 0:
        raise ValueError("На интервале [-2;2] не меняет знак")
    

    while (b - a) / 2 > eps:
        x = (a + b) /2
        f_x = f(x)
    #Проверка на сходимость
    if abs(f_X) < delt:
        return x

        #Уменьшаем интервал
        if f(a) * f_x < 0:
            b = x
        else:
            a = x
    
    #Окончание интервала
    return (a + b) / 2 
interval = change(f, -10, 10, step = 0.1)
if interval:
    print(f"Функция меняет знак на интервале: {interval}")
else:
    print(f"На указанном интервале функци не меняет знак!")    
        #Нахождение корня на указанном иноервале
root = Dichotomy(f, -0.6, -0.5, eps=1e-4, delt=1e-6)

print(f"Корни уравнения: {root}")