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
        x**2 + y**2 +z**2 -3,
        x * y * z -1,
        h - x - y,
        a - y - z,
        b - z- x,
        h + a + b - 6
    ])

# Матрица Якоби (частные производные)
def J(X):
    a, b, h, x, y, z = X
    return np.array([
        [2 * x, 2 * y, 2 *z, 0, 0, 0],
        [y * z, x * z, x * y, 0, 0, 0],
        [-1, -1, 0, 1, 0, 0],
        [0, -1, -1, 0, 1, 0],
        [-1, 0, -1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1]
    ])

# Начальное приближение
X0 = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])  

try:
    solution = NewtonRafson(F, J, X0)
    print("Ответ: ", solution)
except ValueError as e:
    print(e)
