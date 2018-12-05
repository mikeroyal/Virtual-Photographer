import FaceDetection
import cv2

def trackEyes(face):
    frame = face.getImage()
    eyeCascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    #eyes = eyeCascade.detectMultiScale(frame, 1.55, 5)
    eyes = eyeCascade.detectMultiScale(frame, 1.55, 5)
    print(len(eyes))#Testing
    if(len(eyes) >= 2): #True when no blinking
        return True
    else:
        return False
