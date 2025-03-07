import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def MonteCarlo(image_path, num_samples=100000, num_trials=10):
    # Загружаем изображение
    img = cv2.imread(image_path)
    if img is None:
        print("Ошибка: изображение не загружено. Проверьте путь к файлу.")
        return None

    # Преобразуем изображение в бинарное (чёрное и белое)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Получаем размеры изображения
    height, width = binary.shape
    total_area = 856440  #

    
    areas = []
    all_points = []  

    for trial in range(num_trials):
        sea_points = 0
        trial_points = []  

        # Генерируем случайные точки и подсчитываем попадания в море (белый цвет)
        for _ in range(num_samples):
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            is_sea = binary[y, x] == 255
            trial_points.append((x, y, is_sea))
            if is_sea:
                sea_points += 1

        
        sea_ratio = sea_points / num_samples
        estimated_sea_area = sea_ratio * total_area

        
        areas.append(estimated_sea_area)
        all_points.extend(trial_points)  
        print(f"Повторение {trial + 1}:  Площадь  Чёрного моря = {estimated_sea_area:.2f} км²")

    # Вычисляем среднее значение и стандартное отклонение
    mean_area = np.mean(areas)
    std_dev = np.sqrt(np.mean(np.square(areas)) - np.square(mean_area))

    print(f"\nОкончатель площади Чёрного моря: {mean_area:.2f} км² ± {std_dev:.2f} км²")

    return mean_area, std_dev, img, binary, all_points

# Путь к изображению
image_path = r'C:\Users\User\Desktop\Algorihtm\black sea.jpg'


mean_area, std_dev, img, binary, all_points = MonteCarlo(image_path, num_samples=1000000, num_trials=6)

# Визуализация
if img is not None:
    plt.figure(figsize=(10, 8))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Разделяем точки на море и сушу
    sea_x = [x for x, y, is_sea in all_points if is_sea]
    sea_y = [y for x, y, is_sea in all_points if is_sea]
    land_x = [x for x, y, is_sea in all_points if not is_sea]
    land_y = [y for x, y, is_sea in all_points if not is_sea]

  
    plt.scatter(sea_x, sea_y, color='blue', s=1, label="Море")
    plt.scatter(land_x, land_y, color='red', s=1, label="Суша")

    plt.title("Метод Монте-Карло: Оценка площади Чёрного моря")
    plt.legend()
    plt.axis("off")
    plt.show()