import subprocess
import pyautogui as pg
import time
import cv2
import csv
import os

def sign_in(meetid, pswrd):
    subprocess.call("C:/Users/Daniel Wiratman/AppData/Roaming/Zoom/bin/Zoom.exe") #Ganti dengan directory ZOOM ya..
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

file_link = open("link_kelas.csv", 'r')
csvreader = csv.reader(file_link)
datainlistform = list(csvreader)[1:]

# Printing
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
