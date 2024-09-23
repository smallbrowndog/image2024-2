# 2024.09.19
# 이미지 분석 강의 - threshold
# threshold: 문턱값

import cv2
import numpy as np
import matplotlib.pylab as plt


# 첫번째 방법
# 127로 중간 숫자를 고정

img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)
# 여기서 이미지의 색상코드를 0으로 바꿔서 검은색으로 바꿈
thres_np = np.zeros_like(img)
# 127색을 기준으로 색 나누기
# thres_np[img > 127] = 255

# 4가지 단계로 나누기 1번째 방법
# thres_np[(img < 128) & (img >= 64)] = 64
# thres_np[(img < 191) & (img >= 128)] = 171
# thres_np[(img < 256) & (img >= 192)] = 255

# 4가지 단계로 나누기 2번째 방법
# thres_np = np.zeros_like(img)
# thres_np[img > 64] = 64
# thres_np[img > 128] = 128
# thres_np[img > 192] = 255

# 4가지 단계로 나누기 3번째 방법
thres_np = np.zeros_like(img)
xsize, ysize = img.shape
for x in range(xsize):
    for y in range(ysize):
        if(img[x,y] > 64):
            thres_np[x,y] = 64
        if(img[x,y] > 128):
            thres_np[x,y] = 128
        if(img[x,y] > 192):
            thres_np[x,y] = 255

# 위와 같은 역할을 함
_, thres_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# print(ret)

cv2.imshow('thr', thres_np)
cv2.imshow('IMG', img)
cv2.imshow('cv2', thres_cv)
cv2.waitKey()
cv2.destroyAllWindows()


# 두번째 방법
# 이미지에 따라 문턱값을 여러개로 조정

img = cv2.imread('./img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)
_, t80 = cv2.threshold(img,80, 255, cv2.THRESH_BINARY)
_, t100 = cv2.threshold(img,100, 255, cv2.THRESH_BINARY)
_, t120 = cv2.threshold(img,120, 255, cv2.THRESH_BINARY)
_, t140 = cv2.threshold(img,140, 255, cv2.THRESH_BINARY)

cv2.imshow('t80', t80)
cv2.imshow('t100', t100)
cv2.imshow('t120', t120)
cv2.imshow('t140', t140)
cv2.waitKey()
cv2.destroyAllWindows()


# 세번째 방법
# otsu 알고리즘 적용

_, t130 = cv2.threshold(img,130, 255, cv2.THRESH_BINARY)
# otsu로 적절히 적용되도록 함
t, totsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(t)

cv2.imshow('t130', t130)
cv2.imshow('totsu', totsu)
cv2.waitKey()
cv2.destroyAllWindows()


# 네번째 방법
# 적응형 문턱값을 적용: 주위값에 따라 달라짐, blk_size에 따라 달라짐

# 가장 까다로웠던 스도쿠에 적용해봄
img = cv2.imread('./img/sudoku.png', cv2.IMREAD_GRAYSCALE)
# 아래처럼 그래디언트 이미지에는 정확하게 적용되지 않음
# img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

blk_size = 9
C = 5

ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(ret)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY , blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , blk_size, C)

cv2.imshow('img', img)
cv2.imshow('totsu', th1)
cv2.imshow('tmean', th2)
cv2.imshow('tgaussian', th3)

cv2.waitKey()
cv2.destroyAllWindows()