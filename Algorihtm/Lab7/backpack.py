from pulp import LpProblem, LpMaximize, LpVariable, LpInteger, lpSum, value, LpBinary
# Словарь с предметами
stuffdict = {
    'палатка': (5, 60),
    'спальный мешок': (2, 40),
    'котелок': (2, 30),
    'фонарик': (1, 50), 
    'аптечка': (4, 50),
    'верёвка': (2, 35)
}

def zadacha():
    prob = LpProblem("Рюкзак туриста", LpMaximize)

    #Список название предметов
    items = list(stuffdict.keys())

    #Бинарные переменные
    item_vars = {name: LpVariable(name, cat=LpBinary) for name in items}
    #Целевая функция
    prob += lpSum(stuffdict[name][1] * item_vars[name] for name in items)
    prob += lpSum(stuffdict[name][0] * item_vars[name] for name in items) <= 10

    #решаем задачу
    prob.solve()

    #Вывод
    print("Решение: ")
    total_weight = 0
    for name in items:
        if item_vars[name].value() == 1:
            weight, value_item = stuffdict[name]
            print(f"Взять: {name}(вес {weight}, ценность: {value_item})")
            total_weight += weight
    print(f"общий вес: {total_weight}")
    print(f"общая ценность: {value(prob.objective)}")

zadacha()