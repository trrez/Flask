from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.book import Book


@app.route('/all_book', methods=['GET'])
def all_book():
    return render_template('all_book.html', books=Book.all_book())


@app.route('/new-book', methods=['POST'])
def new_book():
    Book.new_book(request.form)
    return redirect('/all_book')
