import cv2
import numpy as np

url = "http://192.168.1.10:8080/video"

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    
    print("Error: Could not connect to Camera. Check IP or WiFi.")
    exit()


print("Connecting... Press 'q' to quit the program.")

while True:
    ret, frame = cap.read()

    if ret:
       
        cv2.imshow("Phone Camera Stream", frame)
    else:
        
        print("Connection lost!")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()