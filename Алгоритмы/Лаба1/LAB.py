import numpy as np
import time

# Функция для интегрирования
def f(x):
    return 1 / (0.01 + abs(x))

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
def chapter(a, b, eps=1e-4, n_min=2, n_max=10000):
    n = n_min
    x_prev = np.linspace(a, b, n + 1)
    y_prev = f(x_prev)  # Вычисляем значения функции для начального разбиения
    I_prev = Simpson(a, b, n, y_prev)

    while n <= n_max:
        n *= 2
        
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
def MonteKarlo(f, a, b, epsilon, initial_n=100, max_iteration=10000):
    n = initial_n  # Начальное количество точек
    interval_length = b - a
    iteration = 0
    
    while True:
        iteration += 1
        start_time = time.time()
        
        # Генерация случайных точек и вычисление значений функции
        x_random = np.random.uniform(a, b, n)
        f_value = f(x_random)
        integral_estimate = interval_length * np.mean(f_value)

        # Оценка дисперсии и ошибки
        variance = np.var(f_value)
        error_estimate = interval_length * np.sqrt(variance / n)
        
        # Время выполнения итерации
        iteration_time = time.time() - start_time

        # Условие завершения
        if error_estimate < epsilon or iteration >= max_iteration:
            print(f"Итерация {iteration}: интеграл ≈ {integral_estimate:.6f}, "
                  f"погрешность ≈ {error_estimate:.6f}, точки: {n}, "
                  f"время {iteration_time:.4f} с")
            break

        # Увеличение числа точек (адаптивное)
        n = int(n * (error_estimate / epsilon) ** 2)

    return integral_estimate, error_estimate, iteration


# Сравнение методов
def compare_methods(a, b, epsilon):
    print("\n--- Метод Симпсона ---")
    try:
        start_simp = time.time()
        simpson_integral, simp_points, simp_error = chapter(a, b, epsilon)
        end_simp = time.time()
        print(f"\nМетод Симпсона:")
        print(f"   Значение интеграла: {simpson_integral:.8f}")
        print(f"   Число разбиений: {simp_points}")
        print(f"   Погрешность: {simp_error:.4e}")
        print(f"   Время выполнения: {end_simp - start_simp:.8f} сек")
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
    a, b = -1, 1
    epsilon = 1e-4

    compare_methods(a, b, epsilon)
