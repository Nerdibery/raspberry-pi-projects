from gpiozero import Motor
from time import sleep

# Initialize motor pins
left_motor = Motor(forward=5, backward=6, enable=12)
right_motor = Motor(forward=27, backward=22, enable=13)

def move_forward_and_stop():
    left_motor.forward()
    right_motor.forward()
    right_motor.value = 0.4  # Set right motor speed to 30%
    left_motor.value = 0.4 
    sleep(2)  # Move forward for 2 seconds
    left_motor.stop()
    right_motor.stop()
    sleep(2)  # Stop for 2 seconds

def move_backward():
    left_motor.forward()
    right_motor.forward()
    right_motor.value = -0.4  # Set right motor speed to 30%
    left_motor.value = -0.4
    sleep(2)  # Move backward for 2 seconds
    left_motor.stop()
    right_motor.stop()
    sleep(2)  # Stop for 2 seconds

try:
    while True:
        move_forward_and_stop()
        move_backward()

except KeyboardInterrupt:
    left_motor.stop()
    right_motor.stop()
