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
    return np.cos(x)


# коефициенты
a = -np.pi
b = np.pi
T = b - a
M = 6

a0 = 2 / T * Simpson(f, a, b)
ak = []
bk = []

#Посчитаем коефициенты
for k in range(1, M + 1):
    ak_f = lambda x: f(x) * np.cos(k * np.pi * x / (T / 2))
    bk_f = lambda x: f(x) * np.sin(k * np.pi * x / (T / 2))
    ak_val = (1 / T) * Simpson(ak_f, a, b)
    bk_val = (1 / T) * Simpson(bk_f, a, b)
    ak.append(ak_val)
    bk.append(bk_val)
#Разложение в ряд Фурье
def Furier(x):
    result = a0 / 2
    for k in range(1, M + 1):
        result += ak[k - 1] * np.cos(k * np.pi * x / (T / 2)) + bk[k - 1] * np.sin(k * np.pi * x / (T / 2))
    return result

x_vals = np.linspace(a, b, 1000)
f_original = f(x_vals)
f_approximation = [Furier(x) for x in x_vals]

#Строим график
plt.plot(x_vals, f_original, label="Исходная функция", linestyle='-')
plt.plot(x_vals, f_approximation, label=f"Ряд Фурье (M={M})", linestyle='--')
plt.title("Интерполяция рядом Фурье")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

