#model.py defines what the table looks like

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
from flask_bcrypt import generate_password_hash, check_password_hash


# Define model (User)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(180), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)


    def set_password(self, password):
        """Hash and set the password for this user"""
        self.password_hash = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """check if the password matches the hash of the password"""
        return check_password_hash(self.password_hash, password)

    # __repr__ gives a string representation of the data used
    def __repr__(self):
        return f"<User(id={self.id}, name={self.username}, email={self.email})>"



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # ForeignKey links posts to users who create them
    author_id = Column(Integer, ForeignKey('user.id'))

    # relationship() allows access to post.author.name or user.posts
    author = relationship("User", backref= 'posts')

    def __repr__(self):
        return f"<Post(id = {self.id}, title = {self.title}, author_id = {self.author_id})>"

