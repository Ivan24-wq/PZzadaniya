import numpy as np

# Задаём уравнение
def f(x):
    return np.exp(-x) + x**2 -2

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

    while (b - a) / 2 > eps:
        x = (a + b) / 2
        f_x = f(x)
        
        # Проверка на сходимость
        if abs(f_x) < delt:
            return x

        # Уменьшаем интервал
        if f(a) * f_x < 0:
            b = x
        else:
            a = x

    # Возвращаем середину интервала
    return (a + b) / 2

# Поиск интервала изменения знака
interval = change(f, -10, 10, step=0.1)
if interval:
    print(f"Функция меняет знак на интервале: ({interval[0]:.4f}, {interval[1]:.4f})")
    # Нахождение корня на указанном интервале
    root = Dichotomy(f, *interval, eps=1e-4, delt=1e-6)
    print(f"Корень уравнения: {root:.4f}")
else:
    print("На указанном интервале функция не меняет знак!")
