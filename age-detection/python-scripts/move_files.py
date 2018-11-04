import shutil as sh
import os

def move_to_train():
    max_img_count = 50
    max_age = 50

    current_age = 13
    img_counter = 10
    
    source_path = "UTKFace\\"
    dest_path = "train\\"

    while current_age <= max_age:
        while img_counter < max_img_count:
            img_name = str(current_age) + "_" + str(img_counter) + ".jpg"
            sh.move(source_path + img_name, dest_path + img_name)
            img_counter += 1

        current_age += 1
        img_counter  = 0

def move_to_validation():
    max_img_count = 20
    max_age = 50

    current_age = 1
    img_counter = 0
    
    source_path = "train\\"
    dest_path = "validation\\"

    while current_age <= max_age:
        while img_counter < max_img_count:
            img_name = str(current_age) + "_" + str(img_counter) + ".jpg"
            sh.move(source_path + img_name, dest_path + img_name)
            img_counter += 1

        current_age += 1
        img_counter  = 0


def move_to_test():
    max_img_count = 13
    max_age = 50

    current_age = 11
    img_counter = 0
    
    source_path = "UTKFace\\"
    dest_path = "test\\"

    while current_age <= max_age:
        while img_counter < max_img_count:
            img_name = str(current_age) + "_" + str(img_counter + 51) + ".jpg"
            sh.move(source_path + img_name, dest_path + img_name)
            img_counter += 1

        current_age += 1
        img_counter  = 0
        
move_to_test()
