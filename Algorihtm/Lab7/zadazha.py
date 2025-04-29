from pulp import LpProblem, LpMaximize, LpVariable, value
from fractions import Fraction

def zadacha(branch=None):
  
    prob = LpProblem("Метод Ветвей и Границ", LpMaximize)

    # Определяем переменные
    x1 = LpVariable("x1", lowBound=0, cat="Integer")
    x2 = LpVariable("x2", lowBound=0, cat="Integer")

    # Целевая функция
    prob += 2 * x1 + 3 * x2

    # Ограничения
    prob += 2 * x1 + x2 <= Fraction(19, 3)
    prob += x1 + 3 * x2 <= 10

    # Учитываем ветвление 
    if branch:
        for constraint in branch:
            prob += constraint

    # Решаем задачу
    status = prob.solve()

    # Если решения нет
    if status != 1:
        return None, None

    
    return {
        "x1": value(x1),
        "x2": value(x2),
        "F": value(prob.objective),
    }, prob

# Реализация метода ветвей и границ
def branch_and_bounds():
    best_solution = None  
    best_F = float("-inf")  
    stack = []  # Стек для хранения веток задачи

    # Находим начальное решение
    initial_solution, _ = zadacha()
    if not initial_solution:
        print("Нет решений!")
        return None
    stack.append(([], initial_solution))

    
    while stack:
        branch_constraints, solution = stack.pop()
        x1, x2 = solution["x1"], solution["x2"]

        # Провекра на целочисленность
        if x1.is_integer() and x2.is_integer():
            if solution["F"] > best_F:
                best_F = solution["F"]
                best_solution = solution
            continue


        if not x1.is_integer():
            lower = int(x1)
            upper = lower + 1
            stack.append((branch_constraints + [x1 <= lower], zadacha(branch_constraints + [x1 <= lower])[0]))
            stack.append((branch_constraints + [x1 >= upper], zadacha(branch_constraints + [x1 >= upper])[0]))
        elif not x2.is_integer():
            lower = int(x2)
            upper = lower + 1
            stack.append((branch_constraints + [x2 <= lower], zadacha(branch_constraints + [x2 <= lower])[0]))
            stack.append((branch_constraints + [x2 >= upper], zadacha(branch_constraints + [x2 >= upper])[0]))

    return best_solution

# Вывод 
result = branch_and_bounds()
if result:
    print("Ответ:")
    print(f"x1 = {result['x1']}, x2 = {result['x2']}, F = {result['F']}")
else:
    print("Нет решений!")
