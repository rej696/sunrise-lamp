from multiprocessing import Process
from . import utilities
from .on import on as _on
from .sunrise import sunrise as _rise

OUTPUT="/home/pi/sunrise-lamp/output.txt"
ERR="/home/pi/sunrise-lamp/error.txt"

PROCESS=Process()

def process_wrapper(func, **kwargs):
    from time import asctime
    global PROCESS
    # if PROCESS.is_alive():
        # PROCESS.join()
        # PROCESS.kill()
    PROCESS = Process(target=func, kwargs=kwargs)
    PROCESS.start()
    print(f"{func.__name__} @ {asctime()}")
#     header = f"\n{func} @ {asctime()}:\n"
#     command = ["python3", f"light/{func}"]
#     if kwargs:
#         for key in kwargs:
#             command.append(f"--{key}")
#             command.append(f"{kwargs[key]}")
# 
#     with open(OUTPUT, "a+") as log:
#         log.write(header)
#         with open(ERR, "a+") as err:
#             err.write(header)
#             subprocess.Popen(command, stdout=log, stderr=err)

def on(brightness=100):
    process_wrapper(_on, brightness=brightness)

def off():
    process_wrapper(utilities.turn_off)

def rise(maxtime=30, steps=100):
    process_wrapper(_rise, maxtime=maxtime, steps=steps)
            
