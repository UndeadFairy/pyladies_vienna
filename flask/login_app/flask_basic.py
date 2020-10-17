from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from config import Config
from forms import LoginForm
app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/PyLadies")
def PyLadies():
    return "PyLadies Flask"


# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/PyLadies')
    return render_template('login.html', title='Sign In', form=form)
if __name__ == "__main__":
    app.run()
