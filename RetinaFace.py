# https://github.com/serengil/retinaface

import cv2
import matplotlib.pyplot as plt
from retinaface import RetinaFace

# 원본 이미지 로드
img_path = './img/graduate.jpg'
img = cv2.imread(img_path)

retina_img = RetinaFace.detect_faces(img_path)

print(retina_img)
for i in retina_img.keys():
    face_info = retina_img[i]
    facial_area = face_info['facial_area']
    x1, y1, x2, y2 = facial_area

    # 사각형으로 얼굴 표시
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)

    # # print(eyes)
    # for ex, ey, ew, eh in facial_area:
    #     # 타원
    #     cv2.ellipse(img, (int((ex + x1)*2 + ew / 2) - (ex + x1), int((ey + y1)*2 + eh / 2) - (ey + y1)), (20,10), 0, 0, 360, (0,255,0), 2)

# for face in faces:
#   plt.imshow(face)
#   plt.show()

cv2.imshow('gray', img)
cv2.waitKey()
cv2.destroyAllWindows()