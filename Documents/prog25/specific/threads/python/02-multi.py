import threading
import time
import random

def func(name):
    d = random.randint(1,6)
    print(f'func {name} rodando, esperar: {d}')
    time.sleep(d)
    print(f"func {name} concluída")

threads = list()

for i in range(3):
    x = threading.Thread(target=func, args=("f"+str(i),))
    threads.append(x)
    x.start()

for t in threads:
    t.join()

print("END!")