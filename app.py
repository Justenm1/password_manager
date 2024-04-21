from flask import render_template, session, redirect, url_for
from modules.globals import app, db
from modules.helpers import logged_in, create_session



@app.route('/')
def home():
    """ The home page of the website

           If the user is not logged in, redirect them to the login page,
           otherwise show them the home page, which contains a table of
           their password entries if they have permission.
       """





    return render_template('home.html')

@app.route('/login')
def login():

    return  render_template('login.html')

@app.route('/register')
def register():

    return render_template('register.html')

@app.route('/newentry')
def newentry():

    return render_template('newentry.html')

if __name__ == '__main__':
    app.run(debug=True)