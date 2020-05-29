import cv2

#Actually for now, what we will be just doing is drawing a rectangle accross all the faces which comes in the webcam. So we need a classifier which could classify and detect
#all the faces in each frame of the video of web cam

cam = cv2.VideoCapture(0) 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')#Created an object of haarcascade Classifier which helps in detection of the face in the image/Frame


while True:
    
    returnValue,Frame = cam.read() 

    if returnValue==False:
        continue 

    #Now we will get the coordinates of each face in the frame using the CascadeClassifier
    faces = face_cascade.detectMultiScale(Frame,1.3,5)
    #Here 1.3 is the scaling paramter and 5 is the number of neigbours. See about them below the code

    #Actually now variable 'faces' will contain the details of each face in the frame which include (x-coordinate of starting point of face,y-coordinate of starting point,
    #width of face, height of face). These will be present in the form of tuples


    #Drawing rectangle across faces in each frame
    for eachFace in faces:
        x_coordinate = eachFace[0]
        y_coordinate = eachFace[1]
        width = eachFace[2]
        height = eachFace[3]
        #Now we have to draw the rectance across this face
        #Now if we have coordinates of 2 opposite corners of a rectance, then we can draw a rectance in the frame using openCv and then show.
        #Obviously starting coordinates of the face are = (x_coordinate,y_coordinate) ,  Wherease ending coordinates of the face will be 
        #(x_coordinate + width , y_coordinate+ height). Therefore draw a rectangle using it
        cv2.rectangle(Frame ,(x_coordinate,y_coordinate),(x_coordinate + width , y_coordinate+ height),(255,0,0),2)
        #Here (255,0,0) refers to some RGB colour(colour by overlapping) --> Colour of the rectangle frame and 2 refers to the width of the rectangle in dp

    
    cv2.imshow('Video Frame',Frame)

    keyPressed = cv2.waitKey(1)
    if(keyPressed==ord('q')):
        break


cam.release() 
cv2.destroyAllWindows()



