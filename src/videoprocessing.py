import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

import utility as util

MAX_INTERVAL = 15 # the amount of iterations to wait for before feeding a frame to the cnn.
cnn, test_set = util.load_existing_model() # Get the trained cnn and the test set.

# This function takes in an array generated by a softmax activation as an argument.
# The return value is an age class from 1 - 5, where 1 = [1, 10]; 2 = [11. 20],
# 3 = [21, 30]; 4 = [31, 40]; 5 = [41, 50];
def evaluate_prediction(prediction):
    # Find the maximum value.
    age = -1.0
    print(prediction[0])
    return
    for x in prediction[0]:
        print(x)
        if x > age:
            age = x
            
    return age

    
# This function records a video from the webcam and extracts frames from it.
# Frames are extracted at MAX_INTERVAL intervals.
# Each frame is converted to a grayscale face image of 200x200 dimensions.
# The cropped frames are then sent to a convolutional neural network in order to predict
# the subject's age.
def analyze_video():
    
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml") # We are using haar cascades to highlight the face in an image for convenience.
    cap = cv.VideoCapture(0) #Captures video input from the webcam of the computer.
    wait = 0
    
    while True:
        ret, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cropped_img = gray #We are using a grayscale version of the image in order to make predictions using the cnn.

        # After finding the haar cascade of the face, we will use it to reproduce a 200x200 face image
        # that we can feed to the cnn.
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:

            # Adjust the parameters in order to efficiently crop the image.
            new_y = (y - 20)
            new_x = (x - 20)
            new_w = (w + 20)
            new_h = (h + 20)

            # Only update the cropped_img variable if the new dimensions are valid.
            if(new_x >= 0 & new_y >= 0):
                cv.rectangle(gray,  (new_x, new_y), (new_x + new_w, new_y + new_h), (255, 0, 0), 2)
                cropped_img = cropped_img[new_y:new_y + new_h, new_x:new_x + new_w]
            else:
                cv.rectangle(gray,  (x, y), (x + w, y + h), (255, 0, 0), 2)

            cropped_img = cv.resize(cropped_img, (200, 200)) # Resize the cropped image to 200x200.

        cv.imshow("gray", img)
        cv.imshow("cropped", cropped_img)
    
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

        #Make predictions after 15 frame-intervals
        if(wait == 15):
            cv.imwrite("capt_" + str(wait) + ".jpg", cropped_img)
            prediction = util.evaluate_real_time(cropped_img, cnn)
            #print(evaluate_prediction(prediction))
            wait = 0
            
        wait += 1

    cap.release()
    cv.destroyAllWindows()

analyze_video()
