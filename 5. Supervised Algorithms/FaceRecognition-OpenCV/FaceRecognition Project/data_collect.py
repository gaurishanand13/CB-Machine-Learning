import cv2
import numpy as np

"""
Here we will store only the image of face(in frame) in the form on numpy array. We will just store the face cut of the face and ignore all other data like hands and all. Because when comparing data of the face while testing , it needs to predict the name of the person, so in that it case it should compare only the pixels of the face. So we would be saving the data of only pixel Values inside the box
"""


"""
Note - Though we will be getting a frame picture after every 1 milli second(+ sum Code ExecutionTime too). But we should not consider taking so much frames(images) of the same person(Space Issue can be there) . Instead we will try taking the face in every 10th Face . Skip will maintain that. Every time we detect faces in the frame , skip will be incremented
"""
skip = 0



dataset_path = './data/'

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_alt.xml')
file_name = input("Enter the name of the person : ")
face_data_list = [] ##It will store our array of each face captured. Where each face will itself be a list of data of an image



def compare(myTuple):
    width = myTuple[2]
    height = myTuple[3]
    return width*height
    
    
    

while True:
    returnValue,Frame = cam.read()

    if returnValue==False:
        continue

    faces = face_cascade.detectMultiScale(Frame,1.3,5)

    if len(faces)==0:
        continue

    #Now sort the faces by the size of the image because we will be storing only the largest size face in the frame captured(--> This will be used when there are)
    #mulitple images in the frame
    faces = sorted(faces,key = compare) #Since area of the face = (height*width) , Therefore we should sort on the basis of this area which is present



    highestAreaFace = faces[len(faces)-1]
    x= highestAreaFace[0]
    y = highestAreaFace[1]
    w = highestAreaFace[2]
    h = highestAreaFace[3]

    cv2.rectangle(Frame,(x,y),(x+w,y+h),(255,0,0),2)
    #Extract (Crop out of the required Face ) : Region of the interest  --> Let's take some padding while cropping this frame. Let that padding be of 10px
    #Generally this padding is called offset
    offset = 10
    
    #Note - we already know Frame is a type of numpy array, therefore slicing is allowed in this-
    face_section = Frame[y-offset : y+h+offset , x-offset:x+w+offset ] #It will give us the result in the form of numpy array
    
    #Therefore now we will make the size of each numpy array same. So that when pixels are compared in future to a face, size of all photos should be same to be compared. As discussed it will make the height and width resize.
    face_section = cv2.resize(face_section,(100,100)) #It will reduce the size of the image, i.e make the image of size 100x100
    #Now we will save this face section only after every 10 faces
    skip = skip + 1

    if skip%10==0:
        print(type(face_section),len(face_section))
        face_data_list.append(face_section)

    
    cv2.imshow('Video Frame',Frame)

    keyPressed = cv2.waitKey(1)
    if(keyPressed==ord('q')):
        break


cam.release()
cv2.destroyAllWindows()



#Now after the web cam is closed, let's insert this data in the form of numpy array i.e converting a list of image(numpy array) to a numpy array of image(numpy array)
face_data_list = np.asarray(face_data_list)
print(face_data_list.shape) ##Output will be (face_data_list.size,100,100,3)


#Actually for now, each image will be a numpy array of 100x100x3 --> Where (100x100) represents the total pixels in each channel and 3 represents the total number of
#channels which are 3(RGB). Which can be seen with this  shape.
print(type(face_data_list[0]))
print(face_data_list[0].shape)
#But we will be storing the data of each image in the form of 1D numpy array , so let's reshape it
face_data_list = face_data_list.reshape((face_data_list.shape[0],-1)) #We have put -1 like that, but we know that number of columns will be 100*100*3 for each image
#to be inserted in a row

np.save(dataset_path + file_name + '.npy',face_data_list)
print('Data Saved Successfully')
print(face_data_list.shape)































