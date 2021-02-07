from flask import Blueprint, render_template, redirect, url_for, request, flash

import light
from sunrise_lamp.db import get_db
from sunrise_lamp.auth import login_required

bp = Blueprint('lamp', __name__)


# "/"
# show state of lamp
# set state of lamp (turn on and off, set rgb)
# commit state to database

# "/alarm"
# show state of current alarms
# edit alarm
# commit new alarm ton database
# redirect to "/"

@bp.route("/", methods=("GET", "POST"))
@login_required
def index():
    """Main view, set and display light current light status"""
    db = get_db()

    if request.method == "POST":
        try:
            brightness = int(request.form["brightness"])
            red = int(request.form["red"])
            green = int(request.form["green"])
            blue = int(request.form["blue"])
        except ValueError:
            brightness = -1
            red = -1
            green = -1
            blue = -1

        if brightness not in range(101):
            error = "Brightness must be a percentage value (0 - 100)"
        elif (red not in range(256)
              or green not in range(256)
              or blue not in range(256)):
            error = "rgb values must be in the range 0 - 255"
        else:
            error = None

        if error is None:
            db.execute(
                """update light set brightness = ?,
                red = ?, green = ?, blue = ?""",
                (brightness, red, green, blue)
            )
            db.commit()

            # call function to turn on light
            # or implement light code here?
            light.on()

            return redirect(url_for("lamp.index"))

        flash(error)
    
    # get lamp state from database
    state = db.execute("select * from light").fetchone()

    return render_template("lamp/index.html",
                           brightness=state["brightness"],
                           red=state["red"],
                           green=state["green"],
                           blue=state["blue"])

#TODO implement alarm view
#TODO implement html for alarm and index view
#TODO correct interface between light control and flask
@bp.route("/on")
@login_required
def alarm():
    light.on()
    db = get_db()
    # write state of lamp to database
    db.execute(
        "update lamp set brightness = ?, red = ?, green = ?, blue = ? where id = 0;",
        (brightness, red, green, blue)
    )
    db.commit()
    # light.utilities.update_grid(1)
    return redirect(url_for('home'))


@bp.route("/off")
@login_required
def off():
    light.off()
    # light.utilities.turn_off()
    return redirect(url_for('home'))


@bp.route("/rise")
@login_required
def rise():
    light.rise()
    return redirect(url_for('home'))
