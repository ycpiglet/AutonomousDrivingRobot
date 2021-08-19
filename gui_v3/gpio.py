import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# self.mode = GPIO.getmode()
GPIO.setwarnings(False) 

pin_LED_Red = 40
pin_LED_Green = 38
pin_LED_Blue = 36
pin_Trig = 16
pin_Echo = 18
pin_Switch = 12
pin_Buzzer = 7

GPIO.setup(pin_LED_Red, GPIO.OUT)
GPIO.setup(pin_LED_Green, GPIO.OUT)
GPIO.setup(pin_LED_Blue, GPIO.OUT)
GPIO.setup(pin_Buzzer, GPIO.OUT)
GPIO.setup(pin_Trig, GPIO.OUT)
GPIO.setup(pin_Echo, GPIO.IN)
GPIO.setup(pin_Switch, GPIO.IN)
# self.p = GPIO.PWM(self.pin_Buzzer, 100)   # pin18 : PWM, 100Hz
# self.Frq = [262, 294, 330, 349, 392, 440, 493, 523]
# self.speed = 0.5

while True:
    # GPIO.output(pin_LED_Red, GPIO.HIGH)
    # time.sleep(0.5)
    # GPIO.output(pin_LED_Red, 0)
    # time.sleep(0.5)

    # GPIO.output(pin_LED_Blue, GPIO.HIGH)
    # time.sleep(0.5)
    # GPIO.output(pin_LED_Blue, 0)
    # time.sleep(0.5)

    # GPIO.output(pin_LED_Green, 1)
    # time.sleep(0.5)
    # GPIO.output(pin_LED_Green, 0)
    # time.sleep(0.5)

    if GPIO.input(pin_Switch) == GPIO.HIGH:
        print('3')
    else:
        print('no')


    # Check ultra sonic
    # GPIO.output(pin_Trig, False)
    # GPIO.output(pin_Trig, True)
    # time.sleep(0.00001)
    # GPIO.output(pin_Trig, False)
    
    # while GPIO.input(pin_Echo) == 0:
    #     start = time.time()
        
    # while GPIO.input(pin_Echo) == 1:
    #     stop = time.time()
    
    # check_time = stop - start
    # distance = check_time * 34300 / 2
    
    # print(distance)

    # time.sleep(0.4)

    # if distance < 10:
    #     # p.ChangeFrequency(Frq[7])    
    #     GPIO.setup(pin_LED_Red, GPIO.OUT)
    #     GPIO.setup(pin_LED_Green, GPIO.OUT)
    #     GPIO.setup(pin_LED_Blue, GPIO.OUT)