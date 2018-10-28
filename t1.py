import cv2
import numpy as np

def main():
    w = 960
    h = 540
    
    cap = cv2.VideoCapture(0)
    cap.set(3, w)
    cap.set(4, h)

    print(cap.get(3))
    print(cap.get(4))

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while ret:
        d = cv2.absdiff(frame1, frame2)
        
        gray = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) 
        
        frame3 = frame1
        dilated = cv2.dilate(th, np.ones((3,3),np.uint8), iterations=1)
        eroded = cv2.erode(dilated, np.ones((3,3),np.uint8), iterations=1)

        x,y,w,h = cv2.boundingRect(eroded)
        cv2.rectangle(frame1, (x,y), (x+w, y+h) , (0,255,0),2)

        #img, c,h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame1, c, -1, (0,0,255),2)
        #Find contours
        _,contours, hierarchy = cv2.findContours(eroded, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            #box = cv2.cv.BoxPoints(rect)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame1, [box], 0, (0,0,255), 2)
        
        #ret, frame = cap.read()
        cv2.imshow("Original", frame2)
        cv2.imshow("Intermediate", frame1)
        cv2.imshow("Eroded", eroded)

        if cv2.waitKey(1) == 27:
           break
        frame1 = frame2
        ret, frame2 = cap.read()
        
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()
 
