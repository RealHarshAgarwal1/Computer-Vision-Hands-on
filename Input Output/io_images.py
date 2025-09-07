import os
import cv2

# Read Image

image_path = os.path.join('.','Input Output','Bird.jpg')
img = cv2.imread(image_path)

# Write Image

cv2.imwrite(os.path.join('.','Input Output','Bird_out.jpg'),img)

# Visualize the image

cv2.imshow('image',img)
cv2.waitKey(0) 