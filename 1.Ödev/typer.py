import pyautogui as pr
import random
import names
import time
import os

os.startfile(r"C:\Users\OEM\Ödev\1.ödev\liste.exe")
time.sleep(4)
for i in range(1,40):
    pr.write("%r" % (i))
    time.sleep(1)
    pr.press("enter")
    pr.write(names.get_full_name().replace("''",""))
    time.sleep(1)
    pr.press("enter")
    pr.write('%r' % (random.randint(1,100)) )
    time.sleep(1)
    pr.press("enter")
    time.sleep(1)
    pr.write('%r' % (random.randint(1,100)) )
    pr.press("enter")
    time.sleep(1)