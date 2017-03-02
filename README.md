# Convolutional Neural Networks for DNA Sequence Classification

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

Good links:
- on overfitting and train vs test accuracy: https://github.com/fchollet/keras/issues/877
- on evaluating your algorithm: http://machinelearningmastery.com/evaluate-performance-deep-learning-models-keras/

