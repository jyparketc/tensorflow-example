from __future__ import print_function
import tensorflow as tf
import time

t_end = time.time() + 60 * 5
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
while time.time() < t_end:
  time.sleep(10)
  print(sess.run(hello))
