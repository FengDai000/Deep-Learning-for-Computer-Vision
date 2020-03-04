import tensorflow.compat.v1 as tf
tf.disable_v1_behavior()

x = tf.placeholder(tf.float32, name='x')
y = tf.placeholder(tf.float32, name='y')
z = tf.add(x, y, name='sum')
session = tf.Session()
summary_writer = tf.summary.FileWriter('/tmp/1', session.graph)
summary_writer.flush()

