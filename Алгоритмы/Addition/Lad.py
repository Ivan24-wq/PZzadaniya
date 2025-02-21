import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def Montekarlo(image_path, num_samples=100000):
    # Загружаем изображение
    img = cv2.imread(image_path)
    if img is None:
        print("Ошибка: изображение не загружено. Проверьте путь к файлу.")
        return None, None
    
    #Точки
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    
    # Получаем размеры изображения
    height, width = binary.shape
    total_area = 856440  
    
    # Генерируем случайные точки и считаем, сколько попало в море (белый цвет)
    sea_points = 0
    sample_points = []
    for _ in range(num_samples):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        sample_points.append((x, y, binary[y, x] == 255))
        if binary[y, x] == 255:
            sea_points += 1
    
    # Вычисляем долю точек, попавших в море
    sea_ratio = sea_points / num_samples
    estimated_sea_area = sea_ratio * total_area
    
    return estimated_sea_area, (img, sample_points)


image_path = "D:\\Algorithm\\algorihtm\Addition\\black sea.jpg"
sea_area, result = Montekarlo(image_path)
if sea_area is not None:
    print(f'Оценочная площадь Чёрного моря: {sea_area:.2f} км²')

    # Визуализация
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