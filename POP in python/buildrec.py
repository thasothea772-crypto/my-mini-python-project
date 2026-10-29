import cv2
import numpy as np
import pyautogui

width, height = pyautogui.size()
out = cv2.VideoWriter("Recording.avi", cv2.VideoWriter_fourcc(*"XVID"), 20.0, (width, height))

print("Recording... Press Ctrl + C to stop.")

try:
    while True:
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        out.write(frame)
except KeyboardInterrupt:
    print("Recording stopped. Save as recording.avi")

out.release()
