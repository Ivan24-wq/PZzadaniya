import numpy as np
import time
import math

# Задаём уравнение
def f(x):
    return np.exp(-x) + x**2 - 2

# Производная функции (метод Ньютона)
def g(x):
    return 2 * x - np.exp(-x)

# Ищем интервал, где функция меняет знак
def change(f, start, end, step=0.1):
    x = start
    while x < end:
        if f(x) * f(x + step) < 0:
            return x, x + step
        x += step
    return None

# Метод Дихотомии
def Dichotomy(f, a, b, eps=1e-4):
    if f(a) * f(b) > 0:
        raise ValueError(f"На интервале [{a}, {b}] функция не меняет знак")

    start_time = time.time()
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if abs(f(c)) < eps:
            end_time = time.time()
            print(f"Метод Дихотомии выполнен за: {end_time - start_time:.8f}с")
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    end_time = time.time()
    print(f"Метод Дихотомии выполнен за: {end_time - start_time:.8f}с")
    return (a + b) / 2

# Метод Ньютона
def Newton(f, g, x0, eps=1e-4, max_iteration=100):
    start_time = time.time()
    x = x0
    for i in range(max_iteration):
        f_x = f(x)
        g_x = g(x)

        
        if abs(f_x) < eps:
            end_time = time.time()
            print(f"Метод Ньютона выполнен за: {end_time - start_time:.8f}с")
            return x

        # Если производная равна нулю
        if g_x == 0:
            raise ValueError("Производная равна нулю!")

        # Формула Ньютона
        x = x - f_x / g_x

    end_time = time.time()
    print(f"Метод Ньютона выполнен за: {end_time - start_time:.8f}с")
    raise ValueError("Недостаточное количество итераций")

# Считаем количества итераций для метода Дихотомии
def iteration_count(a, b, eps):
    interval_length = b - a
    return math.ceil(math.log(interval_length / eps) / math.log(2))

# Сравниваем  методов
def Answer(f, g, a, b, eps=1e-4):
    
    root_Dichotomy = Dichotomy(f, a, b, eps)
    print(f"Метод Дихотомии: {root_Dichotomy:.6f}")

    
    root_Newton = Newton(f, g, root_Dichotomy, eps)
    print(f"Метод Ньютона: {root_Newton:.6f}")
    return root_Newton

# Запуск
if __name__ == "__main__":
    start, end, step = -10, 10, 0.1
    eps = 1e-4
    

    # Поиск интервала изменения знака
    interval = change(f, start, end, step)
    if interval:
        a, b = interval
        print(f"Функция меняет знак на интервале: ({a:.4f}, {b:.4f})")

        # Подсчёт количества итераций
        n = iteration_count(a, b, eps)
        print(f"Достигли точности за: {n} итераций методом Дихотомии")

        # Сравнение методов
        try:
            root = Answer(f, g, a, b, eps)
            print(f"Корень уравнения: {root:.4f}")
        except ValueError as e:
            print(f"Ошибка! {e}")
    else:
        print("На указанном интервале функция не меняет знак!")
