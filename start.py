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
    
    if inp =='1':
        print(Fore.GREEN + ' '+Style.BRIGHT)
        print(' Дизайн: '+Fore.CYAN + ' '+Style.BRIGHT+'  ')
        print(Fore.GREEN+' '+Style.BRIGHT)
        print(' [1] предпосмотр')
        print(' [2] установить')
        print(' [0] назад')
        print(Fore.BLUE+' '+Style.BRIGHT)
        inp_1 = input (' Выбери пункт>>> ')
        os.system('clear')
        res()
        if inp_1 =='1':
        os.system('clear')

        if inp_1 =='2':
        os.system('clear')

        else:
            os.system('clear')

    if inp =='0':
        os.system('clear')
        print(Fore.CYAN + ' '+Style.BRIGHT)
        print('Спасибо за использование')
        res()
        break

    else:
        res()
        os.system('clear')
        print(Fore.RED+'выбранный вами пункт не верный')
