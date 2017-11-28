import numpy as np
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
import os
import pandas as pd

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

for n in range(1,6):
    cifar_dict = unpickle('cifar-10-batches-py/data_batch_'+str(n))
    #build a single structure containing the data matrix X, and the target column vector Y
    if n == 1:
        X_train = np.array(cifar_dict[b'data'])
        y_train = np.array(cifar_dict[b'labels'])
    else:
        X_train = np.concatenate([X_train, cifar_dict[b'data']], axis=0)
        y_train = np.concatenate([y_train, cifar_dict[b'labels']], axis=0)

#X_train.shape, y_train.shape

cifar_dict = unpickle('cifar-10-batches-py/test_batch')
X_test = np.array(cifar_dict[b'data'])
y_test = np.array(cifar_dict[b'labels'])

class_names_dict = unpickle('cifar-10-batches-py/batches.meta')
readable = lambda nam: str(nam)[2:-1]

class_names_list = []
for name in class_names_dict[b'label_names']:
    class_names_list.append(str(name)[2:-1])
    
#class_names_list
def transform_cifar_images(images):
    transformed = []
    for image in images:
        transformed_image = image.reshape(3,32,32).transpose(1,2,0)
        transformed.append(transformed_image)
         
    return np.array(transformed)
X_train = X_train.astype('float32')
X_train /= 255
X_test = X_test.astype('float32')
X_test /= 255

X_train = transform_cifar_images(X_train)
X_test = transform_cifar_images(X_test)

print("X_train: {}, y_train: {}".format(X_train.shape, y_train.shape))
print("X_test: {}, y_test: {}".format(X_test.shape, y_test.shape))
print("Class labels: {}".format(class_names_list))