# Convolutional Neural Networks for DNA Sequence Classification

***NOTE that this readme is currently a mish-mash of results and links of interest. It shall be cleaned up in the future.***

***UPDATE***: The new cross validation branch has yielded following results:
min: 93.71%, average: 95.70% (+/- 1.21%), max: 97.81%

Apparently using one convolutional layer provides a record highest accuracy: 
```
Train on 2872 samples, validate on 318 samples
Epoch 1/10
2872/2872 [==============================] - 27s - loss: 0.3015 - acc: 0.8886 - val_loss: 0.0680 - val_acc: 0.9686
Epoch 2/10
2872/2872 [==============================] - 25s - loss: 0.0932 - acc: 0.9708 - val_loss: 0.1497 - val_acc: 0.9434
Epoch 3/10
2872/2872 [==============================] - 27s - loss: 0.0486 - acc: 0.9857 - val_loss: 0.1792 - val_acc: 0.9497
Epoch 4/10
2872/2872 [==============================] - 26s - loss: 0.0286 - acc: 0.9906 - val_loss: 0.1179 - val_acc: 0.9591
Epoch 5/10
2872/2872 [==============================] - 26s - loss: 0.0195 - acc: 0.9941 - val_loss: 0.2257 - val_acc: 0.9434
Epoch 6/10
2872/2872 [==============================] - 26s - loss: 0.0152 - acc: 0.9962 - val_loss: 0.2719 - val_acc: 0.9340
Epoch 7/10
2872/2872 [==============================] - 26s - loss: 0.0131 - acc: 0.9965 - val_loss: 0.2638 - val_acc: 0.9434
Epoch 8/10
2872/2872 [==============================] - 28s - loss: 0.0158 - acc: 0.9934 - val_loss: 0.2412 - val_acc: 0.9465
Epoch 9/10
2872/2872 [==============================] - 32s - loss: 0.0152 - acc: 0.9955 - val_loss: 0.2302 - val_acc: 0.9528
Epoch 10/10
2872/2872 [==============================] - 29s - loss: 0.0189 - acc: 0.9913 - val_loss: 0.2926 - val_acc: 0.9340
318/318 [==============================] - 0s

score = [0.29261739331783737, 0.9339622619017115]
```

A preliminary result on the splice junction dataset (where our CNN is performing best):

```
in on 2872 samples, validate on 318 samples
Epoch 1/10
2872/2872 [==============================] - 83s - loss: 0.3239 - acc: 0.8771 - val_loss: 0.1107 - val_acc: 0.9623
Epoch 2/10
2872/2872 [==============================] - 75s - loss: 0.0812 - acc: 0.9749 - val_loss: 0.1814 - val_acc: 0.9308
Epoch 3/10
2872/2872 [==============================] - 78s - loss: 0.0661 - acc: 0.9784 - val_loss: 0.2546 - val_acc: 0.9151
Epoch 4/10
2872/2872 [==============================] - 74s - loss: 0.0395 - acc: 0.9857 - val_loss: 0.1611 - val_acc: 0.9403
Epoch 5/10
2872/2872 [==============================] - 77s - loss: 0.0209 - acc: 0.9934 - val_loss: 0.2396 - val_acc: 0.9340
Epoch 6/10
2872/2872 [==============================] - 81s - loss: 0.0147 - acc: 0.9955 - val_loss: 0.2094 - val_acc: 0.9434
Epoch 7/10
2872/2872 [==============================] - 81s - loss: 0.0160 - acc: 0.9948 - val_loss: 0.2477 - val_acc: 0.9528
Epoch 8/10
2872/2872 [==============================] - 78s - loss: 0.0179 - acc: 0.9948 - val_loss: 0.2249 - val_acc: 0.9497
Epoch 9/10
2872/2872 [==============================] - 101s - loss: 0.0128 - acc: 0.9962 - val_loss: 0.2784 - val_acc: 0.9308
Epoch 10/10
2872/2872 [==============================] - 92s - loss: 0.0165 - acc: 0.9965 - val_loss: 0.2395 - val_acc: 0.9434
318/318 [==============================] - 2s
score = [0.23952163933957898, 0.94339622678996637]
```

Secondary result w/ `batch size = 54`. Note the worse effect relative to above batch size of `32`. 

```
Train on 2872 samples, validate on 318 samples
Epoch 1/10
2872/2872 [==============================] - 66s - loss: 0.3415 - acc: 0.8611 - val_loss: 0.0984 - val_acc: 0.9560
Epoch 2/10
2872/2872 [==============================] - 65s - loss: 0.1168 - acc: 0.9624 - val_loss: 0.1222 - val_acc: 0.9465
Epoch 3/10
2872/2872 [==============================] - 64s - loss: 0.0724 - acc: 0.9777 - val_loss: 0.1890 - val_acc: 0.9277
Epoch 4/10
2872/2872 [==============================] - 65s - loss: 0.0402 - acc: 0.9871 - val_loss: 0.2028 - val_acc: 0.9340
Epoch 5/10
2872/2872 [==============================] - 65s - loss: 0.0230 - acc: 0.9930 - val_loss: 0.1948 - val_acc: 0.9403
Epoch 6/10
2872/2872 [==============================] - 64s - loss: 0.0201 - acc: 0.9948 - val_loss: 0.2568 - val_acc: 0.9245
Epoch 7/10
2872/2872 [==============================] - 70s - loss: 0.0095 - acc: 0.9972 - val_loss: 0.3410 - val_acc: 0.9214
Epoch 8/10
2872/2872 [==============================] - 71s - loss: 0.0171 - acc: 0.9944 - val_loss: 0.3200 - val_acc: 0.9308
Epoch 9/10
2872/2872 [==============================] - 67s - loss: 0.0150 - acc: 0.9948 - val_loss: 0.1724 - val_acc: 0.9434
Epoch 10/10
2872/2872 [==============================] - 72s - loss: 0.0091 - acc: 0.9969 - val_loss: 0.2535 - val_acc: 0.9403
318/318 [==============================] - 2s

score = [0.25348289227757437, 0.94025156970294022]
```

Good links:
- on overfitting and train vs test accuracy: https://github.com/fchollet/keras/issues/877
- on evaluating your algorithm: http://machinelearningmastery.com/evaluate-performance-deep-learning-models-keras/

