import tensorflow as tf

# MNIST 데이터 세트를 가져
mnist = tf.keras.datasets.mnist
# x_train, x_test은 모델의 입력값, y_train, y_test는 기대 출력값
# 여기서 x에는 손글씨 숫자 이미지, y에는 이미지가 의미하는 숫자가 대입됨
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 이미지 값은 0~255값을 가지지만 0~1값을 갖도록 변환(학습을 위해)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 뉴럴 네트워크 모델을 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # 입력노드개수 28 x 28
    tf.keras.layers.Dense(128, activation='relu'),  # 히든레이어개수
    tf.keras.layers.Dropout(0.2),  # 무작위로 이전 레이어의 출력을 20% 끔
    tf.keras.layers.Dense(10, activation='softmax')  # 출력노드개수 10
])

# 학습을 위한 optimizer와 loss function을 선택
model.compile(optimizer='adam',  # optimizer는 경사하강법을 개선한 것
              loss='sparse_categorical_crossentropy',  # 손실함수(모델의 출력이 one-hot encoding 된다면)
              metrics=['accuracy'])  # 모델을 평가할 때 사용 여기선 정확도(accuracy)

# 학습 데이터 세트를 사용하여 모델을 학습. 5번 반복
model.fit(x_train, y_train, epochs=5)

# 테스트 데이터 세트를 사용하여 모델을 평가
model.evaluate(x_test, y_test)
