from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print('password is: {}'.format(form.password.data)) 
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/simulator")
def dummy_simulator():
    sim_bin_path = "/home/nikon/edu/diploma/zsim/build/libs/libblifparse/blifparse_test"
    design_path = "/home/nikon/edu/diploma/zsim/tests/small_model_1.blif"

    # Using shell=True can be a security hazard
    sim_output = subprocess.check_output([sim_bin_path, design_path], shell=True)
    return sim_output
