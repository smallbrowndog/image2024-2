# Retina Face 활용 얼굴인식
# Haar과 비교

# https://github.com/serengil/retinaface

import cv2
import matplotlib.pyplot as plt
from retinaface import RetinaFace
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 원본 이미지 로드
img_path = './img/graduate.jpg'
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

        cv2.putText(img, f"SCORE: {retina_img[face]['score']:.7f}", (x1, y1), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0))

    # 폰트 설정 (원하는 경로에 있는 TTF 폰트 파일을 사용)
    fontpath = "C:/dev/image2024-2/BMJUA_ttf.ttf"  # 원하는 한글 폰트 파일 경로 설정
    font = ImageFont.truetype(fontpath, 20)  # 폰트 크기 설정

    # OpenCV의 이미지 배열을 PIL 이미지로 변환
    img_pil = Image.fromarray(img)

    # Pillow의 ImageDraw 사용
    draw = ImageDraw.Draw(img_pil)

    # 한글 텍스트
    draw.text((1000, 515), "김기주", font=font, fill=(255, 255, 0))

    # 다시 OpenCV 형식으로 변환
    img = np.array(img_pil)

    cv2.imwrite('./score.png', img)

    cv2.imshow('gray', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# for face in faces:
#   plt.imshow(face)
#   plt.show()
