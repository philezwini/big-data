import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

import utility as util
import os

MAX_INTERVAL = 15 # the amount of iterations to wait for before feeding a frame to the cnn.
cnn, test_set = util.load_existing_model() # Get the trained cnn and the test set.

# This function takes in an array generated by a softmax activation as an argument.
# The return value is an age class from 1 - 5, where 1 = [1, 10]; 2 = [11. 20],
# 3 = [21, 30]; 4 = [31, 40]; 5 = [41, 50];
def evaluate_prediction(prediction):
    # Find the maximum value.
    age = -1.0
    index = -1
    top_two_predictions = []

    for i in range(2):
        found = False
        for t_index, t_age in enumerate(prediction[0]):
            if (t_age > age):
                for (a, i) in top_two_predictions:
                    if (i == t_index):
                        found = True
                        
                if (found == False):
                    age = t_age
                    index = t_index
                
        top_two_predictions.append((age, index))
        age = -1.0
        index = -1
        
    return top_two_predictions

    
# This function records a video from the webcam and extracts frames from it.
# Frames are extracted at MAX_INTERVAL intervals.
# Each frame is converted to a grayscale face image of 200x200 dimensions.
# The cropped frames are then sent to a convolutional neural network in order to predict
# the subject's age.
def analyze_video():
    cr_y = 0
    cr_x = 0
    cr_w = 0
    cr_h = 0
    
    face_cascade = cv.CascadeClassifier("../haar-cascades/haarcascade_frontalface_default.xml") # We are using haar cascades to highlight the face in an image for convenience.
    cap = cv.VideoCapture(0) #Captures video input from the webcam of the computer.
    cropped_img = np.zeros((480, 640), dtype = "i")
    wait = 0
    
    while True:
        ret, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        if(cr_x < 0) | (cr_y < 0) | (cr_w <= 0) | (cr_h <= 0):
            cropped_img = gray #We are using a grayscale version of the image in order to make predictions using the cnn.

        # After finding the haar cascade of the face, we will use it to reproduce a 200x200 face image
        # that we can feed to the cnn.
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            # Adjust the parameters in order to to get the whole face.
            cr_y = (y - 20)
            cr_x = (x - 20)
            cr_w = (w + 20)
            cr_h = (h + 20)

            # Only update the cropped_img variable if the new dimensions are valid.
            if(cr_x >= 0) & (cr_y >= 0):
                cv.rectangle(img,  (cr_x, cr_y), (cr_x + cr_w, cr_y + cr_h), (255, 0, 0), 2)
                cropped_img = gray[cr_y:cr_y + cr_h, cr_x:cr_x + cr_w]
                
            else:
                cr_y = y
                cr_x = x
                cr_w = w
                cr_h = h
                
                cv.rectangle(img,  (cr_x, cr_y), (cr_x + cr_w, cr_y + cr_h), (255, 0, 0), 2)
                cropped_img = gray[cr_y:cr_y + cr_h, cr_x:cr_x + cr_w]

            cropped_img = cv.resize(cropped_img, (200, 200)) # Resize the cropped image to 200x200.
        
        cv.imshow("gray", img)
        cv.imshow("cropped", cropped_img)
    
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

        #Make predictions after MAX_INTERVAL frame-intervals
        if wait == MAX_INTERVAL:
            prediction = util.evaluate_real_time(cropped_img, cnn)
            p = evaluate_prediction(prediction)
            print(p)
            wait = 0
            
        wait += 1

    cap.release()
    cv.destroyAllWindows()

analyze_video()
