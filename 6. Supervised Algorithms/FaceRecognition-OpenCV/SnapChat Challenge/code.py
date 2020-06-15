import cv2
import numpy as np


cam = cv2.VideoCapture(0)

mustacheImage = cv2.imread('mustache.png')

front_eyes_classifier = cv2.CascadeClassifier('frontalEyes35x16.xml')
nose_classifier = cv2.CascadeClassifier('Nose18x15.xml')
face_classifier = cv2.CascadeClassifier('../haarcascade_frontalface_alt.xml')

flag = False
while True:
    returnValue,Frame = cam.read()

    if returnValue==False:
        continue
        
    gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    eyes = front_eyes_classifier.detectMultiScale(gray)
    
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if len(eyes) is not 0:
        for eacheye in eyes:
            ex,ey,ew,eh = eacheye
            glassesImage = cv2.imread('glasses.png')
            print(ew,eh)
            glassesImage = cv2.resize(glassesImage,(int(ew),int(eh)))
            print(glassesImage.shape)
            print(Frame.shape)
            print(ex,ex+ew,ey,ey+eh)
            flag = True
            Frame[ey : ey + eh,ex : ex + ew] = glassesImage
            
        
#    for eachFace in faces:
#        x,y,w,h = eachFace
#        cv2.rectangle(Frame,(x,y),(x+w,y+h),(0,255,255),2)
#        face_section = gray[y:y+h, x:x+w]
#
#        #offset = 10
        
        
        
                #cv2.rectangle(Frame,(ex,ey),(ex+ew,ey+eh),(0,255,255),1)
            
#        nose = nose_classifier.detectMultiScale(face_section)
#        if len(nose) is not 0:
#            for eachNose in nose:
#                nx,ny,nw,nh = eachNose
#                nx = x + nx
#                ny = y + ny
#                mustacheImage = cv2.resize(mustacheImage,(int(nw),int(nh)))
#                print(mustacheImage.shape)
#                print(Frame.shape)
##                Frame[nx:nx + nw,ny:ny + nh] = mustacheImage
#                #cv2.rectangle(Frame,(nx,ny),(nx+nw,ny+nh),(0,255,255),2)
        
        
        
    cv2.imshow('Video Frame',Frame)

    keyPressed = cv2.waitKey(1)
    if(keyPressed==ord('q')):
        break


cam.release()
cv2.destroyAllWindows()









































