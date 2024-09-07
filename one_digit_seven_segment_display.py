from gpiozero import OutputDevice
import time

LSBFIRST = 1#least significant bit
MSBFIRST = 2#most significant bit

# define the pins for 74HC595
dataPin   = OutputDevice(17)      # DS Pin of 74HC595(Pin14)

latchPin  = OutputDevice(27)      # ST_CP Pin of 74HC595(Pin12)

clockPin  = OutputDevice(22)      # CH_CP Pin of 74HC595(Pin11)

# SevenSegmentDisplay display the character "0"- "F" successively
num = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e]

def shiftOut(order,val):
    for i in range(0,8):
        clockPin.off()
        if(order == LSBFIRST):
            dataPin.on() if (0x01&(val>>i)==0x01) else dataPin.off()
        elif(order == MSBFIRST):
            dataPin.on() if (0x80&(val<<i)==0x80) else dataPin.off()
        clockPin.on()

def loop():
    while True:
        for i in range(0,len(num)):
            latchPin.off()
            shiftOut(MSBFIRST,num[i])  # Send serial data to 74HC595
            latchPin.on()
            time.sleep(1)
        for i in range(0,len(num)):
            latchPin.off()
            shiftOut(MSBFIRST,num[i]&0x7f) # Use "&0x7f" to display the decimal point.
            latchPin.on()
            time.sleep(1)

def destroy():  
    dataPin.close()
    latchPin.close()
    clockPin.close() 

if __name__ == '__main__': 
    # Program entrance
    print ('Program is starting...' )
    try:
        loop()  
    except KeyboardInterrupt:  
        # Press ctrl-c to end the program.
        destroy()
        print("Ending program")
'''
null = [0,0,0,0,0,0,0]

zero = [1,1,1,1,1,1,0]

one = [0,1,1,0,0,0,0]

two = [1,1,0,1,1,0,1]

three = [1,1,1,1,0,0,1]

four = [0,1,1,0,0,1,1]

five = [1,0,1,1,0,1,1]

six = [1,0,1,1,1,1,1]

seven = [1,1,1,0,0,0,0]

eight = [1,1,1,1,1,1,1]

nine = [1,1,1,1,0,1,1]
'''
