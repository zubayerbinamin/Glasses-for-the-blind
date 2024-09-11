from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import texttospeech
from engi1020.arduino.api import *

def Getdirection(Destination, Starting, Steplength = 50):
    # assign url in the webdriver object
    #Steplength = Steplength/100
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/maps/@47.5741098,-52.735359,15z")
    sleep(1)

    # search locations
    Place = driver.find_element(By.CLASS_NAME, "searchboxinput")
    Place.send_keys(Destination)
    Submit = driver.find_element(
        By.XPATH, "/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button")
    Submit.click()
    sleep(3.5)

# get directions
    directions = driver.find_element(
        By.XPATH, "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/span")
    directions.click()
    sleep(1)

# find place
    find = driver.find_element(
        By.XPATH, "/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.send_keys(Starting)
    search = driver.find_element(
        By.XPATH, "/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
    sleep(1)


# choose walk 
    walk_button = driver.find_element(
        By.XPATH, "/html/body/div[3]/div[8]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[4]/button/img")
    walk_button.click()
    sleep(1)


# choose first recommended route
    route_button = driver.find_element(
        By.XPATH, "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[4]/button/span")
    route_button.click()
    sleep(1)


# get route details

    Route_Description = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[5]/div/div/div/div/div[2]/div[1]/div[2]/div/div")
    Direction = Route_Description.text.splitlines()
    Direction.pop(-2)
    for i in range(1, len(Direction), 2):
        r = Direction[i]
        if r[-2] == 'k':
#             r = r.replace('km', '') #CANNOT USE REPLACE DIRECTLY WITH XPATH, YOU NEED LOOP
            r = [i.replace('k', '') for i in r]
            r = [i.replace('m', '') for i in r]
            r = ''.join(r)
            r = float(r)
            r = r*1000
            numSteps = r/Steplength
            numSteps = str(int(numSteps)) + " steps"
            Direction[i] = numSteps
        else:
#             r = r.replace('m', '') #CANNOT USE REPLACE DIRECTLY WITH XPATH, YOU NEED LOOP
            r = [i.replace('m', '') for i in r]
            r = ''.join(r)
            r = float(r)
            numSteps = r/Steplength
            numSteps = str(int(numSteps)) + " steps"
            Direction[i] = numSteps
    print(Direction)
    v = 0
    while True:
        if digital_read(6) == True:
            texttospeech.say(str(Direction[v]) + str(Direction[v+1]))
            v = v + 2
            if v == len(Direction): #to make sure it doesn't go out of bounds
                break
            sleep(1)
    sleep(1)

Getdirection("Avalon Mall", "Mun university center", 0.5)

