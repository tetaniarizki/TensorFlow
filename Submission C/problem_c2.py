# -*- coding: utf-8 -*-
"""Problem_C2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N5Jek07ttYFbtMB1A-nyHp5Vafwgtiw7
"""

# =============================================================================
# PROBLEM C2
#
# Create a classifier for the MNIST Handwritten digit dataset.
# The test will expect it to classify 10 classes.
#
# Don't use lambda layers in your model.
#
# Desired accuracy AND validation_accuracy > 91%
# =============================================================================

import tensorflow as tf
from tensorflow import keras


def solution_C2():
    mnist = tf.keras.datasets.mnist
    (x_train,y_train),(x_test,y_test)=mnist.load_data()
    # NORMALIZE YOUR IMAGE HERE
    x_train=x_train/255.0
    x_test=x_test/255.0

    # DEFINE YOUR MODEL HERE
    # End with 10 Neuron Dense, activated by softmax
    # Remember to inherit from the correct class
    class myCallback(tf.keras.callbacks.Callback):
      # Define the correct function signature for on_epoch_end
      def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') is not None and logs.get('accuracy') > 0.92: 
          print("\nReached 99% accuracy so cancelling training!") 
          # Stop training once the above condition is met
          self.model.stop_training = True
    
    callbacks = myCallback()
    model = tf.keras.models.Sequential([ 
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(512, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ]) 
  

    # COMPILE MODEL HERE
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    # TRAIN YOUR MODEL HERE
    history = model.fit(x_train, y_train, epochs=10, callbacks=[callbacks], 
                        validation_data=(x_test,y_test))

    return model


# The code below is to save your model as a .h5 file.
# It will be saved automatically in your Submission folder.
if __name__ == '__main__':
    # DO NOT CHANGE THIS CODE
    model = solution_C2()
    model.save("model_C2.h5")