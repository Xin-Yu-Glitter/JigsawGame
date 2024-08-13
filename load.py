from PIL import Image, ImageTk


# 调用时传入Image
def cut_img_forLoadNewImage(img_pil):
    num_cols_rows = 3
    img_pil = img_pil.resize((450, 450), Image.BICUBIC)  # 不用管这个warning
    # 转换为Pillow Image

    # 计算每个块的大小
    width, height = img_pil.size[1] // num_cols_rows, img_pil.size[0] // num_cols_rows

    # 切割图片
    pieces = []

    for i in range(num_cols_rows):
        for j in range(num_cols_rows):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            piece = img_pil.crop(box)
            pieces.append(piece)

    # 打乱图片块
    # random.shuffle(pieces)
    return pieces
