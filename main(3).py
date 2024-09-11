import motionsensor
import distancesensor
from engi1020.arduino.api import *
from time import sleep
import texttospeech
import Webscrapper 

button = 6
buzzer = 5
echo = 7
potentiometer = 0


#Steplength = distancesensor.calibratestep()
#texttospeech.say("your step length is" + str(Steplength) + "centimeters")
#print(Steplength)

while True:
    while analog_read(potentiometer) == 0:
        print(analog_read(potentiometer))
    # checks for stationary object and tells you how far away it is
        if digital_read(button) == True:
            distance = distancesensor.getdistance()
            if distance == False:
                texttospeech.say("no object detected")
            else:
                texttospeech.say("object" + str(distance) + "cm's away!")

    while analog_read(potentiometer) == 1023:
        print(analog_read(potentiometer))
        if digital_read(button) == True:
cm    # checks for moving object and tells you how fast it is moving
            value = motionsensor.checkmotion()
            if value == True:
                buzzer_frequency(buzzer, 200)
                sleep(2)
                buzzer_stop(buzzer)
                speed = distancesensor.getspeed()
                texttospeech.say("Motion detected going:" + str(speed) + "cm/s")
            else:
                texttospeech.say("no motion detected proceed with caution")

    while analog_read(potentiometer) < 1023 and analog_read(potentiometer) > 0:
    # gives directions to a location based on input from user
        if digital_read(button) == True:
            texttospeech.say("Input destination")
            destination = input("Input destination: ")
            texttospeech.say("Input current position")
            starting = input("input current position: ")
            Webscrapper.Getdirection(destination, starting, 0.5)
