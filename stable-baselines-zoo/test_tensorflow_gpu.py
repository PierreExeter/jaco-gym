import tensorflow as tf
import numpy as np

print("Numpy version: ", np.__version__)
print('Tensorflow version: ', tf.__version__)

gpus = tf.config.experimental.list_physical_devices('GPU') 
print('GPU list: ', gpus)
print('Num GPUs Available: ', len(gpus))
print('Is Tensorflow built with CUDA? ', tf.test.is_built_with_cuda())
print('Is a GPU available?', tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))


# # with tf.device('/gpu:0'):
# #     a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
# #     b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
# #     c = tf.matmul(a, b)

# # with tf.Session() as sess:    # TF1
# # # with tf.compat.v1.Session() as sess:    # TF2
# #     print (sess.run(c))
