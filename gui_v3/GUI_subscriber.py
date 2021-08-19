#! /usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import time
import cv2
import subprocess

route_pi = '/home/pi/Archive/Study/FaceDetector/haarcascade_frontalface_default.xml'
route_window = 'C:/Users/minimamba/Documents/Archive/Study/FaceDetector/haarcascade_frontalface_default.xml'
route_jetson = '/home/minimamba/Archive/Study/FaceDetector/'
route_home = '/home/'

# Define user function
def callback(data):
                print(type(data)) #"<class 'std_msgs.msg._String.String'>":
                # subprocess.call('python face.py',shell=True, cwd=route_jetson)
                if str(type(data.data)) =="<class 'str'>": 
                        callback_String(data)
                else:
                        print(type(data.data))
                
def callback_String(data):
        print(type(data.data))
        if data.data == 'buzzer':
                print(data.data) 
                # p.start(10)             # start PWM, Duty Cycle :10
                # p.ChangeFrequency(Frq[4])
        
        elif data.data == 'led':
                print(data.data)
                # GPIO.output(self.pin_LED_Red, 1)
                time.sleep(0.5)
                # GPIO.output(self.pin_LED_Red, 0)
                time.sleep(0.5)

        elif data.data == 'led off':
                print(data.data)

        elif data.data == 'camera':
                subprocess.call('python face.py',shell=True, cwd=route_jetson)
                pass
        
        elif data.data == 'rqt':
                subprocess.call('rqt_graph',shell=True, cwd=route_home)
                pass

        elif data.data == 'lidar':
                pass

        else:
                print(data.data + " is not option")
                # p.stop()                # stop PWM

class Subscriber():
        def __init__(self):
                # rospy.init_node("RapberryPi4")
                pass
   

class Pi():
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

#main
button = 0
msg_list = list()

rpi = Pi()
rospy.init_node("RapberryPi4")
subscriber = Subscriber()

try:
        sub1 = rospy.Subscriber("counter", Int32, callback)
        sub2 = rospy.Subscriber("message", String, callback)
        
        rospy.spin()
        
except rospy.ROSInterruptException:
        print("Interrupt!!")
