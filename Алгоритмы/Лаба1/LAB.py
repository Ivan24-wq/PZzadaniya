import numpy as np
import time

# Функция для интегрирования
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
        y_new[::2] = y_prev  # Храним старые точки
        y_new[1::2] = f(x_new[1::2])  # Вычисляем только новые точки
        
        # Вычисляем новый интеграл
        I_new = Simpson(a, b, n, y_new)
        error = Runge(I_new, I_prev)  

        if error < eps:
            return I_new, n, error
        x_prev, y_prev, I_prev = x_new, y_new, I_new

    # Ошибка при превышении максимального числа разбиений
    raise ValueError("Не удалось достичь указанной точности")

# Реализация метода Монте-Карло
def MonteKarlo(func, a, b, epsilon):
    n = 100
    max_iteration = 100000  # Максимальное число точек
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
        print(f"Монте-Карло - Итерация {iteration}:")
        print(f"   Интеграл ≈ {integral_estimate:.4f}, Погрешность ≈ {error_estimate:.4e}, n = {n}")
        print(f"   Время итерации: {iteration_time:.4f} сек")

        if error_estimate < epsilon:
            return integral_estimate, n, iteration_end - iteration_start

        # Увеличение числа точек
        n *= 2
        if n > max_iteration:
            raise ValueError(f"Не удалось достигнуть точности за {iteration} итераций. "
                             f"Текущее значение: {integral_estimate:.4f}, погрешность: {error_estimate:.4e}")


# Сравнение методов
def compare_methods(a, b, epsilon):
    print("\n--- Метод Симпсона ---")
    try:
        start_simp = time.time()
        simpson_integral, simp_points, simp_error = chapter(a, b, epsilon)
        end_simp = time.time()
        print(f"\nМетод Симпсона:")
        print(f"   Значение интеграла: {simpson_integral:.4f}")
        print(f"   Число разбиений: {simp_points}")
        print(f"   Погрешность: {simp_error:.4e}")
        print(f"   Время выполнения: {end_simp - start_simp:.4f} сек")
    except ValueError as e:
        print(e)
        return

    print("\n--- Метод Монте-Карло ---")
    start_mc = time.time()
    monte_carlo_integral, mc_points, mc_time = MonteKarlo(f, a, b, epsilon)
    end_mc = time.time()

    print(f"\nМетод Монте-Карло:")
    print(f"   Значение интеграла: {monte_carlo_integral:.4f}")
    print(f"   Использовано точек: {mc_points}")
    print(f"   Время выполнения: {mc_time:.4f} сек")

    print("\n--- Результаты сравнения ---")
    print(f"Метод Симпсона:")
    print(f"   Значение интеграла: {simpson_integral:.4f}")
    print(f"   Время выполнения: {end_simp - start_simp:.4f} сек")
    print(f"\nМетод Монте-Карло:")
    print(f"   Значение интеграла: {monte_carlo_integral:.4f}")
    print(f"   Время выполнения: {mc_time:.4f} сек")


# Основной блок выполнения
if __name__ == "__main__":
    # Границы интегрирования(указанные в задании)
    a, b = 0, 1.6
    epsilon = 1e-4

    compare_methods(a, b, epsilon)
