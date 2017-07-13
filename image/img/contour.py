import numpy as np
import cv2
import math

class ShapeRecong():
          def __init__(self,img):
               self.img = img
          def preprocessing(self):
               lower = np.array([0,0,0],dtype=np.uint8)
               upper = np.array([12,12,12],dtype=np.uint8)
               mask = cv2.inRange(self.img,lower,upper)
               cv2.imshow("mask",mask)
               (flags,contours,h) =    cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
               return contours


img = cv2.imread("/home/manikandan/Desktop/image/image/orginal.jpg")
shape =ShapeRecong(img)
contours = shape.preprocessing()

cv2.imshow('asasa',img)
cv2.waitKey(0)
cv2.destroyAllWindows()