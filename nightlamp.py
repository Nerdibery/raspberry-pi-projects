from gpiozero import PWMLED
import time
from ADCDevice import *

# define ledPin
ledPin = 17 
led = PWMLED(ledPin)
# Define an ADCDevice class object
adc = ADCDevice() 

def setup():
    global adc
    # Detect the pcf8591.
    if(adc.detectI2C(0x48)): 
        adc = PCF8591()
    # Detect the ads7830
    elif(adc.detectI2C(0x4b)):
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)

def loop():
    while True:
        # read the ADC value of channel 0
        value = adc.analogRead(0)    
        
        led.value = value / 255.0    # Mapping to PWM duty cycle 
        voltage = value / 255.0 * 3.3
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.01)

def destroy():
    led.close()
    adc.close()
    
# Program entrance
if __name__ == '__main__':   
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        # Press ctrl-c to end the program.  
        destroy()
        print("Ending program")
        
