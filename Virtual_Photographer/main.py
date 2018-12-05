#Author Dustin Grady
#Function: Program flow/ user IO
#Status: Finished/ Working
#Github: https://github.com/sgrether/Project-2/tree/D-Features

#Print program name + instructions
print("__   __ _       _                _                                   ")
print("\ \ / /(_) _ _ | |_  _  _  __ _ | |                                  ")
print(" \ V / | || '_||  _|| || |/ _` || |                                  ")
print("  \_/  |_||_|   \__| \_,_|\__,_||_|                                  ")
print(" ___  _          _                                _                  ")
print("| _ \| |_   ___ | |_  ___  __ _  _ _  __ _  _ __ | |_   ___  _ _     ")
print("|  _/| ' \ / _ \|  _|/ _ \/ _` || '_|/ _` || '_ \| ' \ / -_)| '_|    ")
print("|_|  |_||_|\___/ \__|\___/\__, ||_|  \__,_|| .__/|_||_|\___||_|      ")
print("                          |___/            |_|                       ")
print("       __     __   _                                                 ")
print("__ __ /  \   /  \ / |                                                ")
print("\ V /| () |_| () || |                                                ")
print(" \_/  \__/(_)\__/ |_|                                                ")
print('\n Press space to capture a photo, and escape to analyze it')

import FaceDetection
import EyeTrack
from ImageGetter import getImage

noGoodPicture = False #Used for program flow

while noGoodPicture == False: #Continue until good picture is found

    face = FaceDetection.Face('webcam.jpg')
    smile = FaceDetection.findSmile(face)
    eyes = EyeTrack.trackEyes(face)

    if(smile == True and eyes == False):
        print('It looks like you were blinking')
        print('Press space to try taking the picture again')
        getImage()


    if(smile == False and eyes == True):
        print('Why so serious? Try smiling :D')
        print('Press space to try taking the picture again')
        getImage()


    if(smile == False and eyes == False):
        print('Wake up sleepy face! (No smile or eyes detected)')
        print('Press space to try taking the picture again')
        getImage()


    if(smile == True and eyes == True):
        print('That looks like a great picture, good work :D')
        noGoodPicture = True #Set to true
