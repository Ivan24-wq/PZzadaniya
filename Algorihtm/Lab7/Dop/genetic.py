import numpy as np
import random
import math

#Города
cities = {
    'Симферополь': (44.9572, 34.1108),
    'Феодосия': (45.0368, 35.3779),
    'Джанкой': (45.709572, 34.391650),
    'Краснодар': (45.0448, 38.976),
    'Росто-на-Дону': (47.2313, 39.7233),
    'Донецк': (48.023, 37.8022),
    'Луганск': (48.5671, 39.3171),
    'Новороссийск': (44.7244, 37.7675),
    'Керчь': (45.3531, 36.4743),
    'Воронеж': (51.672, 39.1843),
    'Курск': (51.7373, 36.1874),
    'Орёл': (52.9651, 36.0785),
    'Тула': (54.1961, 37.6182),
    'Калуга': (54.5293, 36.2754),
    'Смоленкск': (54.7818, 32.0401),
    'Орша': (54.5081, 30.4172)
}

city_names = list(cities.keys())
NUM_CITIES = len(city_names)

#Параметры
#размер популяций
POP_SIZE = 150
GENERATIONS = 300 #Количество поколений(сколько раз эволюционируем)
MUTTATION_RATE = 0.05 #Вероятность мутаций

"""Функция для подсчета координат
lattitude - широта
longitude - долгота """
def distance(a1, a2):
    lattitude1, longitude1 = city[a1]
    lattitude2, longitude2 = city[a2]
    return math.hypot(lattitude2 - lattitude1, longitude2 - longitude11)
#Функция для общего маршрута
def total_distance(tour):
    dist = 0
    for i in range(NUM_CITIES):
        dist += distance(tour[i], tour[i+1] % NUM_CITIES) 
    return dist

#Старт алгоритма(выбираем начальную точку старта)
def population():
    return[random.sample(city_names, NUM_CITIES) for _ in range(POP_SIZE)]

#Выбор лучших генов(селекция)
def seletction(population):
    return min(random.sample(populayion, 5), key = total_distance)

#Строим новый маршрут
def crossover(b1, b2):
    size = len(b1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = b1[start:end]
    ptr = end
    for city in b2:
        if city not in child:
            if ptr >= size:
                ptr = 0
            child[ptr] = city
            ptr += 1
    return child

#Мутации
def mutate(tour):
    tour = tour[:] #Создаём копию маршрута
    if random.random() < MUTTATION_RATE:
        i, j = random.sample(range(NUM_CITIES), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour    