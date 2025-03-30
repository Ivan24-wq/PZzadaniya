import numpy as np
from scipy.interpolate import CubicSpline

#Функция для интерполяции
interpolation_function = 'np.cos(x)'

#Входные данные
x = np.array = ([1.00, 1.04, 1.08, 1.12, 1.16,
                 1.20])
y = np.array = ([0.5403, 0.5062, 0.4713, 0.4357, 0.3963,
                 0.3624])

#Создаём кубический сплайн(встроенная бтблтотека)
cs = CubicSpline(x, y, bc_type = 'natural')

#Точки в которых нужно найти значение сплайна
points = [1.05, 1.09, 1.13, 1.15, 1.17]

#Счимаем сплайн в указанный точках
spline_value = cs(points)
