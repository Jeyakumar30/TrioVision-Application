# import pandas as pd  
import cv2  
# import time 

initial = None   

video = cv2.VideoCapture(0)  

while True:  
   isTrue, frame = video.read()  
   var_motion = 0  

   gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
   gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)
   
   # Assigning grayFrame to initalState in first iteration:  
   if initial is None:  
       initial = gray_frame  
       continue  

   # Difference between static or initial and gray frame  

   differ_frame = cv2.absdiff(initial, gray_frame)  

   thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]  

   dilate = cv2.dilate(thresh_frame, None, iterations = 2)  

   cont,_ = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  

   for cur in cont:  

       if cv2.contourArea(cur) < 10000:  
           continue  

       var_motion = 1  

       (cur_x, cur_y,cur_w, cur_h) = cv2.boundingRect(cur)  

    
       cv2.rectangle(frame, (cur_x, cur_y), (cur_x + cur_w, cur_y + cur_h), (0, 0, 255), 3)
       cv2.putText(frame, "Movement Detected", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 0), 2)

#    cv2.imshow("Gray", gray_frame)  
   cv2.imshow("Inital static frame VS current frame: ", differ_frame)  
#    cv2.imshow("Threshold Frame", thresh_frame)  
#    cv2.imshow("Dialated Frame", dilate)  
   cv2.imshow("Motion Detection", frame)  

   wait_key = cv2.waitKey(1)  
   if wait_key == ord('q'):  
       break 

video.release()  
cv2.destroyAllWindows()







"""
Reference: 

1. https://www.kdnuggets.com/2022/08/perform-motion-detection-python.html
2. https://sokacoding.medium.com/simple-motion-detection-with-python-and-opencv-for-beginners-cdd4579b2319

"""