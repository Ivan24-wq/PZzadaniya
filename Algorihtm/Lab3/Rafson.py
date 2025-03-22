import numpy as np
import time

def NewtonRafson(F, J, X0, tol=1e-6, max_iteration=1000):
    X = X0
    for i in range(max_iteration):
        F_value = F(X)
        J_value = J(X)  # Матрица Якоби
        delta_X = np.linalg.solve(J_value, -F_value)

        X = X + delta_X

        # Проверка условия 
        if np.linalg.norm(delta_X, ord=np.inf) < tol:
            return X
    raise ValueError("Недостаточно количества итераций")


def F(X):
    x, y = X
    return np.array([
        np.sin(x + 0.5) - y - 1,
        np.cos(y - 2) + x
    ])

# Определяем матрицу Якоби
def J(X):
    x, y = X  
    return np.array([
        [np.cos(x + 0.5), -1],
        [1, -np.sin(y - 2)]
    ])

# Начальное приближение
X0 = np.array([0.0, 0.0])

# Решение
start_time = time.time()
try:
    solution = NewtonRafson(F, J, X0)
    end_time = time.time()
    print("Ответ: ", solution)
    print(f"Время затраченное на выполнения алгоритма: {end_time - start_time:.4f} с")
except ValueError as e:
    print(e)