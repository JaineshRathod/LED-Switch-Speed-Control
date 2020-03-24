import threading
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_1 = 8
led_2 = 10
led_3 = 11
led_4 = 12

GPIO.setup(led_1, GPIO.OUT, initial =GPIO.LOW)
GPIO.setup(led_2, GPIO.OUT, initial =GPIO.LOW)
GPIO.setup(led_3, GPIO.OUT, initial =GPIO.LOW)
GPIO.setup(led_4, GPIO.OUT, initial =GPIO.LOW)

d=2.0
c1=0
c2=0
c3=0
c4=0

def blink1():
    GPIO.output(led_1,GPIO.LOW)
    global t1
    t1 = threading.Timer(d,led1)
    t1.start()
def blink2():
    GPIO.output(led_2,GPIO.LOW)
    global t2
    t2 = threading.Timer(d,led2)
    t2.start()
def blink3():
    GPIO.output(led_3,GPIO.LOW)
    global t3
    t3 = threading.Timer(d,led3)
    t3.start()
def blink4():
    GPIO.output(led_4,GPIO.LOW)
    global t4
    t4 = threading.Timer(d,led4)
    t4.start()
def led1():
    global t5
    t5 = threading.Timer(d,blink1)
    t5.start()
    GPIO.output(led_1,GPIO.HIGH)
def led2():
    global t6
    t6 = threading.Timer(d,blink2)
    t6.start()
    GPIO.output(led_2,GPIO.HIGH)
def led3():
    global t7
    t7 = threading.Timer(d,blink3)
    t7.start()
    GPIO.output(led_3,GPIO.HIGH)
def led4():
    global t8
    t8 = threading.Timer(d,blink4)
    t8.start()
    GPIO.output(led_4,GPIO.HIGH)

def led1_OFF():
    global c1
    c1 = 0
    GPIO.output(led_1,GPIO.LOW)
def led2_OFF():
    global c2
    c2 = 0
    GPIO.output(led_2,GPIO.LOW)
def led3_OFF():
    global c3
    c3 = 0
    GPIO.output(led_3,GPIO.LOW)
def led4_OFF():
    global c4
    c4 = 0
    GPIO.output(led_4,GPIO.LOW)
    
def allOFF():
    global c1
    global c2
    global c3
    global c4
    
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    GPIO.output(led_1,GPIO.LOW)
    GPIO.output(led_2,GPIO.LOW)
    GPIO.output(led_3,GPIO.LOW)
    GPIO.output(led_4,GPIO.LOW)

print("LED Switch Speed Control")
print("Press '1' to select LED 1")
print("Press '2' to select LED 2")
print("Press '3' to select LED 3")
print("Press '4' to select LED 4")
print("Press '+' to Increase LED Speed")
print("Press '-' to Decrease LED Speed")
print("Press '0' to Turn OFF selected LED")
print("Press '.' to TURN OFF all LEDs")

while 1:

    n = input('')
    if n=='1':
        print("LED 1 Selected -Blinking")
        led1()
        c1 = (c1+1)%2
        
    elif n=='2':
        print("LED 2 Selected -Blinking")
        led2()
        c2 = (c2+1)%2
        
    elif n=='3':
        print("LED 3 Selected -Blinking")
        led3()
        c3 = (c3+1)%2
        
    elif n=='4':
        print("LED 4 Selected -Blinking")
        led4()
        c4 = (c4+1)%2
        
    elif n=='0':
        print("Turning OFF Selected LED")
        
        if (c1):
            print("LED 1 OFF")
            t1.cancel()
            t5.cancel()
            led1_OFF()
            
        if (c2):
            print("LED 2 OFF")
            t2.cancel()
            t6.cancel()
            led2_OFF()
            
        if (c3):
            print("LED 3 OFF")
            t3.cancel()
            t7.cancel()
            led3_OFF()
            
        if (c4):
            print("LED 4 OFF")
            t4.cancel()
            t8.cancel()
            led4_OFF()
            
    elif n=='.':
        print("Turning OFF all LEDs")
        
        if (c1):
            print("LED 1 OFF")
            t1.cancel()
            t5.cancel()
        if (c2):
            print("LED 2 OFF")
            t2.cancel()
            t6.cancel()
        if (c3):
            print("LED 3 OFF")
            t3.cancel()
            t7.cancel()
        if (c4):
            print("LED 4 OFF")
            t4.cancel()
            t8.cancel()
        allOFF()
    elif n=='+':
        print("Increasing Blinking Speed")
        d = d - 0.25
    elif n=='-':
        print("Decreasing Blinking Speed")
        d = d + 0.25
    else:
        print("Wrong Input")
    