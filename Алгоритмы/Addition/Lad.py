import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def Montekarlo(image_path, num_samples=5):
    # Загружаем изображение
    img = cv2.imread(image_path)
    if img is None:
        print("Ошибка: изображение не загружено. Проверьте путь к файлу.")
        return None, None

    # Преобразование в бинарное изображение
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Получаем размеры изображения
    height, width = binary.shape
    total_area = 856440  # Общая площадь региона в квадратных километрах

    # Переменные для расчета среднего значения и дисперсии
    sea_areas = []
    sea_areas_squared = []
    sea_points = 0
    sample_points = []

    print("Итерация\tСредняя площадь (км²)\tПогрешность (км²)")

    for i in range(1, num_samples + 1):
        # Случайная точка
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        sample_points.append((x, y, binary[y, x] == 255))
        if binary[y, x] == 255:
            sea_points += 1

        # На каждом шаге обновляем расчет площади
        sea_ratio = sea_points / i
        estimated_sea_area = sea_ratio * total_area
        sea_areas.append(estimated_sea_area)
        sea_areas_squared.append(estimated_sea_area ** 2)

        # Среднее и погрешность
        mean_area = np.mean(sea_areas)
        mean_squared_area = np.mean(sea_areas_squared)
        error = np.sqrt(mean_squared_area - mean_area ** 2)

        # Вывод на каждой итерации
        print(f"{i}\t{mean_area:.2f}\t{error:.2f}")

    return sea_areas, sea_areas_squared, (img, sample_points)

# Путь к изображению
image_path = "D:\\Algorithm\\algorihtm\\Addition\\black sea.jpg"
areas, errors, result = Montekarlo(image_path, num_samples=1000)

if areas is not None:
    # Выводим последнюю площадь и погрешность
    print(f'Окончательная оценочная площадь Чёрного моря: {areas[-1]:.2f} км²')
    print(f'Окончательная погрешность: {np.sqrt(np.mean(errors) - np.mean(areas)**2):.2f} км²')

    # Визуализация точек
    img, sample_points = result
    plt.figure(figsize=(10, 8))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    sea_x = [x for x, y, is_sea in sample_points if is_sea]
    sea_y = [y for x, y, is_sea in sample_points if is_sea]
    land_x = [x for x, y, is_sea in sample_points if not is_sea]
    land_y = [y for x, y, is_sea in sample_points if not is_sea]

    plt.scatter(sea_x, sea_y, color='blue', s=1, label="Черное море")
    plt.scatter(land_x, land_y, color='red', s=1, label="Суша")

    plt.xlabel('X координата')
    plt.ylabel('Y координата')
    plt.title('Метод Монте-Карло: Черное море')
    plt.legend()
    plt.show()

    # Визуализация средней площади и погрешности
    iterations = np.arange(1, len(areas) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, areas, label='Средняя площадь (км²)')
    plt.xlabel('Количество повторений')
    plt.ylabel('Площадь (км²)')
    plt.title('Сходимость оценки площади Чёрного моря')
    plt.legend()
    plt.show()