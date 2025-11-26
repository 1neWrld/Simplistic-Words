"""
import the flask framework
url_for - gives a specified url for a function
"""
from flask import Flask, render_template, request, redirect, url_for, abort
from database import db_session, init_db
from model import User, Post
from forms import PostForm


#create an instance (1st arg is name of module)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# initialise DB at startup
init_db()

# route() decorator telling flask what URL will trigger our fucntion
#Home page displays all posts
@app.route('/')
def home():
    posts = db_session.query(Post).all()
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

# Single post page
# HTTPS methods for accessing urls
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = db_session.query(Post).filter_by(id = post_id).first()
    if post is None:
        abort(404)
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
@app.route('/post/<int:post_id>/edit', methods=['GET','POST'])
def edit_post(post_id):
    post = db_session.query(Post).filter_by(id = post_id).first()
    if post is None:
        abort(404)

    form = PostForm(obj= post)

    if form.validate_on_submit():
       post.title = form.title.data
       post.content = form.content.data
       db_session.commit()
       return redirect(url_for('view_post', post_id = post.id))

    return render_template('edit_post.html', form=form, post=post)


# Delete page
@app.route('/post/<int:post_id>/delete', methods=['POST', 'DELETE'])
def delete_post(post_id):
    post = db_session.query(Post).filter_by(id=post_id).first()
    if post is None:
        abort(404)

    db_session.delete(post)
    db_session.commit()

    return redirect(url_for('home'))

@app.teardown_appcontext
def shutdown(exception=None):
    db_session.remove()

if __name__== "__main__":
    print(db_session.query(User).all())
    app.run(debug=True)
