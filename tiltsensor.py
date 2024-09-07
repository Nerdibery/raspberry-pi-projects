"""
Tilt Sensor Alarm Project
author - samantha bochaberi
date -3rd june 2024
The alarm system provides valuable feedback to the user by activating the
buzzer and lighting up the LED when the tilt sensor detects a tilt beyond a certain
threshold.
it displays on an 1602LCD display to show the tilt angle and also to provide valuable feedback to the user.
Applications : stablising drones and robots
"""
# importing modules
import MPU6050
from time import sleep
import I2C_LCD_driver
from gpiozero import Buzzer,LED

#instance creation
mpu = MPU6050.MPU6050()#empty instance
lcd1602 = I2C_LCD_driver.lcd()#empty instance from lcd module
led =LED(27)
buzz = Buzzer(22)

#creating empty lists to store data
acc = [0]* 3
gyro = [0] * 3

#turning mpu6050 on
def mpuon():
    mpu.dmp_initialize() #initializing method

#main function
def main():
    while True:
        acc = mpu.get_acceleration()
        gyro = mpu.get_rotation()#raw data btw,gets data for the sensor
        
        # converting raw data to readable in one dp
        accel ="(g): {:.1f}\t{:.1f}\t{:.1f}".format(acc[0] / 16384.0, acc[1] / 16384.0, acc[2] / 16384.0)
        gyr ="(d/s): {:.1f}\t{:.1f}\t{:.1f}".format(gyro[0] / 131.0, gyro[1] / 131.0, gyro[2] / 131.0)
        lcd1602.lcd_display_string(gyr,1,0)
        
        if gyr > 25:# condiion that sets off alarm
            buzz.on()
            led.on()
            lcd1602.lcd_display_string("restore tilt!!",1,0)
            sleep(3)
            buzz.off
            led.off()
            lcd.lcd_clear()
        else:# if condition isnt met pass the if statement
            pass
        # i  havent figured out how to test the angle
        sleep(3)
        lcd1602.lcd_clear()
        
#ensures program runs, only when excecuted and not when module is imported
if __name__ == '__main__':
    lcd1602.lcd_display_string("Program is starting ...")
    mpuon()
    try:
        main()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        lcd1602.lcd_clear()
        pass
        
        
    