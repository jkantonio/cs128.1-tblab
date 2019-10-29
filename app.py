# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
# import sqlite3

# create the application object
app = Flask(__name__)

app.secret_key = "mypreciouskey"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#create database and db tables

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#create the sqlalchemy object
db = SQLAlchemy(app)

app.database="sample.db"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Please login first. ')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/home')
@app.route('/')
@login_required
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('menu.html', posts=posts)

@app.route('/specimen-assign')
def specimen_assign():
	return render_template('specimen-assign.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            #flash("Login succesful!")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    #flash('Logout succesful.')
    return redirect(url_for('login'))

#def connect_db():
#   return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)