import numpy
import cv2
img = cv2.imread('/home/manikandan/Desktop/image/image/god.png',cv2.IMREAD_COLOR)
# cv2.line(img,(0,0),(1,1),(255,0,0),15)
cv2.rectangle(img,(1,1),(120,30),(0,255,0),5)
cv2.imshow('asas',img)
cv2.waitKey(0)
cv2.destroyAllWindows()