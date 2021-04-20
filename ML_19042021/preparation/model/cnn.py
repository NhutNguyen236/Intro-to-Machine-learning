#Importing the necessary packages
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
#Importing the CNN related layers as described in Chapter 2
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
#Loading data from Keras datasets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#Defining the height and weight and number of samples
#Each Image is a 28 x 28 with 1 channel matrix
training_samples, height, width = x_train.shape
testing_samples,_,_ = x_test.shape
print("Training Samples:",training_samples)
print("Testing Samples:",testing_samples)
print("Height: "+str(height)+" x Width:"+ str(width))

#Lets have a look at a sample image in the training data
plt.imshow(x_train[0],cmap='gray', interpolation='none')

#We now have to engineer the image data into the right form
#For CNN, we would need the data in Height x Width X Channels
# form Since the image is in grayscale, we will use channel = 1

channel = 1
x_train = x_train.reshape(training_samples, height,
width,channel).astype('float32')
x_test = x_test.reshape(testing_samples, height, width,
channel).astype('float32')
#To improve the training process, we would need to standardize
# or normalize the values We can achieve this using a simple
# divide by 256 for all values
x_train = x_train/255
x_test =x_test/255
#Total number of digits =10
target_classes = 10
# numbers 0-9, so ten classes
n_classes = 10
# convert integer labels into one-hot vectors
y_train = np_utils.to_categorical(y_train, n_classes)
y_test = np_utils.to_categorical(y_test, n_classes)
#Designing the CNN Model
model = Sequential()
model.add(Conv2D(64, (5, 5), input_shape=(height,width ,1),
activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(n_classes, activation='softmax'))
# Compile model
model.compile(loss='categorical_crossentropy',
optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(x_train, y_train, validation_data=(x_test, y_test),
epochs=10, batch_size=200)

metrics = model.evaluate(x_test, y_test, verbose=0)
for i in range(0,len(model.metrics_names)):
 print(str(model.metrics_names[i])+" = "+str(metrics[i]))
