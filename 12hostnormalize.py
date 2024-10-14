import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./img/yate.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0,255])
plt.plot(hist)
plt.show()

# 이미지 색 값 정규화 1

# 아래와 같이 작성하게 되면 까만 화면만 나오게 됨, 값이 1, 2 등의 낮은 값만 나오게 됨
# 255.0이 아닌 255로 작성하게 되면 (img - img.min()) * 255 이 때 8비트의 범위를 벗어나서 오버플로우가 발생하게 된다
# img_norm = ((img - img.min()) * 255) / (img.max() - img.min())

# 정리
# 분자의 오버플로우에 의한 에러
# img_norm = ((img - img.min()) * 255) / (img.max() - img.min())

# 첫번째 방법
# 먼저 나누어준 이후 255를 곱한다
# img_norm = ((img - img.min()) / (img.max() - img.min()) * 255

# 두번째 방법
# 형변환을 유도한다 8bit int > float로 변환
# img_norm = ((img - img.min()) * 255.0) / (img.max() - img.min())

# 세번째 방법
# 직접 형변환하기 / 이 방법이 다른 사람들도 알아보기 쉬워서 추천하는 방법임
img_f = img.astype(np.float32)
img_norm = (img_f - img_f.min()) * 255 / (img_f.max() - img_f.min())



# 이미지 색 값 정규화 2
img_normcv = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

print(img_norm)


# 히스토그램 비교
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0,255])
hist_normcv = cv2.calcHist([img_normcv], [0], None, [256], [0,255])

# 최초 이미지, 직접 정규화, normalize 사용 정규화 히스토그램 비교
plt.subplot(1,3,1)
plt.plot(hist)
plt.title('hist')
plt.subplot(1,3,2)
plt.plot(hist_norm)
plt.title('hist_norm')
plt.subplot(1,3,3)
plt.plot(hist_normcv)
plt.title('hist_normcv')
plt.show()

cv2.imshow('img', img)
# .astype(np.uint8)을 넣어줘서 소수점을 지워주면서 정상적인 값이 나오도록 함, 지금 8비트 int를 사용하기때문에
# cv2.imshow('imgNorm', img_norm)
cv2.imshow('imgNorm', img_norm.astype(np.uint8))
cv2.imshow('imgNormCV', img_normcv)
cv2.waitKey()
cv2.destroyAllWindows()