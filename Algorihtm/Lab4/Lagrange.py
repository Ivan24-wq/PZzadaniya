import numpy as np
from sympy import symbols, simplify, lambdify
import cv2

#Задаю значения
x_val = [1, 2, 3, 4 ,5]
y_val = [8.2, 5.9, 4.9, 4, 3.2]

#Находим базсный поллином
def lagrange_basis(x_val, x, i):
    L_i = 1
    for j in range(len(x_val)):
        if j != i:
            L_i *= (x - x_val[j]) / (x_val[i] - x_val[j])
    return L_i
#Функция для нахождения полинома Лагрнжа
def langrange(x_val, y_val, x):
    P_x = 0
    for i in range(len(x_val)):
        L_i = lagrange_basis(x_val, x, i)
        P_x += y_val[i] * L_i
    #Упростим выражение
    return simplify(P_x)

#Определим x 
x = symbols('x')
#Вывод ответа
P_x = langrange(x_val, y_val, x)

print(f"Полином Лагранжа: P(x): ")
print(P_x)

# Преобразуем полином в лямбда-функцию для вычисления значений
P_x_func = lambdify(x, P_x, modules=['numpy'])

# Создаем координаты для графика
x_plot = np.linspace(min(x_val) - 1, max(x_val) + 1, 500)
y_plot = P_x_func(x_plot)
#Вывод координат
print("\n Координаты точек: ")
for x_cord, y_cord in zip(x_plot, y_plot):
    print(f"({x_cord:.2f}, {y_cord:.2f})")
# Параметры изображения
img_height, img_width = 500, 500
img = np.ones((img_height, img_width, 3), dtype=np.uint8) * 255

# Масштабируем координаты в границы изображения
x_img = ((x_plot - min(x_plot)) / (max(x_plot) - min(x_plot)) * (img_width - 50)).astype(np.int32) + 25
y_img = img_height - ((y_plot - min(y_plot)) / (max(y_plot) - min(y_plot)) * (img_height - 50)).astype(np.int32) - 25

# Рисуем оси
cv2.line(img, (25, img_height - 25), (img_width - 25, img_height - 25), (0, 0, 0), 2)
cv2.line(img, (25, img_height - 25), (25, 25), (0, 0, 0), 2)

# Рисуем полином
for i in range(len(x_img) - 1):
    cv2.line(img, (x_img[i], y_img[i]), (x_img[i + 1], y_img[i + 1]), (255, 0, 0), 2)

# Рисуем исходные точки
for x_point, y_point in zip(x_val, y_val):
    x_p = int((x_point - min(x_plot)) / (max(x_plot) - min(x_plot)) * (img_width - 50)) + 25
    y_p = img_height - int((y_point - min(y_plot)) / (max(y_plot) - min(y_plot)) * (img_height - 50)) - 25
    cv2.circle(img, (x_p, y_p), 5, (0, 0, 255), -1)

# Показ изображения
cv2.imshow('Lagrange Polynomial', img)
cv2.waitKey(0)
cv2.destroyAllWindows()