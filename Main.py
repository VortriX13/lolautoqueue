import pyautogui
import time
import colorama
from colorama import Fore
import datetime

colorama.init()
def currenttime():
    now = datetime.datetime.now()
    current_time = now.strftime("[%H:%M:%S]")
    print(Fore.CYAN +"in :",Fore.YELLOW + current_time, end="")
    
def welcome():
    print(Fore.LIGHTGREEN_EX + "you can close this window when its done")
    print(Fore.RED + "@author: not a comrade")
    print(Fore.RED + "@version: 1.1")
    print(Fore.LIGHTGREEN_EX + "")
    time.sleep(1)

def queue_detect():
    coord = pyautogui.locateCenterOnScreen('aceitar.jpg', confidence=0.7)
    if coord != None:
        pyautogui.click(coord)
        print(Fore.GREEN + "| [+] Found! ",end="")
        currenttime()
        print(Fore.GREEN + " |")
        time.sleep(4)      
    else:
        None

welcome()
print(Fore.MAGENTA + "[!] Searching")
while True:
    queue_detect()
    time.sleep(0.5)  
