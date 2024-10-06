"""
OS_lab
Session 0

"""
from time import *
from threading import *


print("############################## first code ################################")

def task()->None:
    print("Task started ...")
    sleep(1)
    print("Task finished ...")

started_time:float = time()
task()
task()
final_time:float = time()
print(f"task takes {final_time - started_time} seconds")

print("############################## second code #############################")

t1:object = Thread(target=task)
t2:object = Thread(target=task)

started_time:float = time()

t1.start()
t2.start()

t1.join()
t2.join()

final_time:float = time()
print(f"task takes {final_time - started_time} seconds")

print("############################## homework #############################")

sleep(3)

def print_name()->None:
    while True:
        print("my name")
        sleep(0.01) #  sleep for better performance

def print_last_name()->None:
    while True:
        print("\x1b[91mmy last name \x1b[0m") # color set to red
        sleep(0.01)

T1:object = Thread(target=print_name)
T2:object = Thread(target=print_last_name)

T1.start()
T2.start()
