import cv2
import glob
import os
import numpy

IMAGE_DIMS = (200, 200) # tuple for storing the image dimensions.

def build_name(char_array):
    name = ""
    for char in char_array:
        name += char

    return name

def load_images_from_file(path):
    return_set = []
    labels = []
    images = []
    image_names = []
    
    # Extracting the names of the images and taking only the first character.
    # of each name. These are the ages of the people in the respective photos.
    # We are going to use the ages as our lables (i.e. 1 means that the
    # subject's age is between i [inclusive] and 10 [inclusive].
    if os.path.isdir(path):
        for image in glob.glob("{0}/*".format(path)):
            temp_name = os.path.split(image)[-1]
            labels += temp_name[0]
            image_names.append(build_name(temp_name))
    else:
        print(path + " is not a valid directory")
     
    # Extract the images from the file system and convert them to numpy arrays.
    for name in image_names:
        url = path + "/" + name # construct relative path using image name.
        image = cv2.imread(url) # read in image as numpy array.
        images.append(image) # add image to array of images.


    return_set.append(images)
    return_set.append(labels)
    return numpy.array(return_set)
