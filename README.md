# Face_ID_project-repo

PROJECT TOPIC :FACE RECOGNITION PROGRAM
The purpose of this program is to detect faces in  pictures, videos and Live cameras as well as mood also.

Having understood the purpose of this program, I began by opening an image from my laptop, using python.  I proceeded with how to access  camera, pictures and videos, in python. When I could  this.

I got a data set containing Images and of people which I used to train the image recognition Model.
The data set contained in a 48 by 48 pixels. 28 709 images for the training set and 3 589.
The moods in it are:
0 = Angry
1 = Disgust
2 = Fear
3 = Happy
4 = Sad
5 = Supprise
6 = Neutral

PROJECT DESCRIPTION:
       It works by running the program in the Terminal or Command Line. When this is  done, the program will Load the already trained model from the .json file and add the weight , if there is no error, it wil Launch Open CV Library to open the Camera. While True,  the model run in the camera feed and uses haarcascade_frontalface_default.xml to detect the faces in the camera, and model, the mood in the face, and creates a green box, around it. And Finnally prints the detected mood. 

Source:
Kaggle
Name:FER 13 Dataset

LIBRARIES
1. Numpy
2. Keras
3. Open Cv
4. Pillow

Others:
Haarcascade_frontalface_default.xml

Requirements:
A good laptop withh a good speed. 


LESSONS LELARNED:
I have more about the capabiities of python, it's application in Image detection and machine learning.
I have learned some applications of face recogition works, especially facebook.