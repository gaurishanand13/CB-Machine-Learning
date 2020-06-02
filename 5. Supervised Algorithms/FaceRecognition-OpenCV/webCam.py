import cv2


# myImage = cv2.imread('dogsImage.jpeg') 
# cv2.imshow('Dog Image',myImage)
# x = cv2.waitKey(10000) 
# print(x)
# cv2.destroyAllWindows()



cam = cv2.VideoCapture(0) #0 is the id of the webCam Recorder which is to be used. By default if we uses
#inbuild cam(Default Webcam), then its id = 0. If the system has more external cams, then you can mention that 
#webcam id in this(whichever cams id needed to be used)

#Now note - A video is just a series/collection of frames where each frame is just an image. These frames are displayed
#like that one after the another so fast, that it looks like a video

while True:
    #cam.read() returns 2 values. First one Tells us whether the cam was successful in capturing the frame or not.
    #If the cam was not successful in capturing that frame , then returnValue will be returned False
    returnValue,Frame = cam.read() #2nd values is the returned Frame which is captured by the cam
    
    #Apart from this coloured Webcam, let's show the webcam in black and white too.
    grayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    
    if returnValue==False:
        continue #Then in this case, don't need to display the frames, it can happen in some of the cases
    
    
    
    #Let's just show the current frame captured i.e updated Frame
    cv2.imshow('Video Frame',Frame)
    cv2.imshow('Black And White Frame',grayFrame)
    
    
    

    #This will make it wait for 1 milli second to check for a key pressed and if the key pressed is q, then it will exit from this loop
    keyPressed = cv2.waitKey(1)
    if(keyPressed==ord('q')):
        break


cam.release() #It will release the webcam so that CPU can use it to allocate to another application if required
cv2.destroyAllWindows()
