#model.py defines what the table looks like

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime

from sqlalchemy.orm import relationship

from database import Base


# Define model (User)
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# __repr__ gives a string representation of the data used
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

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

