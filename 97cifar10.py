import datetime
import cv2
from tensorboard.plugins.histogram.summary import histogram
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.layers.core import dropout, Dropout
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D

mlp_model = Sequential([
    Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)),  # Conv2D로 변경
    Flatten(),
    Dense(32, activation='relu'),
    Dense(10, activation='softmax')
])


(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

print(train_images.shape, train_labels.shape)
print(test_images.shape, test_labels.shape)

print(train_images[999])
print(train_labels[999])
# cv2.imshow('cifar', cv2.resize(train_images[999], (320, 320)))
# cv2.waitKey()
# cv2.destroyAllWindows()

val_images = train_images[45000:]
val_labels = train_labels[45000:]

# 처음 모델, 총 파라미더 17만개
# mlp_model = Sequential([
#     Flatten(input_shape=(32,32,3)),
#     Dense(512, activation='relu'),
#     Dense(256, activation='relu'),
#     Dense(128, activation='relu'),
#     Dense(10, activation='softmax')
# ])

# 두번째 모델
# mlp_model = Sequential([
#     Flatten(input_shape=(32,32,3)),
#     Dense(512, activation='relu'),
#     Dropout(0.2),
#     Dense(256, activation='relu'),
#     Dropout(0.2),
#     Dense(128, activation='relu'),
#     Dropout(0.2),
#     Dense(10, activation='softmax')
# ])

# 단순 Conv2D 모델
mlp_model = Sequential([
    Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)),
    Flatten(),
    Dense(32, activation='relu'),
    Dense(10, activation='softmax')
])

# 동작하는 Conv2D 모델
mlp_model = Sequential([
    Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2,2)),
    Conv2D(62, (3, 3), padding='same', activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), padding='same', activation='relu'),
    Flatten(),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

mlp_model.summary()

mlp_model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

# 텐서보드 실행준비
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir,
                                                      histogram_freq=1)
print(log_dir)
history = mlp_model.fit(train_images, train_labels, epochs=10,
                        validation_data=(val_images, val_labels),
                        callbacks=[tensorboard_callback])

print('Test 결과')
mlp_model.evaluate(test_images, test_labels)
# plt.plot(history.history['accuracy'], label='Train Accuracy')
# plt.plot(history.history['loss'], label='loss')
# plt.show()