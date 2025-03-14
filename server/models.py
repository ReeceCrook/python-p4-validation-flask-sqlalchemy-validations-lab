from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators
    @validates('name')
    def validate_name(self, key, name):
        authors_names = [author.name for author in Author.query.all()]
        if len(name) <= 0:
            raise ValueError("Failed Name length validation")
        elif name in authors_names:
            raise ValueError("Failed Name validation")
        return name
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        int(number)
        if len(number) != 10:
            raise ValueError("Failed Phone Number length validation")
        return number
    

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators

    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Failed Content length validation")
        return content
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Failed Summary length validation")
        return summary
    @validates('category')
    def validate_category(self, key, category):
        if category != 'Fiction' and category != 'Non-Fiction':
            raise ValueError("Failed Category validation")
        return category
    @validates('title')
    def validate_title(self, key, title):
        if "Won't Believe" not in title and "Secret" not in title and "Top" not in title and "Guess" not in title:
            raise ValueError("Failed Title validation")
        return title
        


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
