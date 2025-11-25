"""
import the flask framework
url_for - gives a specified url for a function
"""
from flask import Flask, render_template , request, redirect, url_for, abort
from flask_wtf import form
from sqlalchemy.sql.functions import current_user

from model import User, Post
from database import db_session, init_db
from forms import PostForm


# initialise DB at startup
init_db()

#create an instance (1st arg is name of module)
app = Flask(__name__)
app.secret_key = 'Your secret key'

# route() decorator telling flask what URL will trigger our fucntion
#Home page displays all posts
@app.route('/')
def home():
    posts = db_session.query(Post).all()
    return render_template('home.html', posts = posts)

app.route('/about')
def about():
    return render_template('about.html')

# Single post page
@app.route('/post, <int:post_id>', methods=['GET'])
def view_post(post_id):
    post = db_session.query(Post).get_or_404(post_id)
    return render_template('post.html', post = post)

@app.route('/post/new', methods=['GET', 'POST'])
# Create Post page
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title = form.title.data,
                        content = form.content.data,
                        author_id= 1 # Hardcoded for now
        )
        db_session.add(new_post)
        db_session.commit()
        return redirect(url_for('home'))
    return render_template('create_post.html', form=form)

# Edit post page

# Delete page


@app.teardown_appcontext
def shutdown(exception=None):
    db_session.remove()

if __name__== "__main__":
    app.run(debug=True)
