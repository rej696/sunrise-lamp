from time import sleep, time
import scrollphathd as sphd

def turn_off():
    sphd.clear()
    sphd.show()

def update_grid(brightness:int = 0):
    for y in range(7):
        for x in range(17):
            sphd.set_pixel(x, y, brightness)
    sphd.show()

def rise(maxtime:int = 30, steps:int = 100):
    turn_off()
    
    start_time = time()

    for step in range(0, steps):
        brightness = pow(2, (step / steps)) - 1
        update_grid(brightness)
        sleep(maxtime/steps)
        # sleep((pow(2, ((steps - step) / steps)) -1))
        print(f"{step}: {time() - start_time}s")
    turn_off()

if __name__ == "__main__":
    rise(10, 100)
