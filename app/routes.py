from datetime import datetime
from app import app,db
from forms import TodoForm
from app.models import Book, Rent, Author
from flask import (
    request,
    render_template,
    redirect,
    url_for,
)

@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = TodoForm()    
    error = ""

    if request.method == "POST":
        if form.validate_on_submit():
            if form.data['rent'] == 0:
                rent_form = False
            else:
                rent_form = True
            print(rent_form)
            book = Book(title_db=form.data['title'], description_db =form.data['description'], genre_db =form.data['genre'], date_db = form.data['date'])
            rent = Rent(rent_db = rent_form)
            author = Author(first_name_db = form.data['first_name'], last_name_db = form.data['last_name'])
            db.session.add(book)
            db.session.add(rent)
            db.session.add(author)
            db.session.commit()
        return redirect(url_for("books_list"))
    return render_template("books.html", form=form, books=Book.query.all(), rents = Rent.query.all(), authors = Author.query.all(), error=error, zip = zip)

@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
   
    book = Book.query.get(book_id)
    rent = Rent.query.get(book_id)
    author = Author.query.get(book_id)
    form = TodoForm(data={'id':book.id, 'title':book.title_db, 'description':book.description_db, 'first_name':author.first_name_db, 'last_name':author.last_name_db, 'rent':rent.rent_db, 'genre':book.genre_db, 'date':datetime.strptime(book.date_db, '%Y-%m-%d')})
    if request.method == "POST":        
        if form.validate_on_submit():            

            book.id=book_id
            book.title_db=form.data['title']
            book.description_db =form.data['description']
            author.first_name_db = form.data['first_name']
            author.last_name_db = form.data['last_name']

            if form.data['rent'] == 0:
                rent_form = False
            else:
                rent_form = True
            rent.rent_db = rent_form
            book.genre_db =form.data['genre']
            book.date_db =form.data['date']
            db.session.commit()
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)

@app.route("/delete/<int:book_id>/", methods=["POST"])
def delete_book(book_id):
   
    book = Book.query.get(book_id)
    rent = Rent.query.get(book_id)
    author = Author.query.get(book_id)

    db.session.delete(book)
    db.session.delete(rent)
    # db.session.delete(author)
    db.session.commit()
    return redirect(url_for("books_list"))