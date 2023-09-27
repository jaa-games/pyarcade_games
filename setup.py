import time
import sys
import os

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

print("pyArcade Games Installing Started ✌️")
poetry_command_1='curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -'
poetry_command_2='poetry install'
if os.name in ('nt', 'dos'):
    poetry_command_1='(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -'
    poetry_command_2='poetry install'
    print('Installing Poetry')
    time.sleep(3)
    os.system(poetry_command_1)
    print('Installing Poetry Dependencies')
    time.sleep(3)
    os.system(poetry_command_2)
print("🐢🐢🐢🐢🐢🐢🐢🐢🐢") 
print('Installing Poetry')
print("🐢🐢🐢🐢🐢🐢🐢🐢🐢") 
time.sleep(3)
os.system(poetry_command_1)
print("🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢") 
print('Installing Poetry Dependencies')
print("🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢") 
os.system(poetry_command_2)
print("--------------------------------------------------")


from colorama import Fore, Style
import pyfiglet
end_message = Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("The setup Finished")

print(end_message)

decison=input("Do You want to run the game ? y or n \n")
if decison=='y':
    clear_console()
    os.system('poetry run python -m main')
elif decison=='n':
    clear_console()
    os.system('sys.exit()')



