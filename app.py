from time import asctime
from flask import Flask, render_template, redirect, url_for
# import subprocess

import light

app = Flask(__name__)

@app.route("/")
def home():
    # sunrise()
    return render_template("base.html")

@app.route("/on")
def on():
    light.on()
    # light.utilities.update_grid(1)
    return redirect(url_for('home'))

@app.route("/off")
def off():
    light.off()
    # light.utilities.turn_off()
    return redirect(url_for('home'))

@app.route("/rise")
def rise():
    light.rise()
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(host="0.0.0.0")
