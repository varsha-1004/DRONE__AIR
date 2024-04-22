import cv2
import time

videocapture= cv2.VideoCapture("nvarguscamerasrc sensor-id=0 sensor-mode=4 ! "
        "video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, framerate=(fraction)60/1 ! "
        "nvvidconv flip-method=0 ! "
        "video/x-raw, width=(int)1280, height=(int)720, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink")
for i in range(2):
    k=0
    j=0
    while True:
        ret,frame=videocapture.read()
        k+=1
        if k==42: 
            cv2.imwrite("pande/"+str(i)+".jpg",frame)
            j+=1
        if j==1:
            break
        


        
