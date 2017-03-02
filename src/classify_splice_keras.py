####### import libraries and modules ########
from seq_reader import load_data        # parsing data file
from one_hot_rep import get_rep_mats, conv_labels   # converting to correct format

import numpy as np
np.random.seed(123)  # for reproducibility

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
#############################################

# 1. Load data into train and test sets
X, y = load_data("../data/splice.data.txt")   # sequences, labels
X = get_rep_mats(X)     # convert to array of representation matrices
############
for i in X:
    for idx, j in enumerate(i):
        i[idx] = j[0]
############
y = conv_labels(y)      # convert to integer labels
X = np.asarray(X)       # work with np arrays
y = np.asarray(y)
X_train = X[0:2872]
X_test = X[2872:]
y_train = y[0:2872]
y_test = y[2872:]

# 2. Preprocess input data
# X_train = X_train.reshape(X_train.shape[0], 64, 57, 2)  # (2872, 57, 2, 64) (2872,) becomes (2872, 64, 57, 2) (2872,)
# X_test = X_test.reshape(X_test.shape[0], 64, 57, 2)
print X_train.shape
X_train = X_train.reshape(X_train.shape[0], 1,58, 64)
X_test = X_test.reshape(X_test.shape[0], 1,58, 64)
print X_train.shape
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
# X_train /= 255        this dataset doesn't need to be normalized to [0,1]
# X_test /= 255

# 3. Preprocess class labels; i.e. convert 1-dimensional class arrays to 3-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, 3)   # goes from (2872,) to (2872, 3)
Y_test = np_utils.to_categorical(y_test, 3)

# 4. Define model architecture
model = Sequential()

model.add(Convolution2D(54, 3, 3, activation='relu', input_shape=(1, 58, 64)))
print model.output_shape
#model.add(Convolution2D(54, 3, 3, activation='relu'))      # commented out -- hence only one convolutional layer
print model.output_shape
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

# 5. Compile model
model.compile(loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

# 6. Fit model on training data
model.fit(X_train, Y_train,validation_data=(X_test,Y_test),
              batch_size=32, nb_epoch=10, verbose=1)

# 7. Evaluate model on test data
score = model.evaluate(X_test, Y_test, verbose=1)
print "\nscore = " + str(score)

"""
debug output:
(2872, 58, 64)
(2872, 1, 58, 64)
(None, 54, 56, 62)
(None, 54, 54, 60)
"""
