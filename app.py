#import the flask framework
from flask import Flask, render_template
from model import User, Post
from database import db_session, init_db

# initialise DB at startup
init_db()

#create an instance (1st arg is name of module)
app = Flask(__name__)

# route() decorator telling flask what URL will trigger our fucntion

#Home page displays all posts
@app.route('/')
def home():
    posts = db_session.query(Post).all()
    return render_template('home.html', posts=posts)

# About page, Talk about my experience
@app.route('/about')
def about():

# Single post page

# Create Post page

# Edit post page

# Delete page


@app.teardown_appcontext
def shutdown(exception=None):
    db_session.remove()

if __name__== "__main__":
    app.run(debug=True)
