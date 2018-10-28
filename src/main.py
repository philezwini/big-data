import loader
import tensorflow as tf

# Obtain the train and valiation sets using the "loader" module.
training_set = loader.load_images_from_file("../datasets/age-detection/train/")
validation_set = loader.load_images_from_file("../datasets/age-detection/validation/")

# build the model.
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Convolution2D(200, 3, 3, input_shape = (loader.IMAGE_DIMS[0], loader.IMAGE_DIMS[1], 3)))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2)))


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Convolution2D(200, 3, 3, input_shape = (loader.IMAGE_DIMS[0], loader.IMAGE_DIMS[1], 3)))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2)))

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Convolution2D(200, 3, 3, input_shape = (loader.IMAGE_DIMS[0], loader.IMAGE_DIMS[1], 3)))
model.add(tf.keras.layers.Activation("relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size = (2, 2)))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64))
model.add(tf.keras.layers.Activation("relu"))

model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(9))
model.add(tf.keras.layers.Activation("softmax"))

model.compile(loss = "binary_crossentropy", optimizer = "rmsprop", metrics = ["accuracy"])

train_x = training_set[0].reshape(-1)
train_y = training_set[1]

validation_x = validation_set[0].reshape(-1)
validation_y = validation_set[1]


model.fit_generator( generator = ({"input" : train_x}, {"target" : train_y}),
          epochs = 3,
          validation_data = ({"input" : validation_x}, {"target" : validation_y}),
          steps_per_epoch = 500,
          verbose = 2,
          )
