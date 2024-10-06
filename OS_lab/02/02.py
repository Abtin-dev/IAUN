import threading as th
from time import sleep
from colorama import Back, Style
from random import randint, choice
import numpy as np

Buffer_size:int = 5
Buffer = np.zeros(Buffer_size, dtype=int) #Array of 0

_in:int = 0
_out:int = 0
lock = th.Lock()

# empty = -1, full = 1
def Buffer_chek(_in, _out):
    """
    check the Buffer status
    """
    if _in == _out:
        return -1
    elif ((_in + 1)%Buffer_size )== _out:
        return 1



def adder():
    """
    Add a random number to the Buffer
    """
    global Buffer, _in, _out
    i = 0
    while True:
        with lock:
            _in, _out = _in%Buffer_size, _out%Buffer_size
            i += 1
            if Buffer_chek(_in, _out) != 1:
                rand = randint(1,100)
                Buffer[_in] = rand
                print(f"write {rand} in {_in} ::: {Buffer}")
                _in += 1
            elif Buffer_chek(_in, _out) == 1:
                print(Back.RED + f"Buffer is full ::: {Buffer}"+Style.RESET_ALL)
        sleep(choice([0.9, 0.2, 0.3]))



def remover():
    """
    Read from Buffer
    """
    global Buffer, _in, _out
    i = 0
    while True:
        with lock:
            _in, _out = _in%Buffer_size, _out%Buffer_size
            i += 1
            if Buffer_chek(_in, _out) != -1:
                print(f"Read {Buffer[_out]} from {_out} ::: {Buffer}")
                Buffer[_out] = 0
                _out += 1
            elif Buffer_chek(_in, _out) == -1:
                print(Back.RED + f"Buffer is empty :::: {Buffer}" + Style.RESET_ALL)
        sleep(choice([1, 0.8, 0.2]))

def main():
    th.Thread(target=adder).start()
    th.Thread(target=remover).start()


if __name__ == "__main__":
    main()
