import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./img/mountain.jpg', cv2.IMREAD_GRAYSCALE)

# 0~255로 얼마나 밝은지 어두운지 확인
hist = cv2.calcHist([img], [0], None, [256], [0,255])
plt.plot(hist)
plt.show()

cv2.imshow('mountain_gray', img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('./img/graduate.jpg')

cv2.imshow('mountain_color', img)

# BGR 세가지의 채널로 나누어서 표현하도록 한다
channels = cv2.split(img)
# print(channels)

# 이전의 3차원을 나누어서 표현함
colors = ('b', 'g', 'r')
for (ch, color) in zip(channels, colors):
    print(ch)
    print(color)
    hist = cv2.calcHist([ch], [0], None, [256], [0,255])
    # 각자의 색상대로 히스토그램을 그리겠다라는 코드
    plt.plot(hist, color = color)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()