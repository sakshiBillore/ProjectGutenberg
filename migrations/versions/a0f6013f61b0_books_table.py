"""books table

Revision ID: a0f6013f61b0
Revises: 
Create Date: 2020-08-01 19:34:00.257140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0f6013f61b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_books_book_authors_author_id'), 'books_book_authors', ['author_id'], unique=False)
    op.create_index(op.f('ix_books_book_authors_book_id'), 'books_book_authors', ['book_id'], unique=False)
    op.create_index(op.f('ix_books_book_bookshelves_book_id'), 'books_book_bookshelves', ['book_id'], unique=False)
    op.create_index(op.f('ix_books_book_bookshelves_bookshelf_id'), 'books_book_bookshelves', ['bookshelf_id'], unique=False)
    op.create_index(op.f('ix_books_book_languages_book_id'), 'books_book_languages', ['book_id'], unique=False)
    op.create_index(op.f('ix_books_book_languages_language_id'), 'books_book_languages', ['language_id'], unique=False)
    op.create_index(op.f('ix_books_book_subjects_book_id'), 'books_book_subjects', ['book_id'], unique=False)
    op.create_index(op.f('ix_books_book_subjects_subject_id'), 'books_book_subjects', ['subject_id'], unique=False)
    op.create_index(op.f('ix_books_bookshelf_name'), 'books_bookshelf', ['name'], unique=False)
    op.create_index(op.f('ix_books_format_book_id'), 'books_format', ['book_id'], unique=False)
    op.create_index(op.f('ix_books_language_code'), 'books_language', ['code'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_language_code'), table_name='books_language')
    op.drop_index(op.f('ix_books_format_book_id'), table_name='books_format')
    op.drop_index(op.f('ix_books_bookshelf_name'), table_name='books_bookshelf')
    op.drop_index(op.f('ix_books_book_subjects_subject_id'), table_name='books_book_subjects')
    op.drop_index(op.f('ix_books_book_subjects_book_id'), table_name='books_book_subjects')
    op.drop_index(op.f('ix_books_book_languages_language_id'), table_name='books_book_languages')
    op.drop_index(op.f('ix_books_book_languages_book_id'), table_name='books_book_languages')
    op.drop_index(op.f('ix_books_book_bookshelves_bookshelf_id'), table_name='books_book_bookshelves')
    op.drop_index(op.f('ix_books_book_bookshelves_book_id'), table_name='books_book_bookshelves')
    op.drop_index(op.f('ix_books_book_authors_book_id'), table_name='books_book_authors')
    op.drop_index(op.f('ix_books_book_authors_author_id'), table_name='books_book_authors')
    # ### end Alembic commands ###
