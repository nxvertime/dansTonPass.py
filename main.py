import cv2, numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('frame.png')

cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

while True:

    success, img = cap.read()

    for barcode in decode(img):
        data = barcode.data.decode('utf-8')
        print(data)


    cv2.imshow('Result', img)
    cv2.waitKey(1)


