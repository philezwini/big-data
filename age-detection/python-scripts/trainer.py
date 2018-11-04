import tensorflow as tf
from keras.utils import np_utils

def train_model(training_set, validation_set):
    train_x = training_set[0].reshape(training_set[0].shape[0], 200, 200, 1)
    val_x = validation_set[0].reshape(validation_set[0].shape[0], 200, 200, 1)
    
    #print(train_x.shape)
    #print(val_x.shape)
    #print("--------------")
    #print(train_x)
    #print("-----------------")
    #print(val_x)
    
    train_y = training_set[1]
    val_y = validation_set[1]
    
    #One-hot encode the lables so that they are compatible with softmax activation.
    train_y = np_utils.to_categorical(train_y, 5)
    val_y = np_utils.to_categorical(val_y, 5)

    # build the model.
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Convolution2D(32, (3, 3), input_shape = (loader.IMAGE_DIMS[0], loader.IMAGE_DIMS[1], 1)))
    model.add(tf.keras.layers.Activation("relu"))
    model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2)))

    model.add(tf.keras.layers.Convolution2D(32, (3, 3), input_shape = (loader.IMAGE_DIMS[0], loader.IMAGE_DIMS[1], 1)))
    model.add(tf.keras.layers.Activation("relu"))
    model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2)))

    model.add(tf.keras.layers.Convolution2D(32, (3, 3), input_shape = (loader.IMAGE_DIMS[0], loader.IMAGE_DIMS[1], 1)))
    model.add(tf.keras.layers.Activation("relu"))
    model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2)))

    model.add(tf.keras.layers.Flatten())

    #Fully connected layer.
    model.add(tf.keras.layers.Dense(64))
    model.add(tf.keras.layers.Activation("relu"))

    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(5))
    model.add(tf.keras.layers.Activation("softmax"))

    model.compile(loss = "binary_crossentropy", optimizer = "rmsprop", metrics = ["accuracy"])
    
    model.fit(train_x,
              train_y,
              epochs = 3,
              verbose = 1,
              validation_data = (val_x, val_y))

    model.save("../models/cnn.model")
    print("training complete.")
    return model
