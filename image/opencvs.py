# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv2.imread('/home/manikandan/Desktop/mani.jpg',0)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()



import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/manikandan/Desktop/mani.jpg',0)
img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



# import tensorflow as tf
# import Image ,numpy as np


# filename_queue = tf.train.string_input_producer(['/home/manikandan/Desktop/games.jpg']) #  list of files to read

# reader = tf.WholeFileReader()
# key, value = reader.read(filename_queue)

# my_img = tf.image.decode_png(value) # use png or jpg decoder based on your files.

# init_op = tf.initialize_all_variables()
# with tf.Session() as sess:
#   sess.run(init_op)

#   # Start populating the filename queue.

#   coord = tf.train.Coordinator()
#   threads = tf.train.start_queue_runners(coord=coord)

#   for i in range(1): #length of your filename list
#     image = my_img.eval() #here is your image Tensor :) 

#   print(image.shape)
#   Image.fromarray(np.asarray(image)).show()

#   coord.request_stop()
#   coord.join(threads)