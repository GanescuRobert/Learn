from flask import Flask, jsonify, request, Response
import json

from settings import *


books = [
    {
        'name': "Green Eggs and Ham",
        'price': 7.99,
        'isbn': 9785
    },
    {
        'name': "The Cat In The Hat",
        'price': 6.99,
        'isbn': 9793
    }
]


def validBookObject(bookObject):
    return "name" in bookObject and "price" in bookObject and "isbn" in bookObject

    # GET /books


@ app.route('/books')
def get_books():
    return {'books': books}

# POST /books


@ app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if validBookObject(request_data):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "Invalid book object passed in request",
            "helpString": "Data passed in similar to this{'name':'bookname','price':7.99,'isbn':'0000'}"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg),
                            status=400, mimetype='application/json')
        return response
# GET /books/{isbn}


@ app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if(book["isbn"] == isbn):
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
            return jsonify(return_value)


@ app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
        "name": request_data["name"],
        "price": request_data["price"],
        "isbn": isbn
    }
    indexPos = 0
    for book in books:
        currentISBN = book['isbn']
        if currentISBN == isbn:
            books[indexPos] = new_book
        indexPos += 1
    response = Response("", status=204)
    return response


@ app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    update_book = {}
    attributes = ["name", "price"]

    for attribute in attributes:
        if attribute in request_data:
            update_book[attribute] = request_data[attribute]
    for book in books:
        if book["isbn"] == isbn:
            book.update(update_book)
    response = Response("", status=204)
    response.headers['Location'] = "/books/" + str(isbn)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    index = 0
    for book in books:
        if book["isbn"] == isbn:
            books.pop(index)
            response = Response("", status=204)
            return response
        index += 1

    return Response(json.dumps({"error": "Book with the ISBN number that was provided was not found, so therefore unable to delete"}), status=404, mimetype='application/json')


app.run(port=5000)
