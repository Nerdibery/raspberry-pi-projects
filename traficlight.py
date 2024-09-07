"""
this project displays a counter and blinks 3 leds at intervals.
the system is a prototype for a traffic light system.
components
led(red,blue,green)
7 segment display
jumper wires
author : nerdyberi
date:
"""
#importing modules from libraries
from gpiozero import LED
import time
from gpiozero import OutputDevice

#variables
LSBFIRST = 1#least significant bit
MSBFIRST = 2#most significant bit

#instances
rled = LED(18)
gled = LED(24)
yled = LED(23)

# define the pins for 74HC595
dataPin   = OutputDevice(17)      # DS Pin of 74HC595(Pin14)

latchPin  = OutputDevice(27)      # ST_CP Pin of 74HC595(Pin12)

clockPin  = OutputDevice(22)      # CH_CP Pin of 74HC595(Pin11)

num = [0xc0,0xf9,0xa4,0xb0]
num2 =[0xc0,0xf9,0xa4,0xb0,0x99,0x92]
#main body
def destroy():  
    dataPin.close()
    latchPin.close()
    clockPin.close() 


def three():

        #for i in range(0,len(num)):
            #latchPin.off()
            #shiftOut(MSBFIRST,num[i])  # Send serial data to 74HC595
            #latchPin.on()
            #time.sleep(1)
    
    for i in range(0,len(num)):
        latchPin.off()
        shiftOut(MSBFIRST,num[i]&0x7f) # Use "&0x7f" to display the decimal point.
        latchPin.on()
        time.sleep(1)
        
def five():
    for i in range(0,len(num2)):
        latchPin.off()
        shiftOut(MSBFIRST,num2[i]&0x7f) # Use "&0x7f" to display the decimal point.
        latchPin.on()
        time.sleep(1)
        
def traffic():
    while True:
        rled.on()
        three()
        #time.sleep(3)
        rled.off()
        yled.on()
        time.sleep(1)
        yled.off()
        gled.on()
        five()
        #time.sleep(5)
        gled.off()
        yled.on()
        time.sleep(1)
        yled.off()
    
def shiftOut(order,val):
    for i in range(0,8):
        clockPin.off()
        if(order == LSBFIRST):
            dataPin.on() if (0x01&(val>>i)==0x01) else dataPin.off()
        elif(order == MSBFIRST):
            dataPin.on() if (0x80&(val<<i)==0x80) else dataPin.off()
        clockPin.on()


        
if __name__ =='__main__':
    try:
        print ('Program is starting...' )
        traffic()
    except KeyboardInterrupt:
        print("shutting down")
        destroy()
