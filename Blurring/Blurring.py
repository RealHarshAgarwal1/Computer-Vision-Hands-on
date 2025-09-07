import os 
import cv2

img = cv2.imread(os.path.join('.','Blurring','Cat.jpg'))


k_size=7
img_blur = cv2.blur(img,(k_size,k_size))
Gaussan_blur = cv2.GaussianBlur(img,(k_size,k_size),3)
Median_blur = cv2.medianBlur(img,k_size)

cv2.imshow('image',img)
cv2.imshow("img_blur",img_blur)
cv2.imshow("Gaussian_blur",Gaussan_blur)
cv2.imshow("Median_blur",Median_blur)
cv2.waitKey(0)