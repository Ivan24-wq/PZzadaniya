import numpy as np
import time

# Определяем функцию f(x).
def f(x):
    return 1 / (0.5 * np.sin(x) + 3 * np.cos(x))**2

# Метод Симпсона
def Simpson(a, b, n, y = None):
    h = (b - a) / n  # Вычисляем шаг
    if y is None:
        x = np.linspace(a, b, n + 1)
        y = f(x)

    # Метод Симпсона
    integral = h / 3 * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[n])
    return integral

# Оценка погрешности по Рунге
def Runge(I2h, Ih, p=4):
    return abs(Ih - I2h) / (2**p - 1)

# Подбор числа разбиений
def chapter(a, b, eps=1e-4, n_min=2, n_max=1000):
    n = n_min
    x_prev = np.linspace(a, b, n + 1)
    y_prev = f(x_prev)  # Вычисляем значения функции для начального разбиения
    I_prev = Simpson(a, b, n, y_prev)

    while n <= n_max:
        n *= 2
        # Добавляем новые точки, вместо пересчета всей сетки
        x_new = np.linspace(a, b, n + 1)
        y_new = np.empty(n + 1)
        y_new[::2] = y_prev  # Сохраняем старые точки
        y_new[1::2] = f(x_new[1::2])  # Вычисляем только новые точки
        
        # Вычисляем новый интеграл
        I_new = Simpson(a, b, n, y_new)
        error = Runge(I_new, I_prev)  # Оценка ошибки

        if error < eps:
            return I_new, n, error
        x_prev, y_prev, I_prev = x_new, y_new, I_new

    # Ошибка при превышении максимального числа разбиений
    raise ValueError("Не удалось достичь указанной точности")

# Границы интегрирования
a, b = 0, 1.6
epsilon = 1e-4

start_time = time.time()


# Вычисление интеграла
I, n_final, error_final = chapter(a, b, epsilon)
end_time = time.time()

# Вывод результатов
print(f"Численное значение интеграла: {I:.4f}")
print(f"Число разбиений: {n_final}")
print(f"Погрешность: {error_final:.4e}")
print(f"Время выполнения алгоритма: {end_time - start_time:.4f} с")