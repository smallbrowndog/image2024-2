# 2024.11.4
# 이미지분석프로젝트 필터 - 블러

import cv2
import numpy as np

img = cv2.imread('./img/girl.jpg')

# 나눠줘야 하는 이유: 커널이 모두 더해졌을때 값이 1이 되어야 하는데 나눠주지 않으면 값이 너무 커져서 밝아지게 된다
kernel = np.ones((5,5)) / 25
# print(kernel)

blured = cv2.filter2D(img, -1, kernel)

cv2.imshow('org', img)
cv2.imshow('blur', blured)
cv2.waitKey()
cv2.destroyAllWindows()


img = cv2.imread('./img/gaussian_noise.jpg')
kernel = np.ones((5,5))/25
blured = cv2.filter2D(img, -1, kernel)

# 위처럼 동일하게 모든 값이 더해졌을때 1이 되어야 하기때문에 값에 맞게 나눠준다
k1 = np.array([[1,2,1],
               [2,4,2],
               [1,2,1]]) / 16
print(f'k1: \n{k1}')

k2 = cv2.getGaussianKernel(5, 0)
# k1 = np.array([[1,2,1]]) / 4 의 방식과 동일하다고 볼 수 있음, 하지만 ksize가 커질수록 수를 입력하고 나눠주기 번거롭기때문에 Gaussian을 사용하는것
print(f'k2: \n{k2}')

k1Img = cv2.filter2D(img, -1, k1)
# k2.T는
# [[0.25]
#  [0.5 ]
#  [0.25]]
#         를 [[0.25 0.5  0.25]] 처럼 변경한것이다
k2Img = cv2.filter2D(img, -1, k2 * k2.T)
print(f'k2 * k2.T: \n{k2 * k2.T}')

# 모든 값들을 정렬해서 가운데 값만 취해서 변환하는것
k3Img = cv2.medianBlur(img, 5)
# 기존의 blur는 주변(1의 범위)에 따라
k4Img = cv2.bilateralFilter(img, 5, 75, 75)

cv2.imshow('noise', img)
cv2.imshow('blur', blured)
cv2.imshow('k1', k1Img)
cv2.imshow('k2', k2Img)
cv2.imshow('median', k3Img)
cv2.imshow('bilateral', k4Img)
cv2.waitKey()
cv2.destroyAllWindows()