"""
import the flask framework
url_for - gives a specified url for a function
"""
from flask import Flask, render_template, request, redirect, url_for, abort, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from database import db_session, init_db
from model import User, Post
from forms import PostForm, RegistrationForm, LoginForm
import os

#create an instance (1st arg is name of module)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# initialise DB at startup
init_db()

#setup flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

#Make User class compatible with flask login
class UserLogin(UserMixin):
    def __init__(self, user):
        self.id = user.id
        self.username = user.username
        self.email = user.email

@login_manager.user_loader
def load_user(user_id):
    """Load user from database"""
    user = db_session.query(User).get(int(user_id))
    if user:
        return UserLogin(user)
    return None


"""Routes"""

# route() decorator telling flask what URL will trigger our fucntion
#Home page displays all posts
@app.route('/')
def home():
    posts = db_session.query(Post).all()
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        db_session.add(user)
        db_session.commit()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


#Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = db_session.query(User).filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            user_login = UserLogin(user)
            login_user(user_login)
            flash('Logged in successfully!', 'success')

            # Redirect to the page they were trying to access
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login failed. Please check your username and password.', 'danger')

    return render_template('login.html', form=form)


# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


# view single post page
# HTTPS methods for accessing urls
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = db_session.query(Post).filter_by(id = post_id).first()
    if post is None:
        abort(404)
    return render_template('post.html', post = post)

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
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
@login_required
def edit_post(post_id):
    post = db_session.query(Post).filter_by(id = post_id).first()
    if post is None:
        abort(404)

    #check if user is post author
    if post.author != current_user.id:
        abort(403) # forbidden

    form = PostForm(obj= post)

    if form.validate_on_submit():
       post.title = form.title.data
       post.content = form.content.data
       db_session.commit()
       return redirect(url_for('view_post', post_id = post.id))

    return render_template('edit_post.html', form=form, post=post)


# Delete page
@app.route('/post/<int:post_id>/delete', methods=['POST', 'DELETE'])
@login_required
def delete_post(post_id):
    post = db_session.query(Post).filter_by(id=post_id).first()
    if post is None:
        abort(404)

    #check if user is post author
    if post.author_id != current_user.id:
        abort(403) # forbidden


    db_session.delete(post)
    db_session.commit()
    flash('Post deleted successfully!', 'info')
    return redirect(url_for('home'))

@app.teardown_appcontext
def shutdown(exception=None):
    db_session.remove()

if __name__== "__main__":
    app.run(debug=True)
