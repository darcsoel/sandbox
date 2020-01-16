import tensorflow as tf

a = [[0.1, 0.2, 0.3],
     [20, 2, 3]
     ]
b = tf.Variable(a, name='b')

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    result = sess.run(tf.argmax(b, 1))

    print(f'Argmax - {result}')
