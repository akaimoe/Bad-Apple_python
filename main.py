import cv2
import os
import numpy
import vid2img
import img2askii


vid_path = "D:\\nn\\video\\bad apple.mp4"
save_path = "D:\\nn\py\\bad apple\\img\\"
#vid2img.vid_2_img(vid_path,save_path)
for i in range(1,6574):
    print(i)
    img2askii.img_2_ascii(save_path,i)
