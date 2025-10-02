# https://realpython.com/intro-to-python-threading/#working-with-many-threads
import threading
import time
import random

def func(name):
    d = random.randint(1,6)
    print(f'func {name} rodando, esperar: {d}')
    time.sleep(d)
    
x = threading.Thread(target=func, args=(1,))
x.start()