import numpy as np
import matplotlib.pyplot as plt

#Рекурсивная реализация БПФ
def fft(x):
    N = len(x) #Входные данные
    if N == 1:
        return x

    #используем разделение ДПФ
    even = fft(x[::2]) #Четные
    odd = fft(x[1::2]) #Нечетные

    #Поворачивающий множитель
    W = [np.exp(-2j * 2 * np.pi * k / N) * odd[k] for k in range(N // 2)]

    #Комбинирование результатов
    X = [even[k] + W[k] for k in range(N // 2)] + \
        [even[k] - W[k] for k in range(N // 2)]
    return X 

#Моя функция
N = 6
x = np.linspace(0, 2 * np.pi, N, endpoint=False)
y = np.sin(x**2)


#Постором график
plt.plot(x, y, label="Быстрое преобразование Фурье", linestyle='-', color='red')
plt.title("БПФ")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()