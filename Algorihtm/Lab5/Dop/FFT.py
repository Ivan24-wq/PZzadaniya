import numpy as np
import matplotlib.pyplot as plt


"""Быстрое разложение Фурье
Создадим сигнал - сумма синусоидов"""
#Частота Дискредитации
Fs = 500
#Последнюю точку не учитываю в массив
k = np.linspace(0, 1, Fs, endpoint = False)
sign = 3 * np.sin(2 * np.pi * 60 * k) + 2 * np.sin(2 * np.pi * 120 * k) + np.sin(2 * np.pi * 200 * k)

#Реализазия БПФ
fft_res = np.fft.fft(sign)
freq = np.fft.fftfreq(len(k), 1 /Fs)

#Строим график
plt.figure(figsize=(10, 4 ))
plt.plot(freq[:Fs // 2], np.abs(fft_res)[:Fs // 2] * 2 / Fs)
plt.title("Спектр Сигнала")
plt.xlabel("Частота")
plt.ylabel("Амплитуда")
plt.grid()
plt.show()