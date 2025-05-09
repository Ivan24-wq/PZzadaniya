import numpy as np

# Функция — принимает вектор x
def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

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
def method(f, b1, h, eps=1e-12, max_iters=10000):
    iter_count = 0
    while np.linalg.norm(h) > eps and iter_count < max_iters:
        iter_count += 1
        b2 = investigate_search(b1, h)
        if np.array_equal(b2, b1):
            h = h / 2.0
            continue
        else:
            P = b1 + 2 * (b2 - b1)
            if f(P) < f(b2):
                b1 = P
            else:
                b1 = b2
        if iter_count % 100 == 0:  
            print(f"Итерация {iter_count}: x = {b1}, f(x) = {f(b1):.5f}")        
    return b1, f(b1)

# Входные значения
b1 = np.array([0.0, 0.0])
h = np.array([0.01, 0.01])

# Запуск программы
min_point, min_value = method(f, b1, h)
print(f"Минимум функции: f = {min_value:.3f} в точке x = {min_point}")