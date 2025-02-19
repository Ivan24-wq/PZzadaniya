import numpy as np
import time

# Реализация метода Монте-Карло
def MonteKarlo(func, a, b, epsilon):
    n = 1
    max_iteration = 20
    interval_length = b - a
    iteration = 0

    while True:
        iteration += 1
        iteration_start = time.time()  

        x_random = np.random.uniform(a, b, n)
        f_value = func(x_random)
        integral_estimate = interval_length * np.mean(f_value)

        # Погрешность
        variance = np.var(f_value)
        error_estimate = interval_length * np.sqrt(variance / n)

        iteration_end = time.time()  
        iteration_time = iteration_end - iteration_start  

        # Отладочная информация
        print(f"Итерация {iteration}:")
        print(f"   Интеграл ≈ {integral_estimate:.4f}, Погрешность ≈ {error_estimate:.4e}, n = {n}")
        print(f"   Время итерации: {iteration_time:.4f} сек")

        if error_estimate < epsilon:
            return integral_estimate, n
        # Увеличение числа точек
        n *= 2
       

# Функция для интегрирования
def F(x):
    return 1 / (0.5 * np.sin(x) + 3 * np.cos(x))**2

# Параметры (указанные в задании)
a = 0
b = 1.6
epsilon = 1e-4

start_time = time.time()

try:
    integral, points_used = MonteKarlo(F, a, b, epsilon)
    end_time = time.time()

    print(f"\nЗначение интеграла: {integral:.4f}")
    print(f"Использовано точек: {points_used}")
    print(f"Общее время выполнения алгоритма: {end_time - start_time:.4f} сек")
except ValueError as e:
    print(e)