import math
import time
from ADCDevice import *

#instances
adc = ADCDevice()#define adc as class object

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
        value = adc.analogRead(0)# read adc value from A0 pin
        voltage = value /255.0 * 3.3# calculate voltage
        Rt = 10 * voltage /(3.3 - voltage) #calc resistance value of thermistor
        tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)#calculate temp in kelvin
        tempC = tempK
        