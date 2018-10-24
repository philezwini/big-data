import src.data_parser as parser
import cv2

print("testing data_parser...")
parser.load_data("New Load.")
print("Done.")

img = cv2.imread("../datasets/cats vs dogs/train/cat.5000.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("read image.")

