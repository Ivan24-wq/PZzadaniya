import numpy as np
import matplotlib.pyplot as plt

# Рекурсивная реализация БПФ
def fft(x):
    N = len(x)
    if N == 1:
        return x
    if (N & (N - 1)) != 0:
        raise ValueError(f"Длина массива {N} должна быть степенью двойки")
    even = fft(x[::2])
    odd = fft(x[1::2])
    W = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    X = [even[k] + W[k] for k in range(N // 2)] + \
        [even[k] - W[k] for k in range(N // 2)]
    return X

# Генерация сигнала
N = 1024
x = np.linspace(-np.pi, np.pi, N, endpoint=False)
y = np.where((-np.pi / 2 <= x) & (x <= np.pi / 2), -1, 1)

# Применим БПФ
Y = fft(y)
amplitude = np.abs(Y)

# Вычисляем частотную ось
frequencies = np.fft.fftfreq(N, d=(2 * np.pi / N))

# Берём только положительные частоты
positive_freqs = frequencies[:N // 2]
positive_amplitude = amplitude[:N // 2]

# Построим график амплитуды спектра для положительных частот
plt.figure(figsize=(10, 5))

plt.plot(positive_freqs, positive_amplitude, color="blue", label="Амплитудный спектр")
plt.title("Амплитудный спектр сигнала (Положительные частоты)")
plt.xlabel("Частоты (рад/с)")
plt.ylabel("Амплитуда")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

