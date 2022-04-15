import os, time
os.system('clear && pip install colorama && pkg install toilet -y && clear')
from colorama import Fore, Style
print ('\n')
def res():
    print(Style.RESET_ALL)
os.system('clear')
while True:
    print(Fore.CYAN + ' ')
    print(Style.BRIGHT + ' ')
    print(' ╔═══╗╔═══╗╔═══╗╔══╗╔═══╗╔═╗─╔╗╔═══╗╔═══╗')
    print(' ╚╗╔╗║║╔══╝║╔═╗║╚╣─╝║╔═╗║║║╚╗║║║╔══╝║╔═╗║')
    print(' ─║║║║║╚══╗║╚══╗─║║─║║─╚╝║╔╗╚╝║║╚══╗║╚═╝║')
    print(' ─║║║║║╔══╝╚══╗║─║║─║║╔═╗║║╚╗║║║╔══╝║╔╗╔╝')
    print(' ╔╝╚╝║║╚══╗║╚═╝║╔╣─╗║╚╩═║║║─║║║║╚══╗║║║╚╗')
    print(' ╚═══╝╚═══╝╚═══╝╚══╝╚═══╝╚╝─╚═╝╚═══╝╚╝╚═╝')
    res()
    





    inp = input (' Выбери пункт>>> ')
    os.system('clear')
    
    if inp =='0':
        res()
        os.system('clear')
        print('Спасибо за использование')
        break

    else:
        res()
        os.system('clear')
        print(Fore.RED+'не верный пункт')
