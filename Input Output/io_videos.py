import os
import cv2

# read video

video_path = os.path.join(".","Input Output","Waterfall.mp4")
video = cv2.VideoCapture(video_path)

# Visualize video 

ret = True
while ret:
  ret,frame = video.read()

  if ret:
    cv2.imshow('frame',frame)
    cv2.waitKey(45)

# Release resources
video.release()
cv2.destroyAllWindows()