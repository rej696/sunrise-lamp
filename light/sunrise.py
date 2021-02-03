from time import sleep, time
try:
    from light.utilities import update_grid, turn_off
except ModuleNotFoundError:
    from utilities import update_grid, turn_off

def sunrise(maxtime:int = 30, steps:int = 100):
    turn_off()

    start_time = time()

    for step in range(0, steps):
        brightness = pow(2, (step / steps)) - 1
        update_grid(brightness)
        sleep(maxtime/steps)
        # sleep((pow(2, ((steps - step) / steps)) -1))
        print(f"{step}: {time() - start_time}s")

if __name__ == "__main__":
    # parse arguments for maxtime (in seconds) and steps etc.
    sunrise()
