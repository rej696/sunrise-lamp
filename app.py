from time import asctime
from flask import Flask
import subprocess

app = Flask(__name__)

def sunrise():
    header = f"\nSunrise @ {asctime()}:\n"

    with open("/home/pi/sunrise-lamp/output.txt", "a+") as log:
        log.write(header)
        
        with open("/home/pi/sunrise-lamp/error.txt", "a+") as err:
            err.write(header)
            
            subprocess.Popen(["python3", "sunrise.py"], stdout=log, stderr=err)



@app.route("/")
def hello():
    sunrise()
    
    return "Hi Sally, hope you are enjoying your lamp"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
