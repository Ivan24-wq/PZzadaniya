import numpy as np
import time
import math

# Задаём уравнение
def f(x):
    return np.exp(-x) + x**2 - 2

# Интервал, где функция меняет знак
def change(f, start, end, step=0.1):
    x = start
    while x < end:
        if f(x) * f(x + step) < 0:
            return x, x + step
        x += step
    return None

# Метод Дихотомии
def Dichotomy(f, a, b, eps=1e-4, delt=1e-6):
    if f(a) * f(b) > 0:
        raise ValueError("На интервале [{}, {}] функция не меняет знак".format(a, b))

    # Запуск таймера
    start_time = time.time()

    while (b - a) / 2 > eps:
        x = (a + b) / 2
        f_x = f(x)
        
        # Проверка на сходимость
        if abs(f_x) < delt:
            end_time = time.time()
            print(f"Время выполнения алгоритма: {end_time - start_time:.8f}с")
            return x

        # Уменьшаем интервал
        if f(a) * f_x < 0:
            b = x
        else:
            a = x
    # Возвращаем середину интервала
    end_time = time.time()
    print(f"Время выполнения алгоритма: {end_time - start_time:.8f}с")
    return (a + b) / 2

    #Количество итерация для нахождения заданной точности
def iteration(a, b, eps):
    interval_length = b - a
    return math.ceil(math.log(interval_length / eps) / math.log(2))

# Поиск интервала изменения знака
interval = change(f, -10, 10, step=0.1)
if interval:
    a, b = interval
    eps = 1e-4
    print(f"Функция меняет знак на интервале: ({interval[0]:.4f}, {interval[1]:.4f})")
    #Вывод количества итераций
    n = iteration(a, b, eps)
    print(f"Достигли точность за: {n} итераций")
    # Нахождение корня на указанном интервале
    root = Dichotomy(f, *interval, eps=1e-4, delt=1e-6)
    print(f"Корень уравнения: {root:.4f}")
else:
    print("На указанном интервале функция не меняет знак!")
