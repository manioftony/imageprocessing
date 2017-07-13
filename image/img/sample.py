##########lets draw the line
# import numpy as np
# import cv2

# image = np.zeros((512,512,3),np.uint8)
# cv2.line(image,(0,0),(512,512),(255,127,0),5)
# cv2.imshow("blue line",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


###### lets draw rectangle line

# import numpy as np
# import cv2

# image = np.zeros((512,512,3),np.uint8)
# cv2.rectangle(image,(10,10),(300,250),(127,50,127),5)
# cv2.imshow("Rectangle",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

######### lets draw circle line
# import numpy as np
# import cv2


# image = np.zeros((512,512,3),np.uint8)
# cv2.circle(image,(350,350),100,(15,75,50),-1)
# cv2.imshow("Circle",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



######### lets draw polygan line

# import numpy as np
# import cv2
# image = np.zeros((512,512,3),np.uint8)
# # let is define four points
# pts = np.array([[10,50],[40,50],[90,200],[50,200],[12,12]],np.int32)
# pts = pts.reshape(-1,1,2)
# cv2.polylines(image,[pts],True,(0,0,255),3)
# cv2.imshow("Polygan",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import numpy as np
import cv2
image = np.zeros((512,512,3),np.uint8)
cv2.putText(image,"Hello World",(75,290),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)
cv2.imshow("Hello world",image)
cv2.waitKey(0)
cv2.destroyAllWindows()