import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.utils.np_utils import to_categorical
# import matplotlib.pyplot as plt

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(28, (3,), activation='relu',
                           padding='same',
                           input_shape=(28, 28)),
    tf.keras.layers.Conv1D(28, (3,), activation='relu'),
    tf.keras.layers.MaxPooling1D(pool_size=(2,)),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(10, activation='softmax')
])

if __name__ == '__main__':
    dataset = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = dataset.load_data()

    print('*********************', x_train[0].shape)
    # plt.imshow(x_train[0])
    # plt.show()
    # plt.imshow(x_train[1])
    # plt.show()

    # Normalize data set to 0-to-1 range
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    # Convert class vectors to binary class matrices
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    model.summary()
    model.fit(x_train, y_train, epochs=5)

    loss, accuracy = model.evaluate(x_test, y_test)
    print(f'Loss = {loss}; Accuracy = {accuracy}')

    predicted_images = model.predict(x_test)
    for predicted_image, img in zip(predicted_images, x_test):
        plt.imshow(img)
        plt.title(int(np.argmax(predicted_image)))
        plt.show()
