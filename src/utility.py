import loader as ld
import trainer as tr
import tensorflow as tf
import cv2 as cv
import matplotlib.pyplot as plt
    
test_set = ld.load_images_from_file("..\\datasets\\age-detection\\test")

# This function trains a model and returns it along with the test set.
def train_new_model():
    # Obtain the train and valiation sets using the "loader" module.
    training_set = ld.load_images_from_file("..\\datasets\\age-detection\\train")
    validation_set = ld.load_images_from_file("..\\datasets\\age-detection\\validation")
    
    model = tr.train_model(training_set, validation_set)
    
    return model, test_set

# This function loads a trained model and returns it along with the test set.
def load_existing_model():
    path = "../models/cnn_80.model"
    model = ld.load_saved_model(path)

    return model, test_set

def evaluate(index, model):
    img = test_set[0][index].reshape(1, test_set[0][index].shape[0], test_set[0][index].shape[1], 1)
    print(img.shape)
    prediction = model.predict(img)
    answer = test_set[1][index]
    
    return prediction, answer

def evaluate_from_file(path, model):
    img = cv.imread(path, 0)
    img = img.reshape(1, img.shape[0], img.shape[1], 1)
    prediction = model.predict(img)
    
    return prediction

def evaluate_real_time(img, model):
    img = img.reshape(1, img.shape[0], img.shape[1], 1)
    prediction = model.predict(img)

    print(prediction)

def display_image(index):
    img = test_set[0][index]
    plt.imshow(img, cmap = "gray")
    plt.show()