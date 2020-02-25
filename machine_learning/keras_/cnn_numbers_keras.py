"""
Simple Keras NN for recognise simple images of numbers
Running on CPU or GPU

"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

physical_devices = tf.config.experimental.list_physical_devices('GPU')
gpu_test = tf.test.is_gpu_available()
version = tf.version.VERSION

tf.config.experimental.set_memory_growth(physical_devices[0], True)
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    # Restrict TensorFlow to only allocate 1GB of memory on the first GPU
    try:
        tf.config.experimental.set_virtual_device_configuration(
            gpus[0],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2048)])
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Virtual devices must be set before GPUs have been initialized
        print(e)

with tf.device('CPU:0'):
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    x_train = x_train.reshape(60000, 28, 28, 1)
    x_test = x_test.reshape(10000, 28, 28, 1)

    y_train = keras.utils.to_categorical(y_train)
    y_test = keras.utils.to_categorical(y_test)

    model = keras.models.Sequential()

    model.add(layers.Conv2D(64, kernel_size=3, input_shape=(28, 28, 1), activation='relu'))
    model.add(layers.Conv2D(32, kernel_size=3, activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer=keras.optimizers.Adam(), loss=keras.losses.CategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=6)
    model.save('keras_cnn.h5')

    print(model.predict(x_test[:4]))
    print(y_test[:4])

exit()

# unix time on macbook air I5-5250U
# real    11m23.957s
# user    32m19.105s
# sys     2m9.797s

# unix time on amd ryzen 5 3600
# real    4m9,047s
# user    18m22,199s
# sys     0m19,405s
