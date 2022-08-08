

import time
import requests
import os
import colorama
from colorama import Fore
from selenium import webdriver
import sys
os.system(f'cls & mode 125,35 & title JTChecker!')


def main():
    menu()


def menu():
    choice = input(Fore.LIGHTCYAN_EX  +  """
 
        ▄█     ███      ▄████████    ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
    ███ ▀█████████▄ ███    ███   ███    ███     ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
    ███    ▀███▀▀██ ███    █▀    ███    ███     ███    █▀  ███    █▀    ███▐██▀     ███    █▀    ███    ███ 
    ███     ███   ▀ ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ███     ███     ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
    ███     ███     ███    █▄    ███    ███     ███    █▄  ███    █▄    ███▐██▄     ███    █▄  ▀███████████ 
    ███     ███     ███    ███   ███    ███     ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
█▄ ▄███    ▄████▀   ████████▀    ███    █▀      ██████████ ████████▀    ███   ▀█▀   ██████████   ███    ███ 
▀▀▀▀▀▀                                                                  ▀                        ███    ███ 
                                       Made By Jose#0001 
                                        
                                     [1] Check Single Discord Token 
                                     [2] Check Multi Discord Tokens 
                                     [3] Discord Token Login
                                     [4] Exit
                                    Enter Your Choice: """)
    if choice == "1":
        single()
    elif choice == "2":
        multi()
    elif choice == "3":
        login()
    elif choice == "4":
        exit
    else:
        print("Enter Right Choice")
        time.sleep(3)
        os.system('cls')
        menu()



def single():
  print(Fore.YELLOW + "This Is A Single Discord Token Checker")
  token = input(Fore.LIGHTCYAN_EX + "Enter The Token You Wanna Check:")
  headers = {'Content-Type': 'application/json', 'authorization': token}
  check = requests.get(f"https://discordapp.com/api/v9/users/@me", headers=headers)
  if check.status_code == 200:
    print(Fore.GREEN + "Discord Token Is Valid")
    time.sleep(2)
    os.system('cls')
    menu()
  
  elif check.status_code == 403:
    print(Fore.MAGENTA + "Discord Token Is Locked")
    time.sleep(2)
    os.system('cls')
    menu()


  else:
    print(Fore.RED + "Discord Token Is Invalid")
    time.sleep(2)
    os.system('cls')
    menu()






def multi():
    print(Fore.YELLOW + "This Will Checks Multiple Discord Tokens")
    name = input(Fore.LIGHTCYAN_EX + "Enter The Name Of The Txt File:")
    file = open(name, "r").read().split('\n')
    Valid = open('Valid.txt', 'w')
    Invalid = open('Invalid.txt', 'w')
    Locked = open('Locked.txt', 'w')
    for line in file:
        tokens = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': tokens}
        check = requests.get(f"https://discordapp.com/api/v9/users/@me", headers=headers)
        if check.status_code == 200:
            print(Fore.GREEN + "{} Token Is Valid.".format(line.strip("\n")))
            time.sleep(1)
            Valid.write(f'{line}\n')
        
        elif check.status_code == 403:
             print(Fore.MAGENTA + "{} Token Is Locked.".format(line.strip("\n")))
             time.sleep(1)
             Locked.write(f'{line}\n')
    
     
        else:
            print(Fore.RED + "{} Token Is Invalid.".format(line.strip("\n")))
            time.sleep(1)
            Invalid.write(f'{line}\n')






def login():
   token = input('Enter The Token You Want To Login Into:')
   driver = webdriver.Chrome('chromedriver.exe')
   driver.get('https://discord.com/login')
   script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   
        """
   driver.execute_script(script + f'login("{token}")')
   while True:
    print(Fore.GREEN + "SucessFully Logined As" + token)
   



def exit():
    sys.exit

menu()
