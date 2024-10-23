import cv2
from cv2.data import haarcascades
import numpy as np
from PIL import ImageFont, ImageDraw, Image


face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')
img = cv2.imread('./img/family.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray)
# print(faces)
# x, y, w, h = faces[0]
# print(f'x={x}')
# cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 10)

# 교수님 최종 정리
for fx, fy, fw, fh in faces:
    # 사각형
    # cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 8)

    # 원
    # cv2.circle(img, (int(fx + fw / 2), int(fy + fh / 2)), (60), (255, 0, 0), 2)

    # 타원
    cv2.ellipse(img, (int(fx + fw / 2), int(fy + fh / 2)), (60,80), 0, 0, 360, (255,0,0), 2)


    eyes = eye_cascade.detectMultiScale(gray[fy:fy+fh, fx:fx+fw])
    # print(eyes)
    for ex, ey, ew, eh in eyes:
        # 사각형
        cv2.rectangle(img, (ex + fx, ey + fy), (ex + fx + ew, ey + fy + eh), (0, 255, 0), 2)

        # 원
        # cv2.circle(img, center, radian, color, thickness) 이런 방식으로 동작해야함
        # faces안에서 eyes가 동작하기 때문에 rectangle에서 x좌표에 2를 곱하고 높이를 2로 나눠서 중심좌표를 만들어주었다
        # cv2.circle(img, (int((ex + fx)*2 + ew / 2) - (ex + fx), int((ey + fy)*2 + eh / 2) - (ey + fy)), (20), (0, 255, 0), 2)

        # 타원
        # cv2.ellipse(img, (int((ex + fx)*2 + ew / 2) - (ex + fx), int((ey + fy)*2 + eh / 2) - (ey + fy)), (20,10), 0, 0, 360, (0,255,0), 2)

# 폰트 설정 (원하는 경로에 있는 TTF 폰트 파일을 사용)
fontpath = "./BMJUA_ttf.ttf"  # 원하는 한글 폰트 파일 경로 설정
font = ImageFont.truetype(fontpath, 20)  # 폰트 크기 설정

# OpenCV의 이미지 배열을 PIL 이미지로 변환
img_pil = Image.fromarray(img)

# Pillow의 ImageDraw 사용
draw = ImageDraw.Draw(img_pil)

# 한글 텍스트
draw.text((280, 600), "김기주 중간과제", font=font , fill=(0, 255, 255))

# 다시 OpenCV 형식으로 변환
img = np.array(img_pil)

cv2.imwrite('./Middle.png', img)

cv2.imshow('gray', img)
cv2.waitKey()
cv2.destroyAllWindows()