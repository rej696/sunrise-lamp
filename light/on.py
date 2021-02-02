import getopt
import sys
from time import sleep

try:
    from utilities import update_grid
except ModuleNotFoundError:
    from light.utilities import update_grid

def on(brightness=None):
    if brightness is not None:
        print(f"Turn on light with brightness at {brightness}%")
        update_grid(brightness=(brightness/100))
    else:
        print("No correct value for brightness supplied, using default value of 100%")
        update_grid(brightness=1)

    
if __name__ == "__main__":
    brightness = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["brightness="])
    except getopt.GetOptError:
        pass
    else:
        for opt, arg in opts:
            if opt == "--brightness":
                try:
                    brightness = int(arg)
                except ValueError:
                    print(f"value of brightness is not a int out of 100: {arg}")
