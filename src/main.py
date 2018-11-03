import loader
import trainer
import tensorflow as tf
import cv2 as cv

model = tf.keras.models.load_model("../models/cnn.model")
img = loader.load_test_img("../datasets/age-detection/test/42_51.jpg")
print(model.predict(img))
