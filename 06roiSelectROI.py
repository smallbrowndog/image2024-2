# x,y,w,h = cv2.selectROI('img', img, False)
# selectROI 를 직접 만들어 본다
# 개략적인 얼개만 보인다
import cv2


def onMouse(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print('Lbutton down')
        print(x,y)
        x0 = x; y0 = y;
    elif(event == cv2.EVENT_MOUSEMOVE):
        # print('mouse move')
        # print(x,y)
        XX = 1 # 오류 안 뜨게 잠시 넣어둠
    elif(event == cv2.EVENT_LBUTTONUP):
        print('Lbutton up')
        print(x,y)
        x1 = x; y1 = y;

img = cv2.imread('./img/sunset.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)

cv2.waitKey()
cv2.destroyAllWindows()