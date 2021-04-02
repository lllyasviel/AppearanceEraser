# Python (TensorFlow) Implementation of basic TV image smoothing
# For reviewing purposes only. Please refer to main article for more details.

import sys
sys.path.append('..')

from configs.config import *

import tensorflow as tf  # This code has been tested under many versions of TensorFlow using CPU or GPU
import numpy as np

session = tf.Session()  # Creating TensorFlow Session

optimizer = tf.train.AdamOptimizer(learning_rate=0.005)  # Using Adam to optimize TV

# Here we use RGB sample images.
source_variable = tf.Variable(tf.zeros(shape=[image_height, image_width, 3], dtype=tf.float32), trainable=False)
target_variable = tf.Variable(tf.zeros(shape=[image_height, image_width, 3], dtype=tf.float32), trainable=True)

# Binarized variable for erasing set.
# Ones are for supporting positions and Zeros are for non-supporting positions.
erasing_set = tf.Variable(tf.ones(shape=[image_height, image_width, 1], dtype=tf.float32), trainable=False)

# Define appearance preserving energy and TV smoothing energy.
appearance_preserving_term = tf.square(source_variable - target_variable)
smoothing_term = tf.reduce_sum(tf.abs(target_variable[1:, :, :] - target_variable[:-1, :, :])) + \
                 tf.reduce_sum(tf.abs(target_variable[:, 1:, :] - target_variable[:, :-1, :]))

# Only minimize source and target distance in supporting position set.
appearance_preserving_term *= erasing_set

# Define optimization operation.
loss = tf.reduce_sum(appearance_preserving_term) + tf.reduce_sum(smoothing_term) * 0.1
optimization = optimizer.minimize(loss, var_list=[target_variable])
session.run(tf.global_variables_initializer())


def total_variation_smoothing(image, erasing_positions):

    # feed images.
    session.run(tf.assign(ref=source_variable, value=image))
    session.run(tf.assign(ref=target_variable, value=image))
    session.run(tf.assign(ref=erasing_set, value=erasing_positions[:, :, None]))

    # Here we roughly run 250 turns.
    for i in range(250):
        session.run(optimization)

    # Read Smoothed Images.
    smoothed_image = session.run(target_variable).astype(np.float32)

    return smoothed_image
