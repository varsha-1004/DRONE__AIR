
import cv2
sensor_id=0
capture_width=1280
capture_height=720
framerate=120
flip_method=0
display_width=640
display_height=480
video_capture = cv2.VideoCapture("nvarguscamerasrc sensor-id=%d ! "
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        ), cv2.CAP_GSTREAMER)
if(video_capture.isOpened):
        # Under GTK+ (Jetson Default), WND_PROP_VISIBLE does not work correctly. Under Qt it does
        # GTK - Substitute WND_PROP_AUTOSIZE to detect if window has been closed by user
    #while(True):
    #    ret,frame=video_capture.read()
    #    cv2.imshow("Hell", frame)
    #    if cv2.waitKey(27) & 0xFF==ord("q"):
    #       break       
    ret,frame=video_capture.read()
    cv2.imshow("Hell", frame)
    cv2.waitKey(0)
    #if cv2.waitKey(27) & 0xFF==ord("q"):
    #break 
video_capture.release()
cv2.destroyAllWindows()



