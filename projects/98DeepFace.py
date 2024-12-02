import cv2
from deepface import DeepFace
import time
import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

img_file = '../img/children_smiling.jpg'
# backend = ['opencv', 'ssd', 'dlib', 'mtcnn', 'fastmtcnn', 'retinaface', 'mediapipe', 'yolov8', 'yunet', 'centerface']
# backend = ['opencv', 'ssd', 'mtcnn', 'retinaface', 'mediapipe', 'yolov8', 'yunet', 'centerface']
backend = ['opencv', 'mtcnn', 'retinaface', 'yolov8', 'centerface']

all_process_time = []
images = []

for i in backend:
    start = time.time()
    img = cv2.imread(img_file)

    detections = DeepFace.extract_faces(img_path=img_file,
                                        detector_backend=i,
                                        enforce_detection=False)
    # print(detections)

    if not detections:
        print("얼굴이 인식되지 않았습니다")
    else:
        # 각 얼굴에 대해 영역 표시
        for face in detections:
            facial_area = face['facial_area']
            x1 = facial_area['x']
            y1 = facial_area['y']
            x2 = x1 + facial_area['w']
            y2 = y1 + facial_area['h']

            # 사각형으로 얼굴 표시
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.putText(img, f"Engine: {i}", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
    end = time.time()
    process_time = round((end - start), 2)
    print(f"{i}를 구동하는데 걸린 시간: {process_time}초")

    all_process_time.append({"backend": i, "process_time": process_time})
    images.append(img)

    # cv2.imshow(f"{i}", img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

manyimage = cv2.vconcat(images)
cv2.imwrite('../vstack.png', manyimage)
all_process_time_df = pd.DataFrame(all_process_time)
print(all_process_time_df)

all_process_time_df = pd.DataFrame(all_process_time)

# x축 레이블 및 y축 값 설정
x = all_process_time_df['backend']
y = all_process_time_df['process_time']
plt.bar(x, y, color='skyblue')
plt.xlabel("Backend", fontsize=14)
plt.ylabel("Process Time", fontsize=14)
plt.xticks(rotation=20)
plt.show()