import cv2
import numpy as np
from PyQt5.sip import array

img = cv2.imread("./img/children.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gx_kernel = np.array([[-1, 1]])
gy_kernel = np.array([[-1], [1]])

# 가로축방향으로 뺄셈(이미지의 오른쪽 값에서 왼쪽값을 뺌)
edge_gx = cv2.filter2D(img, -1, gx_kernel)
# 세로축방향으로 뺄셈
edge_gy = cv2.filter2D(img, -1, gy_kernel)

cv2.imshow("sudoku", img)
cv2.imshow("edge x", edge_gx)
cv2.imshow("edge y", edge_gy)
cv2.waitKey()
cv2.destroyAllWindows()

# Sobel 커널 만들기
gx_k = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy_k = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
edge_gxs = cv2.filter2D(img, -1, gx_k)
edge_gys = cv2.filter2D(img, -1, gy_k)
cv2.imshow("sudoku", img)
cv2.imshow("s edge x", edge_gxs)
cv2.imshow("s edge y", edge_gys)

sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)
sobelxy = sobelx + sobely

cv2.imshow("sobel x", sobelx)
cv2.imshow("sobel y", sobely)
cv2.imshow("sobel xy", sobelxy)

# Scharr 필터
gx_ksc = np.array([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
gy_ksc = np.array([[-3, -10, -3],[0, 0, 0], [3, 10, 3]])

scharx = cv2.filter2D(img, -1, gx_ksc)

cv2.imshow("scharx", scharx)

# Laplacian
gx_kl = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

lapl = cv2.filter2D(img, -1, gx_kl)
laplf = cv2.filter2D(img, -1, gx_kl)

# 흑백으로 바꿔주어야 함, 엣지를 검출할때는 색이 중요한게 아니라 모양이 중요한것이기때문에 흑백으로 바꾸어야함
canny = cv2.Canny(img, 50, 150)

cv2.imshow("laplace", lapl)
cv2.imshow("laplacian", laplf)
cv2.imshow("canny", canny)

cv2.waitKey()
cv2.destroyAllWindows()
