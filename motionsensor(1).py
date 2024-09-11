from engi1020.arduino.api import *
import time

motionsensor = 2

def checkmotion():
    """ checks if any motion for 5 seconds after function is called"""
    state = False
    endtime = time.time() + 5
    while time.time() < endtime:
        state2 = digital_read(motionsensor)
        if state2 != state:
            if state2 == True:
                #motion detected
                break
            else:
                pass           
        else:
            pass 
        state = state2
    return state2
