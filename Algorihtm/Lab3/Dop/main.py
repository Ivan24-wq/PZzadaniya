import numpy as np

def NewtonRafson(F, J, X0, tol=1e-6, max_iteration=1000):
    X = X0
    for i in range(max_iteration):
        F_value = F(X)
        J_value = J(X)
        
        try:
            delta_X = np.linalg.solve(J_value, -F_value)
        except np.linalg.LinAlgError:
            raise ValueError("Матрица Якоби не обратима.")
        
        X = X + delta_X

        # Проверяем условие сходимости
        if np.linalg.norm(delta_X, ord=np.inf) < tol:
            return X
    
    raise ValueError("Метод Ньютона-Рафсона не сошелся за заданное количество итераций.")

# Наша СНАУ
def F(X):
    a, b, h, x, y, z = X
    return np.array([
        x**2 + y**2 - h - 1,
        np.exp(y**2) - x**4 + z - 5,
        np.sin(x) + 2 * b, 
        x * a - y * b - 6, 
        np.log(1 + z**2) - h * a + 1,
        x**2 + b**3 - z - 4
    ])

# Матрица Якоби (частные производные)
def J(X):
    a, b, h, x, y, z = X
    epsilon = 1e-8  # Для избежания деления на ноль
    return np.array([
        [2 * x, 2 * y, -1, 0, 0, 0],
        [-4 * x**3, 2 * y * np.exp(y**2), 0, 0, 0, 1],
        [np.cos(x), 2, 0, 0, 0, 0],
        [a, -b, 0, x, -y, 0],
        [0, 0, -a, 0, 0, (2 * z / (x**2 + epsilon)) + 1],  # Исправлено
        [2 * x, 3 * b**2, 0, 0, 0, -1]
    ])

# Начальное приближение
X0 = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])  # Установлено ненулевое начальное значение

try:
    solution = NewtonRafson(F, J, X0)
    print("Ответ: ", solution)
except ValueError as e:
    print(e)
