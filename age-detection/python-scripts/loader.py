import cv2
import glob
import os
import numpy
import tensorflow as tf

IMAGE_DIMS = (200, 200) # tuple for storing the image dimensions.
MIN_AGE_CAT = 1
MAX_AGE_CAT = 5

# This function returns the age range/category in [MIN_AGE_CAT, MAX_AGE_CAT] that the person
# in the image belongs to.
def determine_age_range(char_array):
    #Check to see where the underscore is and assign an appropriate age.
    if char_array[1] == '_':
        return 0
    elif char_array[2] == '_':
        if char_array[1] == '0':
            return int(char_array[0]) - 1
        elif char_array[1] != '0':
            return (int(char_array[0]) - 1) + 1
    else:
        raise ValueError("Invalid position for underscore.")

def load_images_from_file(path):
    return_set = []
    labels = []
    images = []
    image_urls = []
    
    # Extracting the names of the images and taking only the first character.
    # of each name. These are the ages of the people in the respective photos.
    # We are going to use the ages of the subjects to generate our label array
    # (i.e. 1 means that the subject's age is between i [inclusive] and 10 [inclusive].
    if os.path.isdir(path):
        for image in glob.glob("{0}/*".format(path)):
            image_urls.append(image)
            temp_name = os.path.split(image)[-1]
            labels.append(determine_age_range(temp_name))
    else:
        print(path + " is not a valid directory")
     
    # Extract the images from the file system and convert them to numpy arrays.
    for url in image_urls:
        image = cv2.imread(url, 0) # read in image as numpy array.
        images.append(image) # add image to array of images.
    
    images = numpy.array(images)
    labels = numpy.array(labels)
    
    return_set.append(images)
    return_set.append(labels)
    
    return return_set

def load_saved_model(path):
    return tf.keras.models.load_model(path)
    
