import os, time
os.system('clear && pip install colorama && pkg install toilet -y && clear')
from colorama import Fore, Style
print ('\n')
def res():
    print(Style.RESET_ALL)
os.system('clear')
while True:
    print(Fore.CYAN + ' '+Style.BRIGHT)
    print(' ╔═══╗╔═══╗╔═══╗╔══╗╔═══╗╔═╗─╔╗╔═══╗╔═══╗')
    print(' ╚╗╔╗║║╔══╝║╔═╗║╚╣─╝║╔═╗║║║╚╗║║║╔══╝║╔═╗║')
    print(' ─║║║║║╚══╗║╚══╗─║║─║║─╚╝║╔╗╚╝║║╚══╗║╚═╝║')
    print(' ─║║║║║╔══╝╚══╗║─║║─║║╔═╗║║╚╗║║║╔══╝║╔╗╔╝')
    print(' ╔╝╚╝║║╚══╗║╚═╝║╔╣─╗║╚╩═║║║─║║║║╚══╗║║║╚╗')
    print(' ╚═══╝╚═══╝╚═══╝╚══╝╚═══╝╚╝─╚═╝╚═══╝╚╝╚═╝')
    print(Fore.GREEN+' '+Style.BRIGHT)
    print(' [1] ')
    print(' [2] ')
    print(' [3] ')
    print(' [4] ')
    print(' ')
    print(' [0] выход')
    print(Fore.BLUE+' '+Style.BRIGHT)
    inp = input (' Выбери пункт>>> ')
    os.system('clear')
    res()

    if inp =='0':
        os.system('clear')
        print(Fore.CYAN + ' '+Style.BRIGHT)
        print('Спасибо за использование')
        res()
        break

    else:
        res()
        os.system('clear')
        print(Fore.RED+'не верный пункт')
