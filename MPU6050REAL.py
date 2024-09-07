import MPU6050
import time
import I2C_LCD_driver

mpu = MPU6050.MPU6050()     # instantiate an MPU6050 class object
accel = [0] * 3            # define an array to store accelerometer data
gyro = [0] * 3             # define an array to store gyroscope data
lcd1602 = I2C_LCD_driver.lcd()

def setup():
    mpu.dmp_initialize()    # initialize MPU6050

def loop():
    while True:
        accel = mpu.get_acceleration()      # get accelerometer data
        gyro = mpu.get_rotation()           # get gyroscope data
        # Print converted values
        acc ="(g): {:.1f}\t{:.1f}\t{:.1f}".format(accel[0] / 16384.0, accel[1] / 16384.0, accel[2] / 16384.0)
        gyro ="(d/s): {:.1f}\t{:.1f}\t{:.1f}".format(
            gyro[0] / 131.0, gyro[1] / 131.0, gyro[2] / 131.0)
        lcd1602.lcd_display_string(acc,1,0)
        lcd1602.lcd_display_string(gyro,2,0)
        time.sleep(3)

if __name__ == '__main__':
    print("Program is starting ...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        pass
