import pulp
from pulp import LpProblem, LpMaximize, LpVariable, LpInteger

#Данные задачи
prob = LpProblem("Жилищный вопрос: ", pulp.LpMinimize)

#Переменная для количества домов
x1 = LpVariable("x1", lowBound=0, cat="Integer")
x2 = LpVariable("x2", lowBound=0, cat="Integer")
x3 = LpVariable("x3", lowBound=0, cat="Integer")
x4 = LpVariable("x4", lowBound=0, cat="Integer")

#Целевая функция
prob += 8300*x1 + 9500*x2 + 4200*x3 +3900*x4

#Ограничения
prob += 14*x1 + 20*x2 +22*x3 + 13*x4 >= 1800
prob += 42*x2 + 18*x3 + 19*x4 >= 1300
prob += 24*x1 + 55*x3 >=2300
prob += 68*x1 +10*x4 >= 5000

#Задача решается с помощью Lp решателя
prob.solve()

#Вывод результата
print("Оптимальное количество домов: ")
print(f"x1 (Д1) = {x1.varValue:.1f}")
print(f"x2 (Д2) = {x2.varValue:.1f}")
print(f"x3 (Д3) = {x3.varValue:.1f}")
print(f"x4 (Д4) = {x4.varValue:.1f}")
print(f"Минимальная себестоимость: {pulp.value(prob.objective):,.2f} тыс руб")