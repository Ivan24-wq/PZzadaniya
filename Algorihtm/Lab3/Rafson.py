import numpy as np

def NewtonRaphson(F, J, X0, tol=1e-6, max_iteration=1000):
    X = X0
    for _ in range(max_iteration):
        F_value = F(X)
        J_value = J(X)

        if np.linalg.det(J_value) == 0:
            raise ValueError("Матрица Якоби вырожденная, невозможно решить систему.")

        delta_X = np.linalg.solve(J_value, -F_value)
        X = X + delta_X
        # Проверка, что изменение решения достаточно маленькое (проверка сходимости)
        
        if np.linalg.norm(delta_X, ord=np.inf) < tol:
            return X

    raise ValueError("Метод Ньютона-Рафсона не сошелся за заданное число итераций.")

def F(X):
    x, y = X
    return np.array([
        np.sin(x + 0.5) - y - 1,
        np.cos(y - 2) + x
    ])

def J(X):
    x, y = X
    return np.array([
        [np.cos(x + 0.5), -1],
        [1, -np.sin(y - 2)]
    ])

# Начальное приближение
X0 = np.array([0.0, 0.0])

# Решение системы
try:
    solution = NewtonRaphson(F, J, X0)
    print("\nОтвет:", solution)

    # Проверка результата
    F_solution = F(solution)
    print("\nПроверка решения:")
    print("F(X):", F_solution)
    if np.allclose(F_solution, 0, atol=1e-6):
        print("Решение корректно, значения функций близки к нулю.")
    else:
        print("Решение некорректно, значения функций не равны нулю.")
except ValueError as e:
    print("\nОшибка:", e)