#1. capture image
#2. apply effect
#3. effects: gray, canny, rgb, hsv
#4. combine 4 of them -> collage
#5. show 

import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)
    
ret, frame = capture.read()
if  ret:
       

    #resize
    resized_img = cv.resize(frame, (400,400), interpolation=cv.INTER_AREA)
    #gray
    gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    #canny
    canny = cv.Canny(resized_img, 125, 175)
    canny = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
                #rgb
    rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)
                #hsv
    hsv = cv.cvtColor(resized_img, cv.COLOR_BGR2HSV)
                #combine
    row1 = np.hstack((gray, canny))
    row2 = np.hstack((hsv, rgb))
    collage = np.vstack((row1, row2))
    cv.imshow("collage", collage)
else:
    print("failed")


cv.waitKey(0)
capture.release()
cv.destroyAllWindows()
    