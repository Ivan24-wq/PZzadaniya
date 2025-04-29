import pulp
from pult import LpProblem, LpMaximize, LpVariable, LpInteger
from fractions import Fraction

prob = LpProblem("Метод Ветвей и границ: ", pulp.LpMaximize)

x1 = LpVariable("x1", lowBound=0, cat="Integer")
x2=LpVariable("x2", lowBound=0, cat="Integer")

#Целевая функция
prob += 2 * x1 + 3 * x2

#Ограничения
prob += 2 * x1 + x2 <=Fraction(19, 3)
prob += x1 + 3 * x2 <= 10