"""
This is a python program that starts the countdown when the button is pressed. The LED should blink at
regular intervals, and the buzzer should sound when the countdown reaches zero.
This Countdown Timer project is an excellent way to learn about
•timing events,
• digital inputs, and outputs.
• It can be used in various applications, such as;
• time management,
•Cooking,
•games, etc.
authour samantha bochaberi
"""
import time
from time import sleep
from gpiozero import Button,LED,Buzzer
button = Button(2)
led = LED(4)
buzz = Buzzer(3)
my_time =int(input("number of seconds for count down "))#prompts user to input time in seconds
button.wait_for_press()#makes function to wait for button to be executed
while True:
    if button.is_pressed:
        for x in range(0,my_time):#iterates for the number of seconds inputed
            led.on()
            sleep(1)
            led.off()
            sleep(1)
            
        print("times up")    
        buzz.on()
        sleep(2)
        buzz.off()
        sleep(2)
    else:
        break