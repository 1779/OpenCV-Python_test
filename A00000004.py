import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[50:100, 50:100] = [0,0,0]

watch_face = img[150:250, 150:250]
img[0:100, 0:100] = watch_face
#print(roi)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
