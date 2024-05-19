import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split as tts

from src.image import Image

target = input("Enter target image: ")  # 사진이 images 디렉터리 안에 있어야 함
image = Image(plt.imread(f"images/{target}"))  # 이미지 객체 생성

plt.figure(figsize=(image.array.shape[0] / 100, image.array.shape[1] / 100))
gradient_array = np.array(np.gradient(image.array)[0][:][:])
# plt.imshow(_a, cmap="seismic", interpolation='none', resample=False)
plt.show()

# 선형 회귀로 별 식별
lr = LR()
x_train, x_test, y_train, y_test = tts()
