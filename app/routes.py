from flask import jsonify
from sqlalchemy.sql import select
from app import app
from app.models import BooksAuthor, BooksBook,BooksBookAuthor


@app.route('/')
@app.route('/index')
def index():

    books = BooksBook.query.all()
    author=BooksBookAuthor.query.all()
    all_users = [{'name': title.name, 'id': title.book_id,'book_title':title} for title in author]

    books = BooksBook.query.first()
    var1 = books.books_author
    var2 = books.books_book_authors
    return jsonify(all_users)


