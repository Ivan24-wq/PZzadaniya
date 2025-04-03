import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Функция для интерполяции
interpolation_function = 'np.cos(x)'

# Входные данные
x = np.array([1.00, 1.01, 1.02, 1.03, 1.04,  1.06, 1.07, 1.08,  
              1.10, 1.11, 1.12,  1.14,  1.16,  1.18, 1.19, 1.20])
y = np.array([0.5403, 0.5319, 0.5234, 0.5148, 0.5062,  0.4889, 0.4801, 
              0.4713,  0.4536, 0.4447, 0.4357, 0.4176,  
              0.3993, 0.3810, 0.3718, 0.3624])
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
exact_values = np.cos(points)
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
plt.plot(xs, np.cos(xs), '--', label='Точная функция cos(x)')
plt.plot(points, spline_values, 'ro', label='Вычисленные точки')
plt.title('Интерполяция cos(x) кубическим сплайном')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()