from gpiozero import Motor  # Import the Motor class from gpiozero library
import time  # Import the time module

class Robot:
    def __init__(self):
        # Initialize motor pins
        self.left_motor = Motor(forward=5, backward=6, enable=12)  # Create a left motor instance
        self.right_motor = Motor(forward=27, backward=22, enable=13)  # Create a right motor instance

    def move_forward(self):
        # Move both motors forward at half speed
        self.left_motor.forward()
        self.right_motor.forward()
        self.right_motor.value = 0.5
        self.left_motor.value = 0.5

    def move_backward(self):
        # Move both motors backward at a slower speed
        self.left_motor.backward()
        self.right_motor.backward()
        self.right_motor.value = 0.3
        self.left_motor.value = 0.3
        
    def turn_left(self):
        # Turn left by adjusting motor speeds
        self.left_motor.backward()
        self.right_motor.forward()
        self.right_motor.value = 0.55
        self.left_motor.value = 0.3

    def turn_right(self):
        # Turn right by adjusting motor speeds
        self.left_motor.forward()
        self.right_motor.backward()
        self.right_motor.value = 0.3
        self.left_motor.value = 0.55

    def stop_motors(self):
        # Stop both motors
        self.left_motor.stop()
        self.right_motor.stop()

if __name__ == "__main__":
    robot = Robot()  # Create an instance of the Robot class
    try:
        while True:
            user_input = input("Enter command (w/a/s/d): ")  # Get user input
            if user_input == 'w':
                robot.move_forward()  # Move forward
            elif user_input == 's':
                robot.move_backward()  # Move backward
            elif user_input == 'a':
                robot.turn_left()  # Turn left
            elif user_input == 'd':
                robot.turn_right()  # Turn right
            else:
                robot.stop_motors()  # Stop motors
            time.sleep(0.1)  # Add a small delay to avoid excessive CPU usage
    except KeyboardInterrupt:
        robot.stop_motors()  # Stop motors on keyboard interrupt

