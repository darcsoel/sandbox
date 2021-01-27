import sys

import keras
from keras.datasets.reuters import get_word_index, load_data
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = load_data()
    word_index = get_word_index()

    num_classes = max(y_train) + 1
    print(f'Number of classes: {num_classes}')

    index_to_word = {}
    for key, value in word_index.items():
        index_to_word[value] = key

    max_words = 10000

    tokenizer = Tokenizer(num_words=max_words)
    x_train = tokenizer.sequences_to_matrix(x_train)
    x_test = tokenizer.sequences_to_matrix(x_test)

    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    print(x_train[0])
    print(len(x_train[0]))

    print(y_train[0])
    print(len(y_train[0]))

    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    print(model.metrics_names)

    batch_size = 32

    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=10,
                        validation_split=0.1)
    score = model.evaluate(x_test, y_test, batch_size=batch_size)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    sys.exit()
