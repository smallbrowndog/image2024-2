# 2024.10.28 이미지 분석 강의
# 대칭이동, resize, 회전

import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
height, width, _ = img.shape

m_flip = np.float32([[-1, 0, width],
                     [0, 1, 0]])


m_flipy = np.float32([[-1, 0, width],
                     [0, -1, height]])

dflip = cv2.warpAffine(img, m_flip, (height, width))
dflipy = cv2.warpAffine(img, m_flipy, (height, width))

dflip3 = np.zeros_like(img)
# 좌우 반전
for i in range(width):
    dflip3[:, i, :] = img[:, width-i-1, :]

dflip4 = np.zeros_like(img)
# 상하 반전
for i in range(height):
    dflip4[i, :, :] = img[height-i-1, :, :]

dflip5 = np.zeros_like(img)
# 상하좌우 반전
for i in range(height):
    dflip5[i, :, :] = dflip3[height-i-1, :, :]

cv2.imshow('img', img)
cv2.imshow('flip', dflip)
cv2.imshow('flipy', dflipy)
cv2.imshow('dflip3', dflip3)
cv2.imshow('dflip4', dflip4)
cv2.imshow('dflip5', dflip5)
cv2.waitKey()
cv2.destroyAllWindows()

# cv2 resize
# x 2배, y 0.5배
dst1 = cv2.resize(img, None, None, 2, 0.5, cv2.INTER_CUBIC)
# 임의로 크기 정하기
dst2 = cv2.resize(img, (200, 300), interpolation=cv2.INTER_AREA)

dst3 = cv2.resize(img, (int(width*0.5), int(height*2)), None, 0, 0, cv2.INTER_AREA)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey()
cv2.destroyAllWindows()