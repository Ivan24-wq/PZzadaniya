import numpy as np
import matplotlib.pyplot as plt

# Входные данные
def f(x):
    return np.exp(x) + x

# Первая производная
def gradient_f(x):
    return np.exp(x) + 1

# Вторая производная
def hessian_f(x):
    return np.exp(x)

# Метод Ньютона (второго порядка)
def Newton(f, gradient_f, hessian_f, x0, eps=1e-6, max_iter=1000):
    x = x0
    for k in range(max_iter):
        gradien = gradient_f(x)
        hessian = hessian_f(x)

        # Критерий остановки
        if abs(gradien) < eps:
            print(f"Итерация {k}: Градиент мал, метод завершён.")
            return x

        # Проверка на слишком малый или нулевой гессиан
        if abs(hessian) < eps:
            print(f"Итерация {k}: Гессиан близок к нулю, метод завершён.")
            return x

        
        p = -gradien / hessian

        # Обновляем x
        x = x + p

    print("Достигнуто максимальное число итераций.")
    return x

# Начальное приближение
x0 = -1.0

# Ищем локальный минимум
res = Newton(f, gradient_f, hessian_f, x0)
print(f"Локальный минимум находится в точке: {res:.2f}")
print(f"Значение функции: {f(res):.2f}")


#Посторим График
x_vals = np.linspace(-2, 1, 500)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label = "Функция", linestyle='-', color='black')
plt.title("График функции")
plt.xlabel('x')
plt.ylabel('y')
plt.grid = True
plt.legend()
plt.show()