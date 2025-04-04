import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

# Исходная функция
def f(x):
    return x**3 + 2 * x**2 + 6 * x - 9

# Контрольные точки на интервале [-2;2]
x_vals = [-2, -1, 0, 1, 2]
control = [(x, f(x)) for x in x_vals]

# Функция построения кривой Безье
def beze(control_points, points=200):
    n = len(control_points) - 1
    t_values = np.linspace(0, 1, points)  # Исправлено: t от 0 до 1
    curve = np.zeros((points, 2))

    for i in range(points):
        t = t_values[i]
        pts = np.zeros(2)
        for j, p in enumerate(control_points):
            bernstein_poly = comb(n, j) * (t ** j) * ((1 - t) ** (n - j))
            pts += bernstein_poly * np.array(p)
        curve[i] = pts

    return curve

# Построение кривой Безье
curve_pts = beze(control)

# Точки, в которых сравниваем значения
x_t = [-1.5, 0.6, 1.5]
y_beze = []
y_exact = []

# Сравнение значений на кривой и точной функции
for x_target in x_t:
    closest_index = np.argmin(np.abs(curve_pts[:, 0] - x_target))
    y_beze.append(curve_pts[closest_index, 1])
    y_exact.append(f(x_target))

# Построение графиков
x_vals_full = np.linspace(-2, 2, 400)
y_vals_full = f(x_vals_full)

plt.plot(x_vals_full, y_vals_full, 'g-', label="f(x) = x^3 + 2x^2 + 6x - 9")
plt.plot(*zip(*control), 'ro--', label="Контрольные точки")
plt.plot(curve_pts[:, 0], curve_pts[:, 1], 'b-', label="Кривая Безье")
plt.scatter(x_t, y_beze, color='blue', marker='x', label="Значения на Безье")
plt.scatter(x_t, y_exact, color='green', marker='o', label="Точные значения")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Сравнение кривой Безье и точной функции")
plt.grid(True)
plt.show()

# Вывод результатов
print("Контрольные точки:", control)
print("x =", x_t)
print("Значения на кривой Безье:", y_beze)
print("Точные значения функции:", y_exact)

# Абсолютные ошибки
errors = [abs(a - b) for a, b in zip(y_beze, y_exact)]
print("Абсолютные ошибки:", errors)

