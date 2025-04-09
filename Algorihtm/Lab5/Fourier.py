import numpy as np
import matplotlib.pyplot as plt

# Метод Симпсона
def Simpson(f, a, b, n=1000):
    """Только четное количество отрезков"""
    #Проверка на точность
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    #Формула Симпсона
    S = y[0] + y[-1] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:-2:2])

    return (h / 3) * S

# Моя Функция
def f(x):
    return np.abs(np.cos(3 * x))


# коефициенты
a = -np.pi
b = np.pi
T = b - a
M = 10

a0 = (1 / np.pi) * Simpson(f, a, b)
ak = []
bk = []

#Посчитаем коефициенты
for k in range(1, M + 1):
    ak_f = lambda x: f(x) * np.cos(k * x)
    bk_f = lambda x: f(x) * np.sin(k * x)
    ak_val = (1 / np.pi) * Simpson(ak_f, a, b)
    bk_val = (1 / np.pi) * Simpson(bk_f, a, b)
    ak.append(ak_val)
    bk.append(bk_val)

#Разложение в ряд Фурье
def Furier(x):
    result = (a0 / 2)
    for k in range(1, M + 1):
        result += ak[k - 1] * np.cos(k * x) + bk[k - 1] * np.sin(k * x)
    return result

x_vals = np.linspace(a, b, 1000)
f_original = f(x_vals)
f_approximation = [Furier(x) for x in x_vals]

#Строим график
plt.plot(x_vals, f_original, label="Исходная функция", linestyle='-', color='red')
plt.plot(x_vals, f_approximation, label=f"Ряд Фурье (M={M})", linestyle='--', color='black')
plt.title("Апроксимация рядом Фурье")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

