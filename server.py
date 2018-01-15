from __future__ import print_function
import tensorflow as tf
import time

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
while True:
  time.sleep(10)
  print(sess.run(hello))
