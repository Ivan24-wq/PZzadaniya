import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Задаем равномерные узлы интерполяции с шагом h = 0.04
h = 0.04
x = np.arange(1.00, 1.20 + h, h)  # равномерное разбиение

# Выбираем функцию для интерполяции (например, cos(x))
y = np.cos(x)

# Создаем кубический сплайн
cs = CubicSpline(x, y, bc_type='natural')

# Точки, в которых нужно найти значение сплайна
points = [1.08, 1.09, 1.13, 1.15, 1.19]

# Вычисляем значения сплайна в указанных точках
spline_values = cs(points)

# Вывод результатов
print("Кубический сплайн:")
for point, value in zip(points, spline_values):
    print(f"S({point:.2f}) = {value:.6f}")

# Точные значения cos(x) для сравнения
exact_values = np.cos(points)
print("\nТочное значение cos(x):")
for point, exact_val in zip(points, exact_values):
    print(f"cos({point:.2f}) = {exact_val:.6f}")

# Вычисляем погрешность
print("\nПогрешность:")
for point, spline_val, exact_val in zip(points, spline_values, exact_values):
    error = abs(spline_val - exact_val)
    print(f"Погрешность {point:.2f} = {error:.6f}")

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Узлы интерполяции', markersize=8)
xs = np.linspace(1.00, 1.20, 100)
plt.plot(xs, cs(xs), label='Кубический сплайн')
plt.plot(xs, np.cos(xs), '--', label='Точная функция cos(x)')
plt.plot(points, spline_values, 'ro', label='Вычисленные точки')
plt.title('Интерполяция cos(x) кубическим сплайном')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
