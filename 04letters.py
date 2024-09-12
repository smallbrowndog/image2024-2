import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# OpenCV로 빈 이미지 생성
img = np.full((500, 500, 3), 255, dtype=np.uint8)

# sans-serif small
cv2.putText(img, "Plain", (50,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
# sans-serif normal
cv2.putText(img, "Simplex", (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
# sans-serif bold
cv2.putText(img, "Duplex", (50,110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))
# sans-serif normal 스케일 늘리기
cv2.putText(img, "Simplex * 2", (50,170), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0))

# serif small
cv2.putText(img, "Complex small", (50,240), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
# serif normal
cv2.putText(img, "Complex", (50,280), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
# serif bold
cv2.putText(img, "Triplex", (50,320), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
# serif normal
cv2.putText(img, "Complex * 2", (50,380), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0))

# 폰트 설정 (원하는 경로에 있는 TTF 폰트 파일을 사용)
fontpath = "C:/dev/image2024-2/BMJUA_ttf.ttf"  # 원하는 한글 폰트 파일 경로 설정
font = ImageFont.truetype(fontpath, 20)  # 폰트 크기 설정

# OpenCV의 이미지 배열을 PIL 이미지로 변환
img_pil = Image.fromarray(img)

# Pillow의 ImageDraw 사용
draw = ImageDraw.Draw(img_pil)

# 한글 텍스트
draw.text((50, 460), "아름다운 강산 - 김기주", font=font, fill=(0, 0, 0))

# 다시 OpenCV 형식으로 변환
img = np.array(img_pil)

# 이미지 출력
cv2.imshow('letters', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
