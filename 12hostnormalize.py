import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0,255])
plt.plot(hist)
plt.show()

# 이미지 색 값 정규화 1
img_norm = (img - img.min()) * 255 / (img.max() - img.min())

# 이미지 색 값 정규화 2
img_normcv = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('img', img)
cv2.imshow('imgNorm', img_norm)
cv2.imshow('imgNormCV', img_normcv)
cv2.waitKey()
cv2.destroyAllWindows()