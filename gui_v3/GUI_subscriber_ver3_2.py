#! /usr/bin/env python3
import Jetson.GPIO as GPIO
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import time
import cv2
import subprocess
import random

#---------------------------------------------- Directory Path ----------------------------------------------
path_pi = '/home/pi/Archive/Study/FaceDetector/haarcascade_frontalface_default.xml'
path_window = 'C:/Users/minimamba/Documents/Archive/Study/FaceDetector/haarcascade_frontalface_default.xml'
path_jetson = '/home/minimamba/Archive/Study/FaceDetector/'
path_home = '/home/'
path_package = '/home/minimamba/catkin_ws/src/basics/scripts/'


#---------------------------------------------- User Function ----------------------------------------------
def callback(data):
                print(type(data)) #"<class 'std_msgs.msg._String.String'>":
                # subprocess.call('python face.py',shell=True, cwd=path_jetson)
                if str(type(data.data)) =="<class 'str'>": 
                        callback_String(data)
                else:
                        print(type(data.data))
                
def callback_String(data):
        global count
        if data.data == 'buzzer':
                print(data.data) 
                # p.start(10)             # start PWM, Duty Cycle :10
                # p.ChangeFrequency(Frq[4])
        
        elif data.data == 'led on':
                nano.led_blue()
                # nano.led_random(count)
                print(data.data)

        elif data.data == 'led red':
                nano.led_red()

        elif data.data == 'led blue':
                nano.led_blue()

        elif data.data == 'led green':
                nano.led_green()

        elif data.data == 'led off':
                nano.led_off()
                print(data.data)

        elif data.data == 'camera on':
                subprocess.call('python faceScan.py &',shell=True, cwd=path_package)

        elif data.data == 'rqt on':
                subprocess.call('rqt_graph &',shell=True, cwd=path_home)

        elif data.data == 'rqt off':
                subprocess.call('F1',shell=True, cwd=path_home)

        elif data.data == 'distance':
                nano.sonar_disance()

        elif data.data == 'lidar':
                pass

        elif data.data == '(auto) git commit':
                subprocess.call('bash git_commit.sh',shell=True, cwd=path_package)

        elif data.data == '(auto) git push':
                subprocess.call('bash git_push.sh',shell=True, cwd=path_package)

        else:
                print(data.data + " is not option")
                # p.stop()                # stop PWM


#---------------------------------------------- ROS Subscriber Topic ----------------------------------------------
class Subscriber():
        def __init__(self):
                # rospy.init_node("RapberryPi4")
                pass
   

#---------------------------------------------- Jetson Nano ----------------------------------------------
class JetsonNano():
        def __init__(self):
                # Setting pin number
                self.pin_LED_Red = 40
                self.pin_LED_Green = 36
                self.pin_LED_Blue = 38
                self.pin_Trig = 16
                self.pin_Echo = 18
                self.pin_Switch = 12
                self.pin_Buzzer = 7
                self.pin_GND = 39
                self.pin_5V = 2
                # GPIO mode setting
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BOARD) # GPIOn Mode
                self.gpio_default()

        def gpio_default(self):
                # GPIO pin setting
                GPIO.setup(self.pin_LED_Red, GPIO.OUT)
                GPIO.setup(self.pin_LED_Green, GPIO.OUT)
                GPIO.setup(self.pin_LED_Blue, GPIO.OUT)
                GPIO.setup(self.pin_Buzzer, GPIO.OUT)
                GPIO.setup(self.pin_Trig, GPIO.OUT)
                GPIO.setup(self.pin_Echo, GPIO.IN)
                # GPIO.setup(self.pin_Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                # self.p = GPIO.PWM(self.pin_Buzzer, 100)   # pin18 : PWM, 100Hz
                # self.Frq = [262, 294, 330, 349, 392, 440, 493, 523]
                # self.speed = 0.5

        def led_red(self):
                GPIO.output(self.pin_LED_Red, 1)
                # time.sleep(0.5)
                # GPIO.output(self.pin_LED_Red, 0)
                # time.sleep(0.5

        def led_blue(self):
                GPIO.output(self.pin_LED_Blue, 1)

        def led_green(self):
                GPIO.output(self.pin_LED_Green, 1)

        def led_random(self, count):
                # global count
                # turn LED on
                if count % 3 == 0:
                        GPIO.output(self.pin_LED_Red, 1)
                        time.sleep(0.5)
                        GPIO.output(self.pin_LED_Red, 0)
                        time.sleep(0.5)

                elif count % 3 == 1:
                        GPIO.output(self.pin_LED_Green, 1)
                        time.sleep(0.5)
                        GPIO.output(self.pin_LED_Green, 0)
                        time.sleep(0.5)

                elif count % 3 == 2:
                        GPIO.output(self.pin_LED_Blue, 1)
                        time.sleep(0.5)
                        GPIO.output(self.pin_LED_Blue, 0)
                        time.sleep(0.5)
                
        def led_off(self):
                GPIO.output(self.pin_LED_Red, 0)
                GPIO.output(self.pin_LED_Green, 0)
                GPIO.output(self.pin_LED_Blue, 0)

        def sonar_disance(self):
                GPIO.output(self.pin_Trig, False)
                GPIO.output(self.pin_Trig, True)
                time.sleep(0.00001)
                GPIO.output(self.pin_Trig, False)
                
                while GPIO.input(self.pin_Echo) == 0:
                        start = time.time()
                        
                while GPIO.input(self.pin_Echo) == 1:
                        stop = time.time()
                
                check_time = stop - start
                self.distance = check_time * 34300 / 2
                print(self.distance)
                # return self.distance


#---------------------------------------------- main ----------------------------------------------
button = 0
msg_list = list()
count = 0

nano = JetsonNano()
rospy.init_node("JetsonNano")
subscriber = Subscriber()

try:
        sub1 = rospy.Subscriber("counter", Int32, callback)
        sub2 = rospy.Subscriber("message", String, callback)
        count += 1
        rospy.spin()
        
except rospy.ROSInterruptException:
        print("Interrupt!!")
