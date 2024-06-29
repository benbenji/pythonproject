# 人脸特征提取

import cv2
import dlib
import numpy as np

# 读取图片
img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸检测器
detector = dlib.get_frontal_face_detector()
dets = detector(gray, 1)

# 人脸特征点检测器
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

for face in dets:
    shape = predictor(img, face)
    for pt in shape.parts():
        pt_pos = (pt.x, pt.y)
        cv2.circle(img, pt_pos, 2, (0, 255, 0), 1)

cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()