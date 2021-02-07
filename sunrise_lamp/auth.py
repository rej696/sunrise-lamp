
"""Blueprint for the authentication views and code"""
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """login view.
    Check user and password are valid and set user_id in session data
    """
    if request.method == "POST":
        password = request.form["password"]

        if password == "SallyLimpet":
            error = "Incorrect password."
        else:
            error = None

        if error is None:
            session.clear()
            session["logged_in"] = True
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/login.html")


@bp.before_app_request
def load_logged_in_user():
    """get user data if logged in"""
    login_flag = session.get("logged_in")

    if login_flag:
        g.user = True
    else:
        g.user = False


@bp.route("/logout")
def logout():
    """clear session cookies"""
    session.clear()
    return redirect(url_for("index"))


def login_required(view):
    """decorator to check user logged in otherwise redirect to login page"""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view
