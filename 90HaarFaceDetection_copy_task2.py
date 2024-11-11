# Retina Face 활용 얼굴인식
# Haar과 비교

# https://github.com/serengil/retinaface

import cv2
import matplotlib.pyplot as plt
from retinaface import RetinaFace

# 원본 이미지 로드
img_path = './img/man_face.jpg'
img = cv2.imread(img_path)

retina_img = RetinaFace.detect_faces(img_path)

print(retina_img)

if retina_img == {}:
    print("얼굴이 인식되지 않았습니다")
else:
    for face in retina_img.keys():
        facial_area = retina_img[face]['facial_area']
        x1, y1, x2, y2 = facial_area

        # 사각형으로 얼굴 표시
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)

    cv2.imshow('gray', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# for face in faces:
#   plt.imshow(face)
#   plt.show()
