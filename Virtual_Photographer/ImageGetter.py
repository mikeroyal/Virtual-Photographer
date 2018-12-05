#Author: Dustin Grady
#Function: Takes pictures using webcam when the space bar is pressed and saves them to the directory for processing by other function
#Status: Working

import cv2
import cv

def getImage():
    cv2.namedWindow("Camera Preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    print "\n\n\n\n\nTaking photos.."

    while rval:
        cv2.imshow("Camera Preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(40) & 0xFF # & 0xFF is for 64-bit support
        if key == 27: #esc to exit
            break

        if key == 32: #Take photo with space bar
            cv.SaveImage("webcam.jpg", cv.fromarray(frame))
            #img = cv.LoadImage("webcam.jpg") # input image
getImage()
