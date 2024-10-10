import cv2

img1 = cv2.imread('./img/robot_arm1.jpg')
img2 = cv2.imread('./img/robot_arm2.jpg')

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.subtract(img1_gray, img2_gray)
absdiff = cv2.absdiff(img1_gray, img2_gray)

_, diff2 = cv2.threshold(absdiff, 1, 255, cv2.THRESH_BINARY)

# 흰색이 아닌 다른 색으로 표현하기 위해서 코드 작성
diff_red = cv2.cvtColor(diff2, cv2.COLOR_GRAY2BGR)
diff_red[0:-1, 0:-1, 0] = 0

spot = cv2.bitwise_xor(img2, diff_red)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('diff', diff)
cv2.imshow('absdiff', absdiff)
cv2.imshow('diff2', diff2)
cv2.imshow('diff_red', diff_red)
cv2.imshow('spot', spot)
cv2.waitKey()
cv2.destroyAllWindows()