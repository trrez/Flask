from flask_app import app
from flask import redirect, render_template, request
from ..models.author import Author
from ..models.book import Book


@app.route('/all_book', methods=['GET'])
def all_book():
    return render_template('all_book.html', books=Book.all_book())


@app.route('/join/author', methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")


@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    return render_template('show_book.html', book=Book.get_by_id(data), unfavorited_authors=Author.unfavorited_authors(data))
