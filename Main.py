import sys
import pyautogui
import time
import colorama
from colorama import Fore
import datetime

# 
colorama.init()

def time_now():
    now = datetime.datetime.now()
    current_time = now.strftime('[%H:%M:%S]')
    print('em ' + current_time, end='')
    
def welcome():
    print(Fore.LIGHTRED_EX + '''            
                                    _        _           _   
   ___ ___  _ __ ___  _ __ __ _  __| | ___  | |__   ___ | |_ 
  / __/ _ \| '_ ` _ \| '__/ _` |/ _` |/ _ \ | '_ \ / _ \| __|
 | (_| (_) | | | | | | | | (_| | (_| |  __/ | |_) | (_) | |_ 
  \___\___/|_| |_| |_|_|  \__,_|\__,_|\___| |_.__/ \___/ \__|                                                                       
''')
    print(Fore.LIGHTRED_EX + '- @author: not a comrade ')
    print(Fore.LIGHTRED_EX + '- @version: 1.3 ')
    print(Fore.LIGHTGREEN_EX + '''
          - Para garantir que o bot vai funcionar corretamente
          - reinicie o lol e não mude a janela de lugar!
          ''')
    time.sleep(1)
    print(Fore.YELLOW + '- [!] Procurando ', end='\n')
    print('')
    time.sleep(1)
    print(Fore.MAGENTA + '''- [!] Atenção: 
se você quiser que o bot escolha/bana um campeão,
escreva o nome corretamente dos campeões abaixo,
caso contrario deixe em branco.
          ''')

def queue_detect():
        coord = pyautogui.locateCenterOnScreen('aceitar.jpg', confidence=0.7)
        if coord != None:
            pyautogui.click(coord)
            print(Fore.GREEN + '- [+] Aceito! ',end='')
            time_now()
            print(Fore.GREEN + ' ')
            time.sleep(2)

welcome()
time.sleep(2)
   
print(Fore.CYAN + 'Escolha seu campeão:',end='\n')
pick = input('>>')

print(Fore.RED + 'Escolha seu ban:',end='\n')
ban = input('>>')

def ban_cham():
    bancoord = pyautogui.locateCenterOnScreen('ban.jpg', confidence=0.8)
    if bancoord != None:
        search = pyautogui.locateCenterOnScreen('search.jpg', confidence=0.65)
        pyautogui.moveTo(search)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write(ban)
        time.sleep(0.5)
        pyautogui.moveTo(700,325)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(958,758)
        time.sleep(1)
        pyautogui.click()
    else:
        pass

def pick_cham():
    pickcoord = pyautogui.locateCenterOnScreen('pick.jpg', confidence=0.8)
    if pickcoord != None:
        search = pyautogui.locateCenterOnScreen('search.jpg', confidence=0.65)
        pyautogui.moveTo(search)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write(pick)
        time.sleep(0.5)
        pyautogui.moveTo(700,325)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(958,758)
        time.sleep(1)
        pyautogui.click()
    else:
        pass

def main_loop():
    while True:
        queue_detect()
        time.sleep(0.5)
        ban_cham()
        time.sleep(0.5)
        pick_cham()
        time.sleep(0.5)
main_loop()
