import cv2
import numpy as np
import os
import knn as myKNN


#First Collect the data of all faces
############################################################

##Face data will contain each image in the form of numpy array and label will contain the class_id to which that image belongs to
face_data = []
labels = []



#We we will be giving id to each of the face we have in our data(i.e it will be just like the classes to which a particular quey x will
#belong too).  Now that class_id will be having correspondingly a name which would be stored in the 'name' dictionay. Therefore there might
#be many pictures of same face. Therefore they would be belonging to same class
class_id = 0
names = {}

dataset_path = './data/'

#This method will list all the files whicch will be there in this directory
for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        ##First Getting the Name of the person From This --- 
        ##fx will be like this if name is - name.npy. Therefore we can get the name by slicing
        name = fx[:-4]
        data_item = np.load(dataset_path + fx)
        
        face_data.append(data_item)
        print(data_item.shape)
        

        #Create labels for each image as classId in currentfx
        targetLabels = np.ones((data_item.shape[0],))
        targetLabels = class_id * targetLabels
        names[class_id] = name
        print(targetLabels.shape)

        #Now update the class_id, so that for the next file which maybe for another person, so that person's face images belongs to different classes
        class_id+=1
        labels.append(targetLabels)
        
        
        
##Now face_data,labels will be currently like this -->
#[ [data of images of classID 0 ],
#  [data of images of classID 1 ],
#  [data of images of classID 2 ]] i.e in each row , data of all images of users will be concatenated, Therefore seperate them ==> ans store
face_data = np.concatenate(face_data,axis = 0)
labels = np.concatenate(labels,axis = 0)
print(face_data.shape)
print(labels.shape)

#######################################################################################


cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_alt.xml')

while True:
    returnValue,Frame = cam.read()

    if returnValue==False:
        continue

    faces = face_cascade.detectMultiScale(Frame,1.3,5)

    if len(faces)==0:
        continue
        
        
    #Now let's show the name of each face in the data if comes on the screen
    for eachFace in faces:
        x,y,w,h = eachFace
        
        offset = 10
        face_section = Frame[y-offset : y+h+offset, x-offset : x+w+offset]
        face_section = cv2.resize(face_section,(100,100)) #It will be in the shape (100,100,3)
        
        #Find the predicted label for the this query x
        predictedLabel = myKNN.knn(face_data,labels,face_section.flatten())
        
        ##Therefore now getting the predicted name from the predicted Label
        namesOfPerson = names[int(predictedLabel)]
        
        cv2.putText(Frame,namesOfPerson,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA) #1 is the size of the text whereas (255,0,0) is the colour of the text
        cv2.rectangle(Frame,(x,y),(x+w,y+h),(0,255,255),2)
    
    
    cv2.imshow('Video Frame',Frame)

    keyPressed = cv2.waitKey(1)
    if(keyPressed==ord('q')):
        break


cam.release()
cv2.destroyAllWindows()








































