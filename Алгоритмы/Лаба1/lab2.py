import numpy as np
import time

# Функция
def f(x):
    return 1 / (0.01 + np.abs(x))

# Метод Монте-Карло
def MonteKarlo(a, b, n_samples):
    x = np.random.uniform(a, b, n_samples)
    return (b - a) * np.mean(f(x))

# Параметры
a, b = -1, 1  
n_samples = 100000
n_repeats = 25


print(f"Используется {n_samples} точек, количество повторений: {n_repeats}")


total_time = 0
results = []

# Повторяем вычисления несколько раз
for i in range(n_repeats):
    start_time = time.time()  
    result_direct = MonteKarlo(a, b, n_samples)  
    end_time = time.time()  
    
    execution_time = end_time - start_time  
    total_time += execution_time  
    
    
    results.append(float(result_direct))

# Среднее время выполнения
average_time = total_time / n_repeats


average_result = np.mean(results)


std_deviation = np.std(results)

error = std_deviation / np.sqrt(n_repeats)


formatted_results = [f"{r:.4f}" for r in results]


print(f"Результаты (повторения): {', '.join(formatted_results)}")
print(f"Среднее значение интеграла: {average_result:.4f}")
print(f"Погрешность: {error:.4f}")
print(f"Среднее время выполнения: {average_time:.5f} секунд")