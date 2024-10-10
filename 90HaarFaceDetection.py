import cv2
from cv2.data import haarcascades

face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')
img = cv2.imread('./img/graduate.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray)
# print(faces)
# x, y, w, h = faces[0]
# print(f'x={x}')
# cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 10)

# 눈이 얼굴 안에 있기때문에 eye를 face안에 넣어줌
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 8)
    # 아래처럼 하면 y,x로 인식을 해야하는데 x,y로 인식을 해서 코드를 변경해준다
    # eyes = eye_cascade.detectMultiScale(gray[x:x+w, y:y+h])
    eyes = eye_cascade.detectMultiScale(gray[y:y+h, x:x+w])
    # print(eyes)
    # for x, y, w, h in eyes:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 얼굴 좌표를 따로 찾아서 부여해주어야함
    # 아래 코드를 부여하지 않으면 코드가 제대로 동작하지 않음
    new_img = img[y:y+h, x:x+w]
    # print(eyes)
    for x, y, w, h in eyes:
        cv2.rectangle(new_img, (x, y), (x + w, y + h), (0, 255, 0), 2)


# 교수님 최종 정리
for fx, fy, fw, fh in faces:
    cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 8)
    eyes = eye_cascade.detectMultiScale(gray[fy:fy+fh, fx:fx+fw])
    # print(eyes)
    for ex, ey, ew, eh in eyes:
        cv2.rectangle(img, (ex + fx, ey + fy), (ex + + fx + ew, ey + fy + eh), (0, 255, 0), 2)


cv2.imshow('gray', img)
cv2.waitKey()
cv2.destroyAllWindows()