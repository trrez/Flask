from flask_app import app
from flask import redirect, render_template, request
from ..models.author import Author
from ..models.book import Book


@app.route('/authors', methods=['GET'])
def all_authors():
    return render_template('index.html', authors=Author.all())


@app.route('/new-author', methods=['POST'])
def new_author():
    Author.new(request.form)
    return redirect('/')


@app.route('/author/<int:id>', methods=['GET'])
def fav_author(id):
    data = {
        'id': id
    }
    return render_template('fav_author.html', author=Author.get_by_id(data), unfavorited_books=Book.unfavorited_books(data))


@app.route('/join/book', methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")
