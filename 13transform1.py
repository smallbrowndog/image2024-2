import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')

rows, cols = img.shape[0:2]

print(img.shape)
print(f'rows = {rows}, cols = {cols}')

dx, dy = 100, 50

# 이미지 단순 이동
mtrx = np.float32([[1,0,dx], [0,1,dy]])
# mtrx = np.float32([[0,1,dx], [1,0,dy]])
dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()