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
# 단순 이동
dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))

# 탈락된 외곽 픽셀을 파란색으로 보정
dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255,0,0))

# 탈락된 외곽 픽셀 원본을 반사시켜서 보정
dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.imshow('BORDER_CONSTANT', dst2)
cv2.imshow('BORDER_REFLECT', dst3)
cv2.waitKey()
cv2.destroyAllWindows()

height, width, _ = img.shape
# height, width = img.shape[0:2] 와 같음

# 0.5배 축소 변환 행렬
m_small = np.float32([[0.5, 0, 0],
                      [0, 0.5, 0]])
# 2배 확대 변환 행렬
m_big = np.float32([[1.5, 0, 0],
                    [0, 1.5, 0]])
# 보간법 적용 없이 확대 축소
dst1 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)))
dst2 = cv2.warpAffine(img, m_big, (int(height*1.5), int(width*1.5)))

# 보간법 적용한 확대 축소
dst3 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)), None, cv2.INTER_AREA)
# cube는 3차원 곡선으로 두 점 사이를 이어주는것
dst4 = cv2.warpAffine(img, m_big, (int(height*1.5), int(width*1.5)), None, cv2.INTER_CUBIC)


cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('small INTER_AREA', dst3)
cv2.imshow('big INTER_CUBIC', dst4)
cv2.waitKey()
cv2.destroyAllWindows()