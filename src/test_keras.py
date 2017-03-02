"""
An excerpt from keras' source code example of classifying the
cifar-10 dataset.

Copied the initial part here to play around and try and get a handle
on concepts like:
    - input image dimensionality
    - input image depth (i.e. note the 3 color channels in rgb images)
"""
from __future__ import print_function
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

batch_size = 32
nb_classes = 10
nb_epoch = 200
data_augmentation = True

# input image dimensions
img_rows, img_cols = 32, 32
# The CIFAR10 images are RGB.
img_channels = 3

# The data, shuffled and split between train and test sets:
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
print('shape of an individual example: ',X_train[0].shape)

# above print statements show:
# shape: (60000, 3, 32, 32)
# i.e. input is an array of 60,000 examples
# each example has 3 subarrays (i.e. depth = 3) - corresponding to R, G, and B
# each of the R, G, B subarrays is a 32x32 matrix representing the image
#   from the perspective of that channel
# contrastingly, note how greyscale images have only one channel
# - hence a similar dataset for them would be (60000, 32, 32)
# - you'd have to add a 1 to mark depth, thus converting to (60000, 1, 32, 32)
