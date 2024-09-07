from gpiozero import Button
import time
from gpiozero import LED
from ADCDevice import *

Z_Pin = 18      # define Z_Pin
button = Button(Z_Pin) # define Button pin according to BCM Numbering
adc = ADCDevice()# Define an ADCDevice class object
rled = LED(17)
gled = LED(22)
bled = LED(27)

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
        
def loop():
    while True:     
        val_Z = not button.value     # read digital value of axis Z
        val_Y = adc.analogRead(0)    # read analog value of axis X and Y
        val_X = adc.analogRead(1)
        print ('value_X: %d ,\tvlue_Y: %d ,\tvalue_Z: %d'%(val_X,val_Y,val_Z))
        time.sleep(0.01)
        if val_X == 0:
            gled.on()
        elif val_X == 254:
            gled.on()
        elif val_Z == 0:
            rled.on()
        elif val_Y == 254:
            bled.on()
        elif val_Y == 0:
            bled.on()
        else:
            gled.off()
            bled.off()
            rled.off()

def destroy():
    adc.close()
    button.close()

    
if __name__ == '__main__':
    print ('Program is starting ... ') # Program entrance
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
        print("Ending program")
