#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from std_msgs.msg import Int32
from std_msgs.msg import String
import rospy
import time
import random
import tkinter
from tkinter import messagebox
from tkinter.constants import S
import tkinter.font
from PIL import ImageTk, Image
import Jetson.GPIO as GPIO
import subprocess


#---------------------------------------------- ROS Pulbisher Topic ----------------------------------------------
class ROS_topic():
    def __init__(self):
        rospy.init_node("GUI_Publisher")
        self.count = 0
        self.msg = ''
        
    def advertise(self):
        self.pub1 = rospy.Publisher('message', String, queue_size=20)
        self.pub2 = rospy.Publisher('counter', Int32, queue_size=10)
        self.rate = rospy.Rate(2)
        self.count += 1
        '''
        while not rospy.is_shutdown():
                self.pub1 = rospy.Publisher('counter', Int32, queue_size=10)
                self.rate = rospy.Rate(2)
                self.pub1.publish(self.msg)
        '''        
        print(" Start Node ")
            

#---------------------------------------------- ROS MASTER GUI ----------------------------------------------
class ROS_GUI():
    # Interrupt
    def key_input(self, event):
        key = event.keysym

        if key == 'space':
            print("Pressed Space")

        if key == 'Escape':
            self.led_off()
            self.buzzer_off()
            self.camera_off()
            self.rqt_off()
            self.termPublisher()
            print("Reset")

    def destroy(self, event):
        self.window.destroy()
    
    # Jetson Nano
    def led_on(self):
        topic.pub1.publish('led on')
        self.btnLedOff['state'] = 'active'
        print('LED ON')

    def led_off(self):
        topic.pub1.publish('led off')
        self.btnLedOff['state'] = 'disabled'
        self.btnLedOn['state'] = 'active'
        print('LED OFF')

    def buzzer_on(self):
        topic.pub1.publish('buzzer on')
        self.btnBuzOn['state'] = 'disabled'
        self.btnBuzOff['state'] = 'active'
        print('Buzzer ON')

    def buzzer_off(self):
        topic.pub1.publish('buzzer off')
        self.btnBuzOff['state'] = 'disabled'
        self.btnBuzOn['state'] = 'active'
        print('Buzzer OFF')

    def camera_on(self):
        topic.pub1.publish('camera on')
        self.btnCamOn['state'] = 'disabled'
        self.btnCamOff['state'] = 'active'
        print('Camera ON')

    def camera_off(self):
        topic.pub1.publish('camera off')
        self.btnCamOff['state'] = 'disabled'
        self.btnCamOn['state'] = 'active'
        print('Camera OFF')
    
    def rqt_on(self):
        topic.pub1.publish('rqt on')
        self.btnRqtOn['state'] = 'disabled'
        self.btnRqtOff['state'] = 'active'
        print('RQT ON')

    def rqt_off(self):
        topic.pub1.publish('rqt off')
        self.btnRqtOff['state'] = 'disabled'
        self.btnRqtOn['state'] = 'active'
        print('RQT OFF')

    def chkState(self):
        if self.state == False:
            self.btnLedOn['state']='disabled'
            self.btnBuzOn['state']='disabled'
            self.btnCamOn['state']='disabled'
            self.btnRqtOn['state']='disabled'
        else:
            self.btnLedOn['state']='active'
            self.btnBuzOn['state']='active'
            self.btnCamOn['state']='active'
            self.btnRqtOn['state']='active'

    def alt_on(self): # 경고신
        self.label_face2['text'] = '1'
        self.window.configure(bg='red')
        self.label['bg'] = 'red'
        self.label1['bg'] = 'red'
        self.label_face1['bg'] = 'red'
        self.label_face2['bg'] = 'red'
        self.btnAltOn['state'] = 'disabled'
        self.btnAltOff['state'] = 'active'
        print('Alert ON')

    def alt_off(self):
        nano.led_off()
        self.label_face2['text'] = '0'
        self.window.configure(bg='skyblue')
        self.label['bg'] = 'skyblue'
        self.label1['bg'] = 'skyblue'
        self.label_face1['bg'] = 'skyblue'
        self.label_face2['bg'] = 'skyblue'
        self.btnAltOn['state'] = 'active'
        self.btnAltOff['state'] = 'disabled'
        print('Alert ON')

    # Git Command
    def git_commit(self):
        subprocess.call('bash git_commit.sh',shell=True)

    def git_push(self):
        subprocess.call('bash git_push.sh',shell=True)

    # ROS Node
    def initPublisher(self):
        topic.advertise()
        self.state = True
        self.chkState()
        self.btnInitPub['state'] = 'disabled'
        self.btnTermPub['state'] = 'active'
        print('Initiate Publisher')

    def termPublisher(self):
        self.led_off()
        self.buzzer_off()
        self.camera_off()
        self.rqt_off()
        topic.pub1.unregister()
        topic.pub2.unregister()
        self.state = False
        self.chkState()
        self.btnInitPub['state'] = 'active'
        self.btnTermPub['state'] = 'disabled'
        print('Terminate Publisher')

    def initSubscriber(self):
        print('Initiate Subscriber')

    def termSubscriber(self):
        print('Terminate Publisher')
    
    # Button Control
    def pushed_buzzer_on(self):
        self.buzzer_on()

    def pushed_buzzer_off(self):
        self.buzzer_off()

    def pushed_led_on(self):
        self.led_on()

    def pushed_led_off(self):
        self.led_off()

    def pushed_btnInitPub(self):
        self.initPublisher()

    def pushed_btnTermPub(self):
        msg_term = messagebox.askyesno(title="Warning", message="Do you want to terminate the Publisher?")
        if msg_term == True:
            self.termPublisher()
        else:
            pass

    def pushed_CamOn(self):
        self.camera_on()

    def pushed_CamOff(self):
        self.camera_off()

    def pushed_RqtOn(self):
        self.rqt_on()

    def pushed_RqtOff(self):
        self.rqt_off()

    def pushed_AltOn(self):
        self.alt_on()

    def pushed_AltOff(self):
        self.alt_off()

    def pushed_GitCommit(self):
        self.git_commit()

    def pushed_GitPush(self):
        self.git_push()

    # GUI Setup
    def setupWindow(self):
        self.window = tkinter.Tk()
        self.window.title("ROS GUI Ver.3.3")
        self.window.geometry("600x800")
        self.window.configure(bg='skyblue')
        self.window.resizable(False, False)

    def setupCanvas(self):
        self.canvas = tkinter.Canvas(width=600, height=200, bg='white')
        self.canvas.pack()

    def setupFont(self):
        self.fontStyle1 = tkinter.font.Font(self.window, size=24, weight='bold', family='Consoles')
        self.fontStyle2 = tkinter.font.Font(self.window, size=12, weight='bold', family='Consoles')
        self.fontStyle3 = tkinter.font.Font(self.window, size=12, weight='normal', family='Consoles')

    def setupLabel(self):
        # self.label = tkinter.Label(text="ROS GUI for Topic", font=self.fontStyle1, bg='skyblue')
        # self.label.place(x=150, y=600)
        self.label = tkinter.Label(self.frameBlank3, text="ROS GUI for Topic", font=self.fontStyle1, bg='skyblue')
        self.label1 = tkinter.Label(self.frameBlank1, text="Message Control", font=self.fontStyle1, bg='skyblue')
        self.label_face1 = tkinter.Label(self.frameBlank4, text="Face Detection : ", font=self.fontStyle2, bg='skyblue')
        self.label_face2 = tkinter.Label(self.frameBlank4, text="0", font=self.fontStyle2, bg='skyblue')
        self.label.pack()
        self.label1.pack()
        self.label_face1.pack(side='left')
        self.label_face2.pack(side='left')

    def setupFrame(self):
        self.frame = tkinter.Frame(self.window)
        self.frame1 = tkinter.Frame(self.window)
        self.frame2 = tkinter.Frame(self.window)
        self.frame3 = tkinter.Frame(self.window)
        self.frame4 = tkinter.Frame(self.window)
        self.frame5 = tkinter.Frame(self.window)
        self.frame6 = tkinter.Frame(self.window)
        self.frame7 = tkinter.Frame(self.window)
        self.frameBlank1 = tkinter.Frame(self.canvas, height=30)
        self.frameBlank2 = tkinter.Frame(self.window, height=30)
        self.frameBlank3 = tkinter.Frame(self.window, height=30)
        self.frameBlank4 = tkinter.Frame(self.window, height=30)

        self.frameBlank1.pack()
        self.frame.pack()
        self.frameBlank2.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frameBlank3.pack()
        self.frame6.pack()
        self.frameBlank4.pack()
        self.frame7.pack()

    def setupText(self):
        self.text = tkinter.Text(self.frame, width=52, height=5)
        self.text.configure(font=self.fontStyle3)
        self.text.pack()

    def setupButton(self):
        # frame
        self.btnRead = tkinter.Button(self.frame, width=20, height=2, text="Read", command=self.getTextInput, font=self.fontStyle2, state='active')
        self.btnErase = tkinter.Button(self.frame, width=20, height=2, text="Erase", command=self.eraseTextInput, font=self.fontStyle2, state='disabled')
        self.btnRead.pack(side='left')
        self.btnErase.pack(side='left')
        
        # frame1
        self.btnInitPub = tkinter.Button(self.frame1, width=20, height=2, text='Initiate Publisher', command=self.pushed_btnInitPub, font=self.fontStyle2, state='active')
        self.btnTermPub = tkinter.Button(self.frame1, width=20, height=2, text='Terminate Publisher', command=self.pushed_btnTermPub, font=self.fontStyle2, state='disabled')
        self.btnInitPub.pack(side='left')
        self.btnTermPub.pack(side='left')

        # frame2
        self.btnLedOn = tkinter.Button(self.frame2, width=20, height=2, text='LED ON', command=self.pushed_led_on, font=self.fontStyle2, state='disabled')
        self.btnLedOff = tkinter.Button(self.frame2, width=20, height=2, text='LED OFF', command=self.pushed_led_off, font=self.fontStyle2, state='disabled')
        self.btnLedOn.pack(side='left')
        self.btnLedOff.pack(side='left')
        
        # frame3
        self.btnBuzOn = tkinter.Button(self.frame3, width=20, height=2, text='Buzzer ON', command=self.pushed_buzzer_on, font=self.fontStyle2, state='disabled')
        self.btnBuzOff = tkinter.Button(self.frame3, width=20, height=2, text='Buzzer OFF', command=self.pushed_buzzer_off, font=self.fontStyle2, state='disabled')
        self.btnBuzOn.pack(side='left')
        self.btnBuzOff.pack(side='left')       

        # frame4
        self.btnCamOn = tkinter.Button(self.frame4, width = 20, height=2, text='Camera On', command=self.pushed_CamOn, font=self.fontStyle2, state='disabled')
        self.btnCamOff = tkinter.Button(self.frame4, width = 20, height=2, text='Camera Off', command=self.pushed_CamOff, font=self.fontStyle2, state='disabled')
        self.btnCamOn.pack(side='left')
        self.btnCamOff.pack(side='left')

        # frame5
        self.btnRqtOn = tkinter.Button(self.frame5, width = 20, height=2, text='RQT Grpah On', command=self.pushed_RqtOn, font=self.fontStyle2, state='disabled')
        self.btnRqtOff = tkinter.Button(self.frame5, width = 20, height=2, text='RQT Graph Off', command=self.pushed_RqtOff, font=self.fontStyle2, state='disabled')
        self.btnRqtOn.pack(side='left')
        self.btnRqtOff.pack(side='left')

        # frame6
        self.btnAltOn = tkinter.Button(self.frame6, width = 20, height=2, text='Alert On', command=self.pushed_AltOn, font=self.fontStyle2, state='active')
        self.btnAltOff = tkinter.Button(self.frame6, width = 20, height=2, text='Alert Off', command=self.pushed_AltOff, font=self.fontStyle2, state='disabled')
        self.btnAltOn.pack(side='left')
        self.btnAltOff.pack(side='left')

        # frame7
        self.btnGitCommit = tkinter.Button(self.frame7, width = 20, height=2, text='Git Commit', command=self.pushed_GitCommit, font=self.fontStyle2, state='active')
        self.btnGitPush = tkinter.Button(self.frame7, width = 20, height=2, text='Git Push', command=self.pushed_GitPush, font=self.fontStyle2, state='active')
        self.btnGitCommit.pack(side='left')
        self.btnGitPush.pack(side='left')

    def setupMenuBar(self):
        # Main Frameu
        self.menubar = tkinter.Menu(self.window)
        # File
        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Exit")
        # Info
        self.info = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Info", menu=self.info)
        self.info.add_command(label="Who", command=self.msg_who)
        self.info.add_command(label='Version', command=self.msg_version)

    def msg_who(self):
        messagebox.showinfo(title="Inventor", message=" 한국산업기술대학교          \n 메카트로닉스공학과          \n 정윤철")

    def msg_version(self):
        messagebox.showinfo(title="Version", message=" ROS GUI Version 3.3        ")

    def getTextInput(self):
        self.input = self.text.get("1.0", 'end-1c')
        if self.btnTermPub['state'] == 'disabled':
                messagebox.showwarning("Messaage Control", " Publiser Doesn't Work!! ")
        else:
            topic.pub1.publish(self.input)
        
            if self.input == '':
                    messagebox.showwarning("Messaage Control", " Write Anyting!! ")
                    self.btnErase['state'] = 'disabled'

            else:
                self.btnErase['state'] = 'active'
                print(self.input)

    def eraseTextInput(self):
        self.text.delete("1.0", 'end-1c')
        self.btnErase['state'] = 'disabled'

    # main
    def main(self):
        # self.window.after(300,self.main)
        print(2)
        time.sleep(1)

    # Class Constructor
    def __init__(self):
        self.state = False
        # Setup GUI
        self.setupWindow()
        self.setupCanvas()
        self.setupFrame()
        self.setupFont()
        self.setupLabel()
        self.setupText()
        self.setupButton()
        self.setupMenuBar()
        # Flag
        self.flag_buzzer = False
        self.flag_led = False
        self.flag_publisher = False
        self.flag_subscriber = False
        
        self.window.config(menu=self.menubar)
        self.window.bind('<Key>',self.key_input)
        self.window.bind('<Control-c>', self.destroy)
        self.window.mainloop()


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
                GPIO.setup(self.pin_Switch, GPIO.IN)
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
nano = JetsonNano()
# topic = ROS_topic()
gui = ROS_GUI()