from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

##### MVP #####

# INDEX
@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', books = books)

# DELETE
@books_blueprint.route('/books/<id>/delete', methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')


##### EXTENSION #####


# NEW
@books_blueprint.route('/books/new')
def new_book():
    books = book_repository.select_all()
    return render_template('books/new.html', books=books)


# CREATE
@books_blueprint.route('/books', methods=['POST'])
def add_book():
    author_id = request.form['author_id']
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author = author_repository.select(author_id)
    book = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect('/tasks')


# SHOW



##### ADVANCED EXTENSION #####


# EDIT


# UPDATE


