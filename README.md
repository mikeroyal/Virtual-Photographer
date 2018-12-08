# Virtual Photographer

Authors: Scott Grether, Dustin Grady, Michael Royal

Scott: Wrote FaceDetection.py to recognize different facial regions (eyes, mouth, etc).

Dustin: Wrote ImageGetter.py, main.py and the SmileDetector code which Scott implemented into FaceDetection.py 

Michael: Wrote EyeTrack.py and provided a majority of our research during the development of the project.

Our project is the Virtual Photographer it deals with Face and Eye detection. So when the user runs the file Main.py it will start up the Program GUI and Webcam. 

Asking the user to take a snapshot of themselves by pressing the 'Space Bar'and then press the 'Esc' key to have 
the photo be analyzed. Once that is done the file ImageGetter.py retrieves that image saved to the system. 

The script FaceDetection.py which analyzes the face and tells the user whether or not they were smiling. 

It will then reference the script EyeTrack.py which tells the user whether or not their eyes blinked when they took the photo. 

EyeTrack will work with eye glasses if the environment your in has good lighting which is important to get good results from the 
detection program. 

Possible improvements: Have the program work for multiple people at the same time/ red-eye detection.

I hope your enjoy using Virtual Photographer because we sure had fun making it. 

<p align="center">
  <img alt="facialrecog" src="https://user-images.githubusercontent.com/18353476/28000092-614cec1c-64d8-11e7-94aa-3815395fa837.jpg">
</p>
