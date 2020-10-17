# from https://www.nintyzeros.com/2019/11/flask-mysql-crud-restful-api.html
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import os

app = Flask(__name__)
currentpath = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/books.db' % currentpath
db = SQLAlchemy(app)


class Book(db.Model):
    # creating of a table model
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    published = db.Column(db.Integer)
    author = db.Column(db.VARCHAR)
    title = db.Column(db.VARCHAR)
    first_sentence = db.Column(db.VARCHAR)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    def __init__(self, published, author, title, first_sentence):
        self.published = published
        self.author = author
        self.title = title
        self.first_sentence = first_sentence
    def __repr__(self):
        return '' % self.id

db.create_all()

class BookSchema(ModelSchema):
    # create marshmallow schema
    class Meta(ModelSchema.Meta):
        model = Book
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    author = fields.String(required=False)
    published = fields.Integer(required=False)
    title = fields.String(required=True)
    first_sentence = fields.String(required=False)

# homepage that user arrives to - could contain swagger api documentation
@app.route('/', methods = ['GET'])
def home():
    return '''<h1>Database of books</h1>
<p>Example use: GET on /books to see a list of books.
<p>GET info about single book on /books/"id"
<p>Update info about single book with PUT on /books/"id"
<p>DELETE book on /books/"id"
<p>create book using POST on /books with data payload'''


# get all books as a json response
@app.route('/books', methods = ['GET'])
def index():
    get_books = Book.query.all()
    product_schema = BookSchema(many=True)
    books = product_schema.dump(get_books)
    return make_response(jsonify({"books": books}))


# get all info about a single book
@app.route('/books/<id>', methods = ['GET'])
def get_book_by_id(id):
    get_book = Book.query.get(id)
    book_schema = BookSchema()
    book = book_schema.dump(get_book)
    return make_response(jsonify({"book": book}))


# update information about an existing book
@app.route('/books/<id>', methods = ['PUT'])
def update_book_by_id(id):
    data = request.get_json()
    get_book = Book.query.get(id)
    if data.get('published'):
        get_book.published = data['published']
    if data.get('author'):
        get_book.author = data['author']
    if data.get('title'):
        get_book.title = data['title']
    if data.get('first_sentence'):
        get_book.first_sentence = data['first_sentence']
    db.session.add(get_book)
    db.session.commit()
    book_schema = BookSchema(only=['id', 'published', 'author', 'title', 'first_sentence'])
    book = book_schema.dump(get_book)
    return make_response(jsonify({"book": book}))


# delete a book
@app.route('/books/<id>', methods = ['DELETE'])
def delete_book_by_id(id):
    get_book = Book.query.get(id)
    db.session.delete(get_book)
    db.session.commit()
    return make_response("", 204)


# create a book
@app.route('/books', methods = ['POST'])
def create_book():
    data = request.get_json()
    book_schema = BookSchema()
    book = book_schema.load(data)
    result = book_schema.dump(book.create())
    return make_response(jsonify({"book": result}), 201)


if __name__ == "__main__":
    app.run(debug=True)