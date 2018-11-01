import cv2
import sys,os
import numpy as np

gWorkingMode="MODE:AUTO(LEVEL5)"

def main():
    w = 1280
    h = 720

    cap = cv2.VideoCapture("http://192.168.8.1:8083/?action=stream") #0)
    cap.set(3, w)
    cap.set(4, h)

    print("Query Video Width:", cap.get(3))
    print("Query Video Height:", cap.get(4))

    while cap.isOpened():
        ret, frame = cap.read()
        
        cv2.putText(frame, "5G Auxiliary Self-Driving and Remote Driving", (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255),2)
        cv2.putText(frame, gWorkingMode, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (5,255,0),1)
        cv2.putText(frame, "NEURAL NETWORKS DECISION:STOP", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (5,255,0),1)
        cv2.putText(frame, "GPS SIGNAL:NO SIGNAL!", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (5,255,0),1)

        ##############################################################
        #Draw minder box
        cv2.line(frame, (620,360), (660,360),(255,255,255), 2)
        cv2.line(frame, (640,340), (640,380),(255,255,255), 2)

        cv2.line(frame, (230,230), (270,230),(255,255,255),2)
        cv2.line(frame, (230,230), (230,270),(255,255,255),2)

        cv2.line(frame, (1050,230), (1010,230),(255,255,255),2)
        cv2.line(frame, (1050,230), (1050,270),(255,255,255),2)

        cv2.line(frame, (1050,490), (1010,490),(255,255,255),2)
        cv2.line(frame, (1050,490), (1050,450),(255,255,255),2)

        cv2.line(frame, (230,490), (270,490),(255,255,255),2)
        cv2.line(frame, (230,490), (230,450),(255,255,255),2)
        #Draw white box
        cv2.rectangle(frame, (600,320), (680,400), (255, 255,255), 2)
        #Draw ERICSSON LOGO
        cv2.rectangle(frame, (560,540), (650,620), (0, 255,0), 2)
        cv2.rectangle(frame, (560,520), (610,540), (0, 255,0), -1)
        cv2.putText(frame, "LOGO", (561, 539), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0),2)
        #Draw signal,5G NR
        cv2.rectangle(frame, (1210,35), (1215,40), (255,255,255), -1)
        cv2.rectangle(frame, (1220,25), (1225,40), (255,255,255), -1)
        cv2.rectangle(frame, (1230,15), (1235,40), (255,255,255), -1)
        cv2.rectangle(frame, (1240,5), (1245,40), (255,255,255), -1)
        cv2.putText(frame, "5G NR", (1100, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255),2)
        #Draw circle
        cv2.circle(frame, (640, 360), 10, (255, 255, 255), 1)
        #Draw
        #cv2.ellipse(frame, (255, 255), (150, 75), 0, 0, 360, (0, 255, 255), 1) 
        #Draw polylines
        pts = np.array([[100,706],[380,500],[900,500],[1180,706]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(0,255,255),2) #Yellow
        cv2.putText(frame, "270cm", (800, 515), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255),1)        

        pts = np.array([[140,702],[380,520],[900,520],[1140,702]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(0,0,255),2) #Red
        cv2.putText(frame, "220cm", (800, 540), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
        
        pts = np.array([[40,710],[380,480],[900,480],[1240,710]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(0,255,0),2) #Green
        cv2.putText(frame, "320cm", (800, 495), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),1)
        ##############################################################
        #
        #left_info_box = np.zeros((600,200,3), np.uint8)
        #left_info_box[:]=(255,255,255)
        #cv2.imshow("IMG",left_info_box)
        
        ##############################################################
        cv2.imshow("5G Demo Car Front Video", frame)
        
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == '__main__':
    main()

