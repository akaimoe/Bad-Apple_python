import cv2
import numpy as np
import matplotlib.pyplot as plt

show_high = 20
show_wide = 70

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. ")

char_len = len(ascii_char)



def img_2_ascii(img_path,n):

    path = img_path + str(n) + '.jpg'
    img = cv2.imread(path)
    sp = img.shape
    img_high = sp[0]
    img_wide = sp[1]
    gray = 0.2126*img[:,:,2] + 0.7152*img[:,:,1] + 0.0722*img[:,:,0]

    for i in range(show_high):
        # 根据比例映射到对应的像素
        y = int(i * img_high / show_high)
        text = ""
        for j in range(show_wide):
            x = int(j * img_wide / show_wide)
            text += ascii_char[int(gray[y][x] / 256 * char_len)]
        print(text)


