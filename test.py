import cv2
import numpy as np
from PIL import Image
import random

num_cols_rows = 3


def load_img():
    image_path = "3.jpg"
    img = cv2.imread(image_path)
    # 转换为Pillow Image
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # 计算每个块的大小
    width, height = img.shape[1] // num_cols_rows, img.shape[0] // num_cols_rows

    # 切割图片
    pieces = []
    for i in range(num_cols_rows):
        for j in range(num_cols_rows):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            piece = img_pil.crop(box)
            pieces.append(piece)

    # 打乱图片块
    random.shuffle(pieces)
    return pieces

piece = load_img()
print(piece)
