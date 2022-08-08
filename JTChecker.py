import json
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
                                     [4] Info About Discord Token
                                     [5] Single Discord Token Leaver
                                     [6] Multi Discord Token Leaver
                                     [7] Exit
                                     Enter Your Choice: """)
    if choice == "1":
        single()
    elif choice == "2":
        multi()
    elif choice == "3":
        login()
    elif choice == "4":
        info()
    elif choice == "5":
        leavers()
    elif choice == "6":
        leaver()
    elif choice == "7":
        sys.exit
    else:
        print("Enter Right Choice")
        time.sleep(3)
        os.system('cls')
        menu()



def single():
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
        }   44
        """
   driver.execute_script(script + f'login("{token}")')
   while True:
    os.system('cls')
    time.sleep(3)
    print(Fore.GREEN + "SucessFully Logined As" + token)
    time.sleep(3)
    os.system('cls')
    menu()



def info():
    token = input("Enter Your Discord Token Here:")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    check = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    print(Fore.YELLOW + "Please Wait 3 Secs We Are Fetching The Info For:"+ Fore.LIGHTCYAN_EX + token)
    time.sleep(3)
    if check.status_code == 200:
        userName = check.json()['username']  + check.json()['discriminator']
        id = check.json()['id']
        phone = check.json()['phone']
        email = check.json()['email']
        avatar_id = check.json()['avatar']
        has_nitro = False
        checks = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
        nitro_data = checks.json()
        has_nitro = bool(len(nitro_data) > 0)
        print(f'''
        {Fore.YELLOW}Token:{Fore.RESET}{Fore.LIGHTCYAN_EX} {token} {Fore.RESET}
        {Fore.YELLOW}ID:{Fore.RESET}{Fore.LIGHTCYAN_EX} {id} {Fore.RESET}
        {Fore.YELLOW}Username:{Fore.RESET}{Fore.LIGHTCYAN_EX}{userName} {Fore.RESET}
        {Fore.YELLOW}Avatar-Id:{Fore.RESET}{Fore.LIGHTCYAN_EX}{avatar_id} {Fore.RESET}
        {Fore.YELLOW}Email:{Fore.RESET}{Fore.LIGHTCYAN_EX} {email}  {Fore.RESET}
        {Fore.YELLOW}Phone Number:{Fore.RESET}{Fore.LIGHTCYAN_EX}  {phone if phone else "No Phone Number Was Found On The Account"} {Fore.RESET}
        {Fore.YELLOW}Nitro:{Fore.RESET}{Fore.LIGHTCYAN_EX} {has_nitro if has_nitro else "The Account Dosent Have Nitro"} {Fore.RESET}
            ''')
        input()
    exit = input(Fore.CYAN + "Would You Like To Exit y/n:")
    if exit == "y":
        os.system('cls')
        time.sleep(2)
        print(Fore.GREEN + "Thank You For Using JTChecker")
        time.sleep(3)
        sys.exit()
    elif exit == "n":
        os.system('cls')
        time.sleep(2)
        print(Fore.CYAN +'You Are Know Going Back To The Menu')
        time.sleep(3)
        os.system('cls')
        menu()

       
def leavers():
    token = input(Fore.LIGHTCYAN_EX + 'Enter Discord Token:')
    print(Fore.GREEN + "Leaving All Discord Servers")
    id = requests.get("https://discord.com/api/v9/users/@me/guilds", headers={'Authorization': token}).json()
    for guild in id:
            requests.delete(
                    f'https://discord.com/api/v9/users/@me/guilds/'+guild['id'],
                    headers={'Authorization': token})
            time.sleep(2)
            print(Fore.GREEN + "{} Has Left The. All There Servers".format(token.strip("\n")))


        

def leaver():
    name = input(Fore.LIGHTCYAN_EX + "Enter The Name Of The Txt File:")
    file = open(name, "r").read().split('\n')
    left = open('left.txt', 'w')
    for token in file:
        tokens = token.strip("\n")
        print(Fore.GREEN + "Leaving All Discord Servers")
        id = requests.get("https://discord.com/api/v9/users/@me/guilds", headers={'Authorization': token}).json()
        for guild in id:
            requests.delete(
                    f'https://discord.com/api/v9/users/@me/guilds/'+guild['id'],
                    headers={'Authorization': token})
            print(Fore.GREEN + "{} Has Left The. All There Servers".format(token.strip("\n")))
    

def exit():
    sys.exit


menu()
