import tkinter as tk
import cv2
import random
from PIL import Image, ImageTk
import numpy as np
import load
import imagehash
from tkinter import filedialog

aim_button = None
judge = False


def load_img():

    global piece
    global disruption_piece
    global disruption_piece_img

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        img = Image.open(file_path)
        print(img)
        piece = load.cut_img_forLoadNewImage(img)
        disruption_piece_img = piece.copy()
        random.shuffle(disruption_piece_img)
        disruption_piece = []
        for i in range(9):
            disruption_piece.append(ImageTk.PhotoImage(disruption_piece_img[i]))
        fresh_button()

def button1_click():
    global aim_button
    if aim_button is None:
        aim_button = 1
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=1)


def button2_click():
    global aim_button
    if aim_button is None:
        aim_button = 2
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=2)


def button3_click():
    global aim_button
    if aim_button is None:
        aim_button = 3
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=3)


def button4_click():
    global aim_button
    if aim_button is None:
        aim_button = 4
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=4)


def button5_click():
    global aim_button
    if aim_button is None:
        aim_button = 5
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=5)


def button6_click():
    global aim_button
    if aim_button is None:
        aim_button = 6
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=6)


def button7_click():
    global aim_button
    if aim_button is None:
        aim_button = 7
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=7)


def button8_click():
    global aim_button
    if aim_button is None:
        aim_button = 8
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=8)


def button9_click():
    global aim_button
    if aim_button is None:
        aim_button = 9
        button_cond.config(text="状态：已选中\n点击以取消选中")
    else:
        change_button(dest_button=9)


def change_button(dest_button):
    global aim_button
    aim_button = aim_button - 1
    dest_button = dest_button - 1

    # 交换用于显示的
    t = disruption_piece[dest_button]
    disruption_piece[dest_button] = disruption_piece[aim_button]
    disruption_piece[aim_button] = t

    # 交换用于对比的
    t = disruption_piece_img[dest_button]
    disruption_piece_img[dest_button] = disruption_piece_img[aim_button]
    disruption_piece_img[aim_button] = t

    button_cond.config(text="状态：未选中\n点击以取消选中")
    aim_button = None
    fresh_button()


def fresh_button():
    button_left_1.config(image=disruption_piece[0])
    button_left_2.config(image=disruption_piece[1])
    button_left_3.config(image=disruption_piece[2])
    button_left_4.config(image=disruption_piece[3])
    button_left_5.config(image=disruption_piece[4])
    button_left_6.config(image=disruption_piece[5])
    button_left_7.config(image=disruption_piece[6])
    button_left_8.config(image=disruption_piece[7])
    button_left_9.config(image=disruption_piece[8])


def judge_button():
    global judge
    judge = True
    for i in range(8):
        if imagehash.average_hash(disruption_piece_img[i]) != imagehash.average_hash(piece[i]):
            judge = False
            break

    judge_window = tk.Toplevel()
    judge_window.geometry('300x200')
    judge_window.title("判断")
    text_judge = tk.Text(judge_window, font=('Arial', 30))
    text_judge.place(x=30, y=50, width=240, height=100)
    if judge is True:
        text_judge.insert(tk.END, "ok")
    else:
        text_judge.insert(tk.END, "not ok")
    text_judge.config(state='disabled')


def cond_button():
    global aim_button
    aim_button = None
    button_cond.config(text="状态：未选中\n点击以取消选中")


num_cols_rows = 3  # 图片会被分为几x几  放这好看，不要动！！！！！！

window = tk.Tk()
window.title("拼图游戏")
window.geometry('700x550')  # 窗口大小

side_length = 450  # 拼图区域边长。是个正方形
unit_length = int(side_length / num_cols_rows)

button_load = tk.Button(window, text="加载图片", font=('Arial', 12), command=load_img)
button_load.place(x=550, y=100, anchor='nw', width=100, height=50)

button_judge = tk.Button(window, text="判断", font=('Arial', 12), command=judge_button)
button_judge.place(x=550, y=200, anchor='nw', width=100, height=50)

button_cond = tk.Button(window, text="状态：未选中\n点击以取消选中", font=('Arial', 10), command=cond_button)
button_cond.place(x=550, y=300, anchor='nw', width=100, height=100)

white_img = np.ones([unit_length, unit_length], dtype=np.uint8) * 255
white_img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(white_img, cv2.COLOR_BGR2RGB)))

# 默认显示的图片
piece = load.cut_img_forLoadNewImage(Image.open("3.jpg"))  # 这个存储没有打乱的Image对象，用于对比
disruption_piece_img = piece.copy()  # 这个存储Image对象，用于对比
random.shuffle(disruption_piece_img)
disruption_piece = []  # 这个存储了PhotoImage对象，用于显示
for i in range(9):
    disruption_piece.append(ImageTk.PhotoImage(disruption_piece_img[i]))

button_left_1 = tk.Button(window, image=white_img, command=button1_click)
button_left_2 = tk.Button(window, image=white_img, command=button2_click)
button_left_3 = tk.Button(window, image=white_img, command=button3_click)
button_left_4 = tk.Button(window, image=white_img, command=button4_click)
button_left_5 = tk.Button(window, image=white_img, command=button5_click)
button_left_6 = tk.Button(window, image=white_img, command=button6_click)
button_left_7 = tk.Button(window, image=white_img, command=button7_click)
button_left_8 = tk.Button(window, image=white_img, command=button8_click)
button_left_9 = tk.Button(window, image=white_img, command=button9_click)

fresh_button()  # 放置打乱后的图片

button_left_1.place(x=50+unit_length*0, y=50+unit_length*0, anchor='nw', width=unit_length, height=unit_length)
button_left_2.place(x=50+unit_length*1, y=50+unit_length*0, anchor='nw', width=unit_length, height=unit_length)
button_left_3.place(x=50+unit_length*2, y=50+unit_length*0, anchor='nw', width=unit_length, height=unit_length)
button_left_4.place(x=50+unit_length*0, y=50+unit_length*1, anchor='nw', width=unit_length, height=unit_length)
button_left_5.place(x=50+unit_length*1, y=50+unit_length*1, anchor='nw', width=unit_length, height=unit_length)
button_left_6.place(x=50+unit_length*2, y=50+unit_length*1, anchor='nw', width=unit_length, height=unit_length)
button_left_7.place(x=50+unit_length*0, y=50+unit_length*2, anchor='nw', width=unit_length, height=unit_length)
button_left_8.place(x=50+unit_length*1, y=50+unit_length*2, anchor='nw', width=unit_length, height=unit_length)
button_left_9.place(x=50+unit_length*2, y=50+unit_length*2, anchor='nw', width=unit_length, height=unit_length)

window.mainloop()


