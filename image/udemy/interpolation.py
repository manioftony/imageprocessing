# image cropping 


import cv2
import numpy as np


image = cv2.imread("../image/shape.jpg")

height,width = image.shape[:2]
print height
print width

# lets pixel cordinate top left cropping

start_row,start_col = int(height*.25),int(width*.25)

# lets get the ending pixel coordinate(bottom right)

end_row,end_col =  int(height*.75),int(width*.75)

# simple using index croping 

cropped = image[start_row:end_row,start_col:end_col]

cv2.imshow("orginal image",image)
cv2.waitKey(0)
cv2.imshow("crapped image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()









