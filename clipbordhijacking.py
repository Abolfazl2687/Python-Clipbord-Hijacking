import pyperclip
import time
import os

os.system("title Dark-Programmer && color 02 && cls")

list = []
while True:

    if pyperclip.paste() != 'None':
        value = pyperclip.paste()

    if value not in list:

        list.append(value)

        print("Hacked Texts : "+str(list)+" || Dark-Programmer " , end= "\r")

    time.sleep(3)
