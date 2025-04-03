import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

# Моя функция
def f(x):
    return x**3 + 2 * x**2 + 6 * x - 9

# Вычислим точки на интервале [-2;2]
x_vals = [-2, -1, 0, 1, 2]
control = [(x, f(x)) for x in x_vals]

# Функция для построения кривой Безье
def beze(control_points, points=20):
    n = len(control_points) - 1
    t_values = np.linspace(0, 1, points)
    curve = np.zeros((points, 2))  # Используем np.zeros вместо np.zero

    for i in range(points):
        t = t_values[i]
        pts = np.zeros(2)  # Используем np.zeros вместо np.zero
        for j, p in enumerate(control_points):
            bernstein_poly = comb(n, j) * (t ** j) * ((1 - t) ** (n - j))
            pts += bernstein_poly * np.array(p)
        curve[i] = pts  # Записываем точку на кривой

    return curve  # Эта строка должна быть на одном уровне с циклом

# Кривая Безье (график)
curve_pts = beze(control)

# Визуализация
x_vals_full = np.linspace(-2, 2, 400)
y_vals_full = f(x_vals_full)

# Построение графиков
plt.plot(x_vals_full, y_vals_full, 'g-', label="f(x) = x^3 + 2x^2 + 6x - 9")
plt.plot(*zip(*control), 'ro--', label="Контрольные точки")
plt.plot(curve_pts[:, 0], curve_pts[:, 1], 'b-', label="Кривая Безье")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("График")
plt.grid(True)
plt.show()

# Вывод контрольных точек
print(f"Контрольные точки:", control)
