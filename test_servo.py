""" Test the servo """
# Use this comamnd to see the active address:
# sudo i2cdetect -y -r 7  -- use pin 3 and 5
#                         -- use pin 27 28

import time
from adafruit_servokit import ServoKit
import board
import busio

i2c_bus = busio.I2C(board.SCL, board.SDA)

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16, address=0x43
               #, i2c=i2c_bus
               )

def og():
    """ Rest everything """
    all_straight()
    thumb_mid() 
    middle()
    kit.servo[15].angle = 0 # 110 for 90 degree\

def thumb_mid():
    """ move the thumb to the middle position """
    kit.servo[8].angle = 90
    kit.servo[9].angle = 90

def thumb_right():
    """ move the thumb to the left position """
    kit.servo[8].angle = 130
    kit.servo[9].angle = 120

def thumb_rbend():
    #kit.servo[8].angle = 90 #lefr servo
    #kit.servo[9].angle = 110 #right servo
    kit.servo[8].angle = 120
    kit.servo[9].angle = 140

def thumb_lbend():
    #hella sketchy
    kit.servo[8].angle = 20
    kit.servo[9].angle = 70

def thumb_left():
    """ move thumb to the left position """
    kit.servo[8].angle = 60
    kit.servo[9].angle = 70

def thumb_bend():
    """ make the thumb bend """
    kit.servo[8].angle = 50   
    kit.servo[9].angle = 120


def thumb_straight():
    """ make the thumb straight """
    kit.servo[8].angle = 130  # 130
    kit.servo[9].angle = 50   # 50

def all_straight():
    """ make all non-thumb fingers straight """
    kit.servo[0].angle = 0   # 0 straight pinky.
    kit.servo[1].angle = 180 # 0 straight middle finger.
    kit.servo[2].angle = 180 # 180 straight index finger.
    kit.servo[3].angle = 0   # 0 straight ring finger.

def all_bend():
    """ make all non-thumb fingers bend """
    kit.servo[0].angle = 180   # 0 straight pinky.
    kit.servo[1].angle = 0 # 0 straight middle finger.
    kit.servo[2].angle = 0 # 180 straight index finger.
    kit.servo[3].angle = 180   # 0 straight ring finger.

def left_20():
    """ make all non-thumb fingers move left """
    kit.servo[4].angle = 55 #ring
    kit.servo[5].angle = 60 #middle
    kit.servo[6].angle = 70 #pinky
    kit.servo[7].angle = 70 #pointer

def right_20():
    """ make all non-thumb fingers move right """
    kit.servo[4].angle = 95 #ring
    kit.servo[5].angle = 100 #middle
    kit.servo[6].angle = 110 #pinky
    kit.servo[7].angle = 110 #pointer

def middle():
    """ make all non-thumb fingers move to the middle """
    kit.servo[4].angle = 75
    kit.servo[5].angle = 80
    kit.servo[6].angle = 90
    kit.servo[7].angle = 90

def a():
    """ make letter A """
    all_bend()
    thumb_rbend()

def b():
    """ make letter B """
    all_straight()
    thumb_left()

def c():
    """ make letter c """
    kit.servo[0].angle = 170   # 0 straight pinky.
    kit.servo[1].angle = 10 # 0 straight middle finger.
    kit.servo[2].angle = 10 # 180 straight index finger.
    kit.servo[3].angle = 170   # 0 straight ring finger.
    
    kit.servo[8].angle = 90  # 110
    kit.servo[9].angle = 100   # 70 
    kit.servo[15].angle = 120 # 110 for 90 degree to your right

def d():
    """ make letter c """
    kit.servo[2].angle = 180 
    kit.servo[0].angle = 180 
    kit.servo[1].angle = 0 
    kit.servo[3].angle = 180  
    thumb_bend()
    
def e():
    all_bend()
    thumb_bend()

def f():
    kit.servo[2].angle = 0
    thumb_bend() 

def i():
    kit.servo[1].angle = 0 
    kit.servo[2].angle = 0
    kit.servo[3].angle = 180 
    thumb_bend() 

def j():
    i();
    kit.servo[6].angle = 50 #pinky
    kit.servo[0].angle = 110   # 0 straight pinky.
    kit.servo[15].angle = 90 # 110 for 90 degree to your right
    
def k():
    kit.servo[5].angle = 60 
    kit.servo[7].angle = 110
    kit.servo[0].angle = 180   
    kit.servo[3].angle = 180   
    thumb_bend()
    
def l():
    kit.servo[0].angle = 180   # 0 straight pinky.
    kit.servo[1].angle = 0 # 0 straight middle finger.
    kit.servo[3].angle = 180   # 0 straight ring finger.
    thumb_right()
    
def o():
    """ make letter c """
    all_bend()
    thumb_bend()
    kit.servo[15].angle = 120 # 110 for 90 degree to your right

def r():
    kit.servo[2].angle = 150 # 180 straight index finger.
    kit.servo[7].angle = 70 #pointer
    kit.servo[5].angle = 100
    kit.servo[3].angle = 180   # 0 straight ring finger.
    kit.servo[0].angle = 180   # 0 straight pinky.
    thumb_bend()

def s():
    all_bend()
    thumb_lbend()

def t():
    kit.servo[7].angle = 110
    all_bend()
    thumb_bend()
    
def u():
    kit.servo[0].angle = 180   # 0 straight pinky.
    kit.servo[3].angle = 180   # 0 straight ring finger.
    thumb_lbend()

def v():
    u()
    kit.servo[5].angle = 60 #middle
    kit.servo[7].angle = 110
    
def w(): 
    kit.servo[0].angle = 180   # 0 straight pinky.
    kit.servo[7].angle = 110 #pointer
    kit.servo[4].angle = 55 #ring
    thumb_lbend()

def x():
    kit.servo[8].angle = 40   
    kit.servo[9].angle = 170
    
    kit.servo[0].angle = 180   # 0 straight pinky.
    kit.servo[1].angle = 0 # 180 straight middle finger.
    kit.servo[2].angle = 150 # 180 straight index finger.
    kit.servo[3].angle = 180   # 0 straight ring finger.
    
def y():
    kit.servo[1].angle = 0 # 0 straight middle finger.
    kit.servo[3].angle = 180   # 0 straight ring finger.
    kit.servo[2].angle = 0 # 180 straight index finger.
    
    kit.servo[6].angle = 70 #pinky
    thumb_right()
    
    
def z():
    kit.servo[0].angle = 180   # 0 straight pinky.
    kit.servo[1].angle = 0 # 0 straight middle finger.
    kit.servo[3].angle = 180   # 0 straight ring finger.
    thumb_bend()
    
    kit.servo[7].angle = 110 #pointer
    time.sleep(0.5)
    kit.servo[7].angle = 70 #pointer
    time.sleep(0.5)
    
    kit.servo[2].angle = 100 # 180 straight index finger.
    kit.servo[7].angle = 110 #pointer
    time.sleep(0.5)
    kit.servo[7].angle = 70 #pointer
    
while True:   
    og()
    time.sleep(2)
    a()
    time.sleep(2)
    og()
    time.sleep(2)
    b()
    time.sleep(2)
    og()
    time.sleep(2)
    c()
    time.sleep(2)
    og()
    time.sleep(2)
    d()
    time.sleep(2)
    og()
    time.sleep(2)
    e()
    time.sleep(2)
    og()
    time.sleep(2)
    f()
    time.sleep(2)
    og()
    time.sleep(2)
    i()
    time.sleep(2)
    og()
    time.sleep(2)
    j()
    time.sleep(2)
    og()
    time.sleep(2)
    k()
    time.sleep(2)
    og()
    time.sleep(2)
    l()
    time.sleep(2)
    og()
    time.sleep(2)
    o()
    time.sleep(2)
    og()
    time.sleep(2)
    r()
    time.sleep(2)
    og()
    time.sleep(2)
    s()
    time.sleep(2)
    og()
    time.sleep(2)
    t()
    time.sleep(2)
    og()
    time.sleep(2)
    u()
    time.sleep(2)
    og()
    time.sleep(2)
    v()
    time.sleep(2)
    og()
    time.sleep(2)
    w()
    time.sleep(2)
    og()
    time.sleep(2)
    x() 
    time.sleep(2)
    og()
    time.sleep(2)
    y()
    time.sleep(2)
    og()
    time.sleep(2)
    z()
    time.sleep(2)
    og()
    time.sleep(2)
    
print("Existing...")

#time.sleep()
