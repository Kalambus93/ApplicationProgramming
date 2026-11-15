import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_image(img: np.ndarray) -> None:
    """
    Показывает изображение через matplotlib
    :param img: изображение
    """
    plt.figure(figsize=(6, 6))

    if img.ndim == 2:
        plt.imshow(img, cmap="gray", vmin=0, vmax=255)
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    plt.axis("off")
    plt.show()


def download_image(path_image: str) -> np.ndarray:
    """
    Функция для загрузки изображения
    :param path_image: путь к исходному файлу
    :return: загруженный файл
    """

    img = cv2.imread(path_image)
    if img is None:
        raise FileNotFoundError(f"Не удалось загрузить: {path_image}")
    return img


def grayscale_image(img: np.ndarray) -> np.ndarray:
    """
    Функция преобразования в полутоновое изображение
    :param img: изображение
    :return: полутоновое изображение
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def circle_image(img: np.ndarray) -> np.ndarray:
    """
    Функция обрезки фото до круга
    :param img: полутоновое изображение
    :return: полутоновое изображение, вне круга — белый фон
    """
    height = img.shape[0]
    width = img.shape[1]

    mask = np.zeros((height, width), dtype=np.uint8)
    center = (width // 2, height // 2)
    radius = min(center[0], center[1])
    cv2.circle(mask, center, radius, 255, -1)

    result = img.copy()
    result[mask == 0] = 255
    return result


def gradient_image(img: np.ndarray) -> np.ndarray:
    """
    Накладывает горизонтальный градиент (чёрный слева → белый справа)
    на полутоновое изображение.
    :param img: полутоновое изображение
    :return: полутоновое изображение с градиентом
    """
    height = img.shape[0]
    width = img.shape[1]

    row = np.linspace(0, 255, width, dtype=np.uint8)
    grad = np.tile(row, (height, 1))

    result = cv2.multiply(img, grad, scale=1 / 255.0)

    return result
