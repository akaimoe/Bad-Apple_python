import cv2
import os



def vid_2_img(vid_path,save_path):
    cap = cv2.VideoCapture(vid_path)

    if os.path.exists(save_path):
        pass
    else:
        os.makedirs(save_path)
    i = 0
    pd, img = cap.read()
    while pd:
        i = i + 1

        path = save_path + str(i) + '.jpg'
        cv2.imwrite(path,img)
        print(str(i))
        pd, img = cap.read()

