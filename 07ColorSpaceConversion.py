import cv2
import numpy as np

img_file = './img/girl.jpg'
img = cv2.imread(img_file)
print(img.shape)

# cv2.imshow('IMG', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

imgy = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(imgy)

cv2.imshow('IMG', img)
cv2.imshow('IMG2', y)
cv2.waitKey()
cv2.destroyAllWindows()

# 위에서 확인한 크기로 입력
imgyy = np.full((293, 406), 255, dtype=np.uint8)
b, g, r = cv2.split(img)
imgyy = 0.299 * r + 0.587 * g + 0.114 * b
print(imgyy)
imgyy = imgyy.astype(np.uint8)
diff = y - imgyy
print(diff)
cv2.imshow('IMG', img)
cv2.imshow('IMG CV2 change', y)
cv2.imshow('IMG cal change', imgyy)
cv2.imshow('diff', diff)
cv2.waitKey()
cv2.destroyAllWindows()