import numpy as np
import matplotlib.pyplot as plt

# Рекурсивная реализация БПФ
def fft(x):
    N = len(x)
    if N == 1:
        return x
    if(N & (N - 1)) != 0:
        raise ValueError("Длина массива {N} должна быть степенью двойки")
    even = fft(x[::2])
    odd = fft(x[1::2])
    W = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    X = [even[k] + W[k] for k in range(N // 2)] + \
        [even[k] - W[k] for k in range(N // 2)]
    return X

# Генерация сигнала
N = 32
x = np.linspace(0, 2 * np.pi, N, endpoint=False)
y = np.sin(x**3)

# Применим БПФ
Y = fft(y)
amplitude = np.abs(Y)

# Построим графики
plt.figure(figsize=(12, 5))

# Сигнал
plt.subplot(1, 2, 1)
plt.plot(x, y, color='red', label="БПФ: sin(x³)")
plt.title("Быстрый Фурье")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()


# Амплитуда
plt.subplot(1, 2, 2)
plt.stem(range(N), amplitude)  
plt.title("Амплитудный спектр ")
plt.xlabel("Частотный индекс k")
plt.ylabel("Амплитуда")
plt.grid(True)

plt.tight_layout()
plt.show()
