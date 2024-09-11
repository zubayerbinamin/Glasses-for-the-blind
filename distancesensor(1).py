import time
from time import sleep
from engi1020.arduino.api import *

trig = 8
echo = 7
button = 6
buzzer = 5

def getdistance():
    """outputs the distance of the nearest object"""
    valid = True
    endtime = time.time() + 10
    while time.time() < endtime and valid:  #check for 10 seconds only
        distance = ultra_get_centimeters(echo)
        if distance != 0.0:   #only document if the distance is not 0.0
            valid = False
            break
        else:
            valid = True
    if time.time() > endtime: # if nothing in 10 seconds then there is no object
        distance = False
    return distance

def difaverage(calibrationlist):
    """outputs average difference between a list of measurements"""
    differences = []
    for i in range(len(calibrationlist)-1):
        difference = calibrationlist[i+1] - calibrationlist[i]
        differences.append(difference)
    average = sum(differences)/len(differences)
    return average
 
def calibratestep():
    """measures the length of the users step"""
    calibrationlist = []
    calibration = True
    while calibration:
        if digital_read(button) == True:
            sleep(1)
            if digital_read(button) == True:
    #long hold on button ends loop
                calibration = False
            else:  
                calibrationlist.append(getdistance())
                print(calibrationlist)
                buzzer_frequency(buzzer, 200)
                sleep(0.5)
                buzzer_stop(buzzer)
        else:
            calibration = True
    steplength = difaverage(calibrationlist)
    return steplength

def getspeed(timespan=5):
    """ calculates speed of an object assuming it is not accelerating"""
    distance1 = getdistance()
    sleep(timespan)
    distance2 = getdistance()
    speed = (distance2-distance1)/timespan
    return speed
