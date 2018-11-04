import os, glob

path = "UTKFace"


for image in glob.glob("{0}/*".format(path)):
    temp_name = os.path.split(image)[-1]
    age = 0
    if temp_name[1] == "_":
        #single digit
        age = temp_name[0]

    elif temp_name[2] == "_":
        #two digits
        age = temp_name[0] + temp_name[1]
            
    elif temp_name[3] == "_":
        #three digits
        age = temp_name[0] + temp_name[1] + temp_name[2]
            
    index = 0   
    new_name = str(age) + "_" + str(index) + ".jpg"
    while(os.path.isfile(path + "\\" + new_name)):
        index = index + 1
        new_name = str(age) + "_" + str(index) + ".jpg"
                   
    os.rename(image, path + "\\" + new_name)

    
