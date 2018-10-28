#!/usr/bin/env python

import os,sys,time
import cv2
import numpy as np

def nothing(x):
    pass
 

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Trackbars")
    
    cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)

    while True:
        ret, frame = cap.read()
        #cv2.imshow("Capture", frame)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        #cv2.imshow("HSV", hsv_frame)
        #Filter color
        lower_red = np.array([l_h,l_s,l_v])
        upper_red = np.array([u_h,u_s,u_v])
        #mask
        f_frame = cv2.inRange(hsv_frame, lower_red, upper_red)
        #cv2.imshow("Masked", f_frame)
        #erode twice
        element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        element2 = cv2.getStructuringElement(cv2.MORPH_RECT,(8,8))
        
        erode_frame = cv2.erode(f_frame, element)
        erode_frame = cv2.erode(erode_frame, element)

        dilate_frame = cv2.dilate(erode_frame, element2)
        dilate_frame = cv2.dilate(dilate_frame, element2)
        
        #cv2.imshow("MORPH", dilate_frame)
        x,y,w,h = cv2.boundingRect(dilate_frame)
        cv2.rectangle(frame, (x,y), (x+w, y+h) , (0,255,0),2)

        #Find contours
        _,contours, hierarchy = cv2.findContours(dilate_frame, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            #box = cv2.cv.BoxPoints(rect)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame, [box], 0, (0,0,255), 2)

        cv2.imshow("MORPH", dilate_frame)
        cv2.imshow("Capture", frame)
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("test.jpeg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()

