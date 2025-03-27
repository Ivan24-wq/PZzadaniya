import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, simplify

# Исходные данные
x_val = [1, 2, 3, 4, 5]
y_val = [8.2, 5.9, 4.9, 4, 3.2]

# Функция для построения базисного полинома Лагранжа
def lagrange_basis(x_val, x, i):
    L_i = 1
    for j in range(len(x_val)):
        if j != i:
            L_i *= (x - x_val[j]) / (x_val[i] - x_val[j])
    return L_i

# Функция для построения полного полинома Лагранжа
def lagrange_polynom(x_val, y_val, x):
    P_x = 0
    for i in range(len(x_val)):
        L_i = lagrange_basis(x_val, x, i)
        P_x += y_val[i] * L_i
    return simplify(P_x)

# Символ для полинома
x = symbols('x')

# Вычисление полинома
P_x = lagrange_polynom(x_val, y_val, x)
print(f"Полином Лагранжа: {P_x}")

# Преобразование в функцию для вычислений
P_x_func = lambdify(x, P_x, modules=['numpy'])

# Создание точек для графика
x_plot = np.linspace(min(x_val) - 1, max(x_val) + 1, 500)
y_plot = P_x_func(x_plot)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x_plot, y_plot, label="Полином Лагранжа", color='blue')

# Добавление исходных точек
plt.scatter(x_val, y_val, color='red', label="Исходные точки")
for x_point, y_point in zip(x_val, y_val):
    plt.annotate(f"({x_point:.1f}, {y_point:.1f})", (x_point, y_point), textcoords="offset points", xytext=(-10, 10), ha='center')

# Настройка осей
plt.axhline(0, color='black', linewidth=0.8, linestyle="--")
plt.axvline(0, color='black', linewidth=0.8, linestyle="--")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Подписи 
plt.title("Интерполяционный полином Лагранжа")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Отображение графика
plt.show()
