import tensorflow as tf

# Download the code
print('Tensorflow version: {}'.format(tf.__version__) )
print('GPU Identified at: {}'.format(tf.test.gpu_device_name()))