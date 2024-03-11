'''
Move mouse cursor by 1 pixel every 25 minutes to prevent computer from going into sleep mode
'''

from time import sleep
from pyautogui import move

while True:
  move(1,1)
  sleep(1500)
