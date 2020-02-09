from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# Testing dummy calls to simulator
import subprocess


@app.route("/")
@app.route("/index")
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
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/simulator")
def dummy_simulator():
    sim_bin_path = "/home/nikon/edu/diploma/zsim/build/libs/libblifparse/blifparse_test"
    design_path = "/home/nikon/edu/diploma/zsim/tests/small_model_1.blif"

    # Using shell=True can be a security hazard
    sim_output = subprocess.check_output([sim_bin_path, design_path], shell=True)
    return sim_output
