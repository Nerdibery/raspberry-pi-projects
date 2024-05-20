#raspberry pi based alarm system
#expected outcome - when button is pressed the buzzer goes off ad the leed blinks for 5 seconds
#led blinks at a 10hz frequency
#author bochaberi samantha 
"""
• It can be used in various applications, such as;
• Home Security – Panic alarms are often integrated into home security
systems to alert authorities in case of a break-in or other emergencies.
Linux Learning Centre Ltd.
• Medical emergencies – They can be used to signal for help in medical
situations, such as falls or health crises, especially for the elderly or
those with medical conditions.
• Personal safety – individuals can carry panic alarms to alert others if
they are in danger, such as in cases of assault or when feeling
threatened.
• Workplace security – in offices, such alarms can be installed under
desks or in hidden locations to discreetly notify security personnel
during incidents like robberies or intrusions
"""
import time
from time import sleep
from gpiozero import Button,LED,Buzzer
button = Button(2)
led = LED(4)
buzz = Buzzer(3)
button.wait_for_press()
while True:
    if button.is_pressed:
        buzz.on()
        for i in range(50):#calculate to get 10Hz
            print(i)
            led.on()
            sleep(0.05)
            led.off()
            sleep(0.05)
        #sleep(5)
        buzz.off()
        #sleep(5)
        
    else:
        break
        

"""
import gpiozero
import time
if gpiozero.Button(2).is_pressed():
    gpiozero.Buzzer(3).on()
    time.sleep(5)
    end_time = time()+5#adds duration to time function(source stack overflow)
    while time() < end_time:
        gpiozero.LED(4).on()
        time.sleep(0.1)
        gpiozero.LED(4).off
        time.sleep(0.1)
        """
 