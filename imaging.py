# pip install opencv-contrib-python
# pip install cvlib
# pip install gtts playsound
# pip3 install PyObjC

import cv2
import cvlib as cv
from cvlib.object_dectection import draw_bbox
from gtts import gTTS
from playsound import playsound

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Oject Detection", output_image)

    if cv2.waitKey(0) & 0xFF == orf("q"):
        break
