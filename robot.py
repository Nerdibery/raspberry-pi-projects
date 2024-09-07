from gpiozero import Motor  # Import the Motor class from gpiozero library
import time  # Import the time module
import sys  # Import the sys module
import termios  # Import the termios module
import tty  # Import the tty module

class Robot:
    def __init__(self):
        # Define motor pins
        self.left_motor = Motor(forward=5, backward=6, enable=12)  # Initialize left motor pins
        self.right_motor = Motor(forward=27, backward=22, enable=13)  # Initialize right motor pins

    def move_forward(self):
        self.left_motor.forward()  # Move left motor forward
        self.right_motor.forward()  # Move right motor forward
        self.right_motor.value = 0.8 # Set right motor speed to 80%
        self.left_motor.value = 0.8 # Set left motor speed to 80%

    def move_backward(self):
        self.left_motor.backward()  # Move left motor backward
        self.right_motor.backward()  # Move right motor backward
        self.right_motor.value = -0.8  # Set right motor speed to 80%
        self.left_motor.value = -0.8 # Set left motor speed to 80%

    def turn_left(self):
        # Turn left by moving Right motor Faster
        self.left_motor.forward()  
        self.right_motor.forward() 
        self.left_motor.value = 0.4  # Set left motor speed to 40%
        self.right_motor.value = 1  # Set right motor speed to 100%

    def turn_right(self):
        # Turn right by moving left motor Faster
        self.left_motor.forward() 
        self.right_motor.forward()  
        self.right_motor.value = 0.4  # Set right motor speed to 40%
        self.left_motor.value = 1  # Set left motor speed to 100%

    def stop_motors(self):
        self.left_motor.stop()  # Stop the left motor
        self.right_motor.stop()  # Stop the right motor

def get_key():
    # Read a single keypress without waiting for Enter
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == "__main__":
    robot = Robot()  # Create an instance of the Robot class
    try:
        while True:
            key = get_key()  # Get user input
            if key == 'w':
                robot.move_forward()  # Move forward if 'w' key is pressed
            elif key == 's':
                robot.move_backward()  # Move backward if 's' key is pressed
            elif key == 'a':
                robot.turn_left()  # Turn left if 'a' key is pressed
            elif key == 'd':
                robot.turn_right()  # Turn right if 'd' key is pressed
            else:
                robot.stop_motors()  # Stop motors for other keys
    except KeyboardInterrupt:
        robot.stop_motors()  # Stop motors on keyboard interrupt

