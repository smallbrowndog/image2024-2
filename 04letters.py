import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

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

cv2.imshow('letters', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 한글

# cv2.putText(img, "아름다운 강산 - 김기주", (50, 460), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,0))

# cv2 -> PIL 이미지로 변경
color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_pil=Image.fromarray(color_coverted)

# PIL 이미지에 한글 입력
draw = ImageDraw.Draw(img_pil)
draw.text((10, 10),  "안녕하세요!", font=ImageFont.truetype("./malgun.ttf", 48), fill=(255,255,255))

# PIL 이미지 -> cv2 Mat 타입으로 변경
numpy_img = np.array(img_pil)
cv_img = cv2.cvtColor(numpy_img, cv2.COLOR_RGB2BGR)

# 변경된 cv2 Mat 타입 출력
cv2.imshow("test", cv_img)
cv2.waitKey()
cv2.destroyAllWindows()
