from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.main import bp
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

# Testing dummy calls to simulator
import subprocess

@bp.route("/")
@bp.route("/index")
@login_required
def index():
    user = {"username": "Miguel"}
    posts = [
        {
            "author": {"username": "John"},
            "body": {"la;sdoifudblasdjfhblsdjfkghadlfasdflupgsd"},
        },
        {
            "author": {"username": "John"},
            "body": {"la;sdoifudblasdjfhblsdjfkghadlfasdflupgsd"},
        },
    ]
    return render_template("index.html", title="Home", posts=posts)


@bp.route("/simulator")
def dummy_simulator():
    sim_bin_path = "/home/nikon/edu/diploma/zsim/build/libs/libblifparse/blifparse_test"
    design_path = "/home/nikon/edu/diploma/zsim/tests/small_model_1.blif"

    # Using shell=True can be a security hazard
    sim_output = subprocess.check_output([sim_bin_path, design_path], shell=True)
    return sim_output
