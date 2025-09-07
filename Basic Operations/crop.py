# Cropping

import os
import cv2

img = cv2.imread(os.path.join('.','Basic Operations','Cat.jpg'))

print(img.shape)

cropped_img = img[200:450,220:500]

cv2.imshow('img',img)
cv2.imshow('cropped img',cropped_img)
cv2.waitKey(0)