from gpiozero import RGBLED
import time
from ADCDevice import *

# define the pins for R:GPIO22,G:GPIO27,B:GPIO17
led = RGBLED(red=22, green=27, blue=17, active_high=False)

# Define an ADCDevice class object
adc = ADCDevice()

def setup():
	global adc
	# Detect the pcf8591.
	if(adc.detectI2C(0x48)):
		adc = PCF8591()
	elif(adc.detectI2C(0x4b)): # Detect the ads7830
		adc = ADS7830()
	else:
		print("No correct I2C address found, \n""Please use command 'i2cdetect -y 1' to check the I2C address!+++n""Program Exit. \n");
		exit(-1)
	
def loop():
	while True:
		# read ADC value of 3 potentiometers
		'''
		digital (1(ON), 0(OFF)), analog (0-1, 0.01, 0.05, 0.9))
		The analogRead reads values between 0-255 (8bit) 2^8
		on (1.65V) off (0V)
		'''
		value_Red = adc.analogRead(0)
		value_Green = adc.analogRead(1)
		value_Blue = adc.analogRead(2)
		# map the read value of potentiometers into PWM value and output it
		led.red=value_Red/255
		led.green =value_Green/255
		led.blue=value_Blue/255
		# print read ADC value
		print ('ADC Value value_Red: %d ,\tvlue_Green: %d ,\tvalue_Blue: %d'% (value_Red,value_Green,value_Blue))
		time.sleep(0.01)
		
def destroy():
	adc.close()
	led.close()
if __name__ == '__main__': # Program entrance
	print ('Program is starting ... ')
	setup()
	try:
		loop()
	except KeyboardInterrupt: # Press ctrl-c to end the program.
		destroy()
		print("Ending program")
