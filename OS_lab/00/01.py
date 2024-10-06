from colorama import Back, Style
import threading as th

def pritn_name():
    while True:
        print(Back.GREEN + "Abtin " + Style.RESET_ALL)
        

def pritn_last_name():
    while True:
        print(Back.RED + "dev" + Style.RESET_ALL)
        


def run():
    th.Thread(target=pritn_name).start()
    th.Thread(target=pritn_last_name).start()

run()
