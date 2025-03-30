import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Функция для интерполяции
interpolation_function = 'np.sin(x)'

# Входные данные
x = np.array([1.00, 1.04, 1.08, 1.12, 1.16, 1.20])
y = np.array([0.8415, 0.8624, 0.8820, 0.9001, 0.9168, 0.9320])

# Создаём кубический сплайн
cs = CubicSpline(x, y, bc_type='natural')

# Точки, в которых нужно найти значение сплайна
points = [1.05, 1.09, 1.13, 1.15, 1.17]

# Вычисляем сплайн в указанных точках
spline_values = cs(points)

# Вывод
print("Кубический сплайн:")
for point, value in zip(points, spline_values):
    print(f"S({point:.2f}) = {value:.6f}")

# Точные значения для сравнения с таблицей
exact_values = np.sin(points)
print("\nТочное значение cos(x):")
for point, exact_val in zip(points, exact_values):
    print(f"cos({point:.2f}) = {exact_val:.4f}")

#Вычислим погрешность
print("\nПогрешность:")
for point, spline_val, exact_val in zip(points, spline_values, exact_values):
    error = abs(spline_val - exact_val)
    print(f"Погрешность {point:.2f} = {error:.6f}")

#нарисуе график
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Узлы интерполяции', markersize=8)
xs = np.linspace(1.00, 1.20, 100)
plt.plot(xs, cs(xs), label='Кубический сплайн')
plt.plot(xs, np.cos(xs), '--', label='Точная функция sin(x)')
plt.plot(points, spline_values, 'ro', label='Вычисленные точки')
plt.title('Интерполяция sin(x) кубическим сплайном')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()