import numpy as np

# Функция — принимает вектор x
def f(x):
    return (x[0] - 1) * np.sin(x[1]) + 5

# Метод исследования
def investigate_search(b, h):
    b_new = np.copy(b)
    for j in range(len(b)):
        improved = False
        for direction in [-1, 1]:
            x_try = np.copy(b_new)
            x_try[j] += direction * h[j]
            if f(x_try) < f(b_new):
                b_new = x_try
                improved = True
                break
        if not improved:
            continue
    return b_new

# Метод нулевого порядка
def method(f, b1, h, eps=1e-5, max_iters=1000):
    iter_count = 0
    while np.linalg.norm(h) > eps and iter_count < max_iters:
        iter_count += 1
        b2 = investigate_search(b1, h)
        if np.array_equal(b2, b1):
            h = h / 10.0
            continue
        else:
            P = b1 + 2 * (b2 - b1)
            if f(P) < f(b2):
                b1 = P
            else:
                b1 = b2
    return b1, f(b1)

# Входные значения
b1 = np.array([0.0, 0.0])
h = np.array([1.0, 1.0])

# Запуск программы
min_point, min_value = method(f, b1, h)
print(f"Минимум функции: f = {min_value:.3f} в точке x = {min_point}")
