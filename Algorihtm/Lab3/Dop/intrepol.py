import numpy as np

# Ввод данных
x0, x1, x2 = map(float, input("Введите через пробел точки x0, x1, x2: ").split())

# Заданная функция
def Function(x):
    return np.exp(x) + x**2 -2

# Считаем значения функции
y0 = Function(x0)
y1 = Function(x1)
y2 = Function(x2)

# Обратная квадратичная интерполяция
def Interpolation(x0, x1, x2, y0, y1, y2):
    # Формула для обратной квадратичной интерполяции
    denominator = (y0 - y1) * (y0 - y2) * (y1 - y2)
    
    # Коэффициенты интерполяционного полинома
    x_min = (
        (y1 * y2) / ((y0 - y1) * (y0 - y2)) * x0 +
        (y0 * y2) / ((y1 - y0) * (y1 - y2)) * x1 +
        (y0 * y1) / ((y2 - y0) * (y2 - y1)) * x2
    )
    
    return x_min

# Выполнение интерполяции
x_min = Interpolation(x0, x1, x2, y0, y1, y2)
y_min = Function(x_min)

# Вывод результатов
print(f"Значения y: y0 = {y0}, y1 = {y1}, y2 = {y2}")
print(f"Минимум функции: x = {x_min:.0f}, y = {y_min:.0f}")
