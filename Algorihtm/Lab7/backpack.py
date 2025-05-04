# Словарь с предметами
stuffdict = {
    'палатка': (5, 60),
    'спальный мешок': (2, 40),
    'котелок': (2, 30),
    'фонарик': (1, 50), 
    'аптечка': (4, 50),
    'верёвка': (2, 35)
}


items = list(stuffdict.items())
n = len(items)
max_weight = 10
best_value = 0
best_solution = []

# Рекурсивная функция ветвей и границ
def branch_bounds(index, current_weight, current_value, solution):
    global best_value, best_solution

    if current_weight > max_weight:
        return
    if index == n:
        if current_value > best_value:
            best_value = current_value  
            best_solution = solution[:]
        return

    # Рассчёт верхней границы 
    remaining_items = items[index:]
    remaining_sorted = sorted(remaining_items, key=lambda x: x[1][1] / x[1][0], reverse=True)
    weight_left = max_weight - current_weight
    upper_bound = current_value

    for name, (weight, value) in remaining_sorted:
        if weight <= weight_left:
            upper_bound += value
            weight_left -= weight
        else:
            upper_bound += value * (weight_left / weight)
            break

    if upper_bound < best_value:
        return

    # Ветвь 1 (взять предмет)
    solution.append(1)
    name, (weight, value) = items[index]
    branch_bounds(index + 1, current_weight + weight, current_value + value, solution)
    solution.pop()

    # Ветвь 2(не брать предмет)
    solution.append(0)
    branch_bounds(index + 1, current_weight, current_value, solution)
    solution.pop()

# Запуск 
branch_bounds(0, 0, 0, [])

# Вывод информации
print("Решение:")
total_weight = 0
for i in range(n):
    if best_solution[i] == 1:
        name, (weight, value) = items[i]
        print(f"Возьмём: {name} (вес {weight}, ценность {value})")
        total_weight += weight

print(f"Общий вес: {total_weight}")
print(f"Ценность: {best_value}")
