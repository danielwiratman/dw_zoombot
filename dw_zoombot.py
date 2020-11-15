import subprocess
import pyautogui as pg
import time
import cv2
import csv
from datetime import datetime

def sign_in(meetid, pswrd):
    subprocess.call("C:/Users/Daniel Wiratman/AppData/Roaming/Zoom/bin/Zoom.exe")
    time.sleep(3)

    joinbutton = pg.locateOnScreen(r'join.png', confidence=0.8)
    pg.moveTo(joinbutton)
    pg.click()
    time.sleep(1)

    mIDbutton = pg.locateOnScreen(r'mID.png', confidence=0.8)
    pg.moveTo(mIDbutton)
    pg.click()
    pg.write(meetid)
    pg.press('Enter')
    time.sleep(1)

    passbutton = pg.locateOnScreen(r'passcode.png', confidence=0.8)
    pg.moveTo(passbutton)
    pg.click()
    pg.write(pswrd)
    pg.press('Enter')

## For Testing
# sign_in('5775778888','cube')

file_link = open("link_kelas.csv", 'r')
csvreader = csv.reader(file_link)
datainlistform = list(csvreader)[1:]

## For Time Purposes
# listdatetime = datetime.strptime(datainlistform[-1][-2],"%H:%M:%S")
# while True:
#     datetimenow = datetime.now()
#     if listdatetime.hour == datetimenow.hour and datetimenow.minute == listdatetime.minute:
#        #sign_in(datainlistform[-1][0],datainlistform[-1][1])
#        break
#     time.sleep(1)

# Printing
import os
os.system('cls')
print('     __________________________________________')
print('    |')
print("    | WELCOME TO DANIEL'S ZOOMBOT")
print("    | Select Room:")
for i in datainlistform:
    className = i[-1]
    print("    |",str(datainlistform.index(i) + 1)+')',className)
print("    |__________________________________________")
print()
myInput = int(input('    Type Room Index: '))-1
myMID = datainlistform[myInput][0]
myPswd = datainlistform[myInput][1]

sign_in(myMID,myPswd)
