import numpy as np
from sympy import symbols, simplify

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