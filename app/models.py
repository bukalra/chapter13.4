from app import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_db = db.Column(db.String(100), index=True, unique=True)
    description_db = db.Column(db.String(200), index=True)
    date_db = db.Column(db.String(100), index=True)
    genre_db = db.Column(db.String(100), index = True)
    booklist = db.Column(db.String(100), db.ForeignKey('rent.id'))
    book_id = db.relationship("BookList", backref="book", lazy="dynamic")

    def __str__(self):
        return f"<Book {self.username}>"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name_db = db.Column(db.Text)
    last_name_db = db.Column(db.Text)
    author_id = db.relationship("BookList", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author {self.id} {self.body[:50]} ...>"

class BookList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id_db = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id_db = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __str__(self):
        return f"<BookList {self.id} {self.body[:50]} ...>"

class Rent(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rent_db = db.Column(db.String, index= True, unique=False)
    author_id = db.relationship("Book", backref="book", lazy="dynamic")


    def __str__(self):
        return f"<Rent {self.id} {self.body[:50]} ...>"