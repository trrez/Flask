from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite


@app.route('/', methods=['GET'])
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
    book = Book.all_book()
    author = Author.select_author_with_favorite(data)
    return render_template('fav_author.html', author=author, book=book)


@app.route('/author/<int:id>/add-favorite', methods=['POST'])
def add_fav(id):

    data = {
        'author_id': id,
        'book_id': request.form['book_id']
    }
    Favorite.new_favorite(data)

    return redirect('/author/{}'.format(id))
