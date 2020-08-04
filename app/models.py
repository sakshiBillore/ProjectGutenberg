from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class BooksAuthor(db.Model):
    __tablename__ = 'books_author'

    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.SmallInteger)
    death_year = db.Column(db.SmallInteger)
    name = db.Column(db.String(128), nullable=False)
    # book = relationship("BooksBook", secondary="books_book_authors")


class BooksBook(db.Model):
    __tablename__ = 'books_book'

    id = db.Column(db.Integer, primary_key=True)
    download_count = db.Column(db.Integer)
    gutenberg_id = db.Column(db.Integer, nullable=False)
    media_type = db.Column(db.String(16), nullable=False)
    title = db.Column(db.Text)
    # book = relationship("BooksAuthor", secondary="books_book_authors")


class BooksBookAuthor(db.Model):
    __tablename__ = 'books_book_authors'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'), nullable=False, index=True, )
    author_id = db.Column(db.Integer, db.ForeignKey('books_author.id'), nullable=False, index=True)


class BooksBookBookshelf(db.Model):
    __tablename__ = 'books_book_bookshelves'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False, index=True)
    bookshelf_id = db.Column(db.Integer, nullable=False, index=True)
    book = relationship(BooksBook, backref=backref("books_book_bookshelves", cascade="all, delete-orphan"))
    author = relationship(BooksBookAuthor, backref=backref("books_book_bookshelves", cascade="all, delete-orphan"))


class BooksBookLanguage(db.Model):
    __tablename__ = 'books_book_languages'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False, index=True)
    language_id = db.Column(db.Integer, nullable=False, index=True)


class BooksBookSubject(db.Model):
    __tablename__ = 'books_book_subjects'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False, index=True)
    subject_id = db.Column(db.Integer, nullable=False, index=True)


class BooksBookshelf(db.Model):
    __tablename__ = 'books_bookshelf'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)


class BooksFormat(db.Model):
    __tablename__ = 'books_format'

    id = db.Column(db.Integer, primary_key=True)
    mime_type = db.Column(db.String(32), nullable=False)
    url = db.Column(db.Text, nullable=False)
    book_id = db.Column(db.Integer, nullable=False, index=True)


class BooksLanguage(db.Model):
    __tablename__ = 'books_language'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4), nullable=False, index=True)


class BooksSubject(db.Model):
    __tablename__ = 'books_subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
