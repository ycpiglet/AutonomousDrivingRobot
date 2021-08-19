#! /usr/bin/env python3
#-*- coding:utf-8 -*-
import Jetson.GPIO as GPIO
import numpy as np
import cv2

route_pi = '/home/pi/Archive/Study/FaceDetector/haarcascade_frontalface_default.xml'
route_window = 'C:/Users/minimamba/Documents/Archive/Study/FaceDetector/haarcascade_frontalface_default.xml'
route_jetson = '/home/minimamba/Archive/Study/FaceDetector/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(route_jetson)

class JetsonNano():
        def __init__(self):
                # Setting pin number
                self.pin_LED_Red = 2
                self.pin_LED_Green = 3
                self.pin_LED_Blue = 4
                self.pin_Trig = 27
                self.pin_Echo = 17
                self.pin_Switch = 22
                self.pin_Buzzer = 10
                self.pin_GND = 6
                # GPIO mode setting
                # GPIO.setwarnings(False)
                # GPIO.setmode(GPIO.BCM) # GPIOn Mode
                self.gpio_default()

        def gpio_default(self):
                # GPIO pin setting
                GPIO.setmode(GPIO.BCM)
                self.mode = GPIO.getmode()
                GPIO.setup(33, GPIO.OUT)
                # GPIO.setup(pin_LED_Red, GPIO.OUT)
                # GPIO.setup(self.pin_LED_Green, GPIO.OUT)
                # GPIO.setup(self.pin_LED_Blue, GPIO.OUT)
                # GPIO.setup(self.pin_Buzzer, GPIO.OUT)
                # GPIO.setup(self.pin_Trig, GPIO.OUT)
                # GPIO.setup(self.pin_Echo, GPIO.IN)
                # GPIO.setup(self.pin_Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                # self.p = GPIO.PWM(self.pin_Buzzer, 100)   # pin18 : PWM, 100Hz
                # self.Frq = [262, 294, 330, 349, 392, 440, 493, 523]
                # self.speed = 0.5
                pass

        def Pi(count):
                pass
                # # turn LED on
                # if count % 3 == 0:
                #         GPIO.output(self.pin_LED_Red, 1)
                #         time.sleep(0.5)
                #         GPIO.output(self.pin_LED_Red, 0)
                #         time.sleep(0.5)

                # elif count % 3 == 1:
                #         GPIO.output(self.pin_LED_Green, 1)
                #         time.sleep(0.5)
                #         GPIO.output(self.pin_LED_Green, 0)
                #         time.sleep(0.5)

                # elif count % 3 == 2:
                #         GPIO.output(pin_LED_Blue, 1)
                #         time.sleep(0.5)
                #         GPIO.output(pin_LED_Blue, 0)
                #         time.sleep(0.5)


cap = cv2.VideoCapture(0) # 노트북 웹캠을 카메라로 사용
cap.set(3,640) # 너비
cap.set(4,480) # 높이

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # 좌우 대칭
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.05, 5)
    print("Number of faces detected: " + str(len(faces)))

    if len(faces):
        print('hi')
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow('result', frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # Esc 키를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()