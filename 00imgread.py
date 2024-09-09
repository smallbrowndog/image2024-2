import cv2

img_file = "./img/girl.jpg"
img = cv2.imread(img_file)
cv2.imshow("IMG", img)
cv2.waitKey()   # 아무 키나 입력될 때 까지 대기
cv2.destroyAllWindows() # 창 모두 닫기

# # pillow 이용하기
# from PIL import Image
# img = Image.open("./img/girl.jpg")
# img.show()

# 그레이 스케일로 읽어오기
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyAllWindows()

# 동영상 파일 읽어오기
video_file = "./img/big_buck.avi"
cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25) # 25ms마다 가져오는것
        else:
            break
else:
    print("cannot open video")
cap.release()
cv2.destroyAllWindows()