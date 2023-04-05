import cv2
import os
import numpy as np

vidcap = cv2.VideoCapture("015.mp4")
success, image = vidcap.read()

path = "D:\CSE\CSE120\images"
img_array = []
count = 0

inputSize = (640, 360)

if (vidcap.isOpened()== False):
    print("Error opening video file")
  
while(vidcap.isOpened()):
      
# Capture frame-by-frame
    ret, frame = vidcap.read()
    
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', frame)
          
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
  
# Break the loop
    else:
        break

while success:
    try:
        # Capture video frame by frame
        success, image = vidcap.read()

        if(success == None or success == False):
            print("Incorrect size")
        else:

            # Resize the image frames
            resize = cv2.resize(image, inputSize)
            # Saving the frames with certain names
            cv2.imwrite("D:\CSE\CSE120\images\%04d.jpg" % count, resize)
            img_array.append(resize)
        
        # Closing the video by Escape button
            if cv2.waitKey(10) == 27:
                break
  
    # Incrementing the variable value by 1
        count += 1
    except Exception as e:
        print(str(e))

