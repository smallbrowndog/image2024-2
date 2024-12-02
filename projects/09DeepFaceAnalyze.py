import cv2
from deepface import DeepFace

img_file = '../img/children.jpg'
img = cv2.imread(img_file)

actions = ['age', 'gender', 'race', 'emotion']
AR = DeepFace.analyze(img_file, actions=actions)
print(AR)
cv2.rectangle(img, (144, 94), (144+122, 122+92), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()