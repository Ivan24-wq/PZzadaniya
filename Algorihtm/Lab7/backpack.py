# Словарь с предметами
stuffdict = {
    'sofa': (5, 600),
    'desktop': (3, 1000),
    'netbook': (0.5, 1100),
    'fridge': (1, 800),
    'desk': (2, 30),
    'bike': (2, 100),
    'chears': (2, 100)
}

# Извлекаем данные
names = list(stuffdict.keys())
size = [stuffdict[name][0] for name in names]
value = [stuffdict[name][1] for name in names]
max_size = 20

size = [int(s * 2) for s in size]  
max_size_scaled = max_size * 2  

# Алгоритм рюкзака
def knapsack(size, value, max_size):
    n = len(size)
    dp = [[0] * (max_size + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for s in range(1, max_size + 1):
            if size[i-1] <= s:
                dp[i][s] = max(dp[i-1][s], dp[i-1][s - size[i-1]] + value[i-1])
            else:
                dp[i][s] = dp[i-1][s]
    
    # Восстановление предметов
    selected = []
    s = max_size
    for i in range(n, 0, -1):
        if dp[i][s] != dp[i-1][s]:
            selected.append(i-1)
            s -= size[i-1]
    
    return dp[n][max_size], selected

# Решение задачи
max_value, items = knapsack(size, value, max_size_scaled)

# Вывод результатов 
print(f"Максимальная ценность: {max_value} $")
print("Выбранные предметы:")
total_size = 0
for i in items:
    name = names[i]
    item_size = size[i] / 2  
    item_value = value[i]
    total_size += item_size
    print(f"  - {name}: {item_size} м², {item_value} $")

print(f"Общая площадь: {total_size} м²")
