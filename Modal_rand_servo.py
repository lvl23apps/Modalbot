#####################################Modal Bot V2 ###########
# This is the  random function mode for the servos. This function is for
# random movement and may be triggered as a function by another script.
#
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#
# Special thanks to index - https://github.com/Index01
###########################################################

import time
from random import randint
from adafruit_servokit import ServoKit

# Servo Shield/HAT/Bonnet (16) channels

kit = ServoKit(channels=16)

def head():
 print("head")
 switch = randint(1,4)
 if switch == 1:
     kit.servo[3].angle = 160
     time.sleep(1)
     kit.servo[3].angle = 35
 elif switch == 2:
     kit.servo[3].angle = 120
     time.sleep(3)
     kit.servo[3].angle = 70
 else:
     kit.servo[3].angle = 160
     time.sleep(9)
     kit.servo[3].angle = 140
     time.sleep(10)

def wing():
 print("wing")
 switch = randint(1,4)
 if switch == 1:
     kit.servo[3].angle = 120
     time.sleep(1)
     kit.servo[3].angle = 70
 elif switch == 2:
     kit.servo[3].angle = 80
     time.sleep(3)
     kit.servo[3].angle = 70
 else:
     kit.servo[3].angle = 90
     time.sleep(9)
     kit.servo[3].angle = 70
     time.sleep(10)

def greeble():
 print("greeble")
 switch = randint(1,4)
 if switch == 1:
     kit.servo[3].angle = 120
     time.sleep(1)
     kit.servo[3].angle = 70
 elif switch == 2:
     kit.servo[3].angle = 80
     time.sleep(3)
     kit.servo[3].angle = 70
 else:
     kit.servo[3].angle = 90
     time.sleep(9)
     kit.servo[3].angle = 70
     time.sleep(10)

while(1):
    switch = randint(1,4)
    if switch == 1:
        head()
        time.sleep(5)
    elif switch == 2:
        wing()
        time.sleep(10)
    elif switch == 3:
        greeble()
        time.sleep(10)
    else:
        print("nap time!!")
        time.sleep(20)
