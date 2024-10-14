# 12histnormalize에서 값이 0인것들이 양 극단에 있다면 정상적으로 잘 작동하지만 yate.jpg처럼 0이 아닌 아주 작은 값이 있거나 특정하게 튀어나온 값들이 있을때의 평탄화가 되지 않는 문제점이 있다

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./img/yate.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0,255])

img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0,256])

img_eq = cv2.equalizeHist(img)
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0,255])

cv2.imshow('img', img)
cv2.imshow('img_norm', img_norm)
cv2.imshow('img_eq', img_eq)

plt.subplot(1, 3, 1)
plt.plot(hist)
plt.title('hist')
plt.subplot(1, 3, 2)
plt.plot(hist_norm)
plt.title('hist_norm')
plt.subplot(1, 3, 3)
plt.plot(hist_eq)
plt.title('hist_eq')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()