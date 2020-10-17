import requests
# REST API integration

def _url(path):
    return 'http://lubojr.pythonanywhere.com' + path


# get all books
def get_books():
    return requests.get(_url('/books'))


# get one
def describe_book(book_id):
    return requests.get(_url('/books/{:d}'.format(book_id)))


# post
def add_book(published=1900, author="", title="", first_sentence=""):
    return requests.post(_url('/books'), json={
        'published': published,
        'author': author,
        'title': title,
        'first_sentence': first_sentence,
        })


# delete
def delete_book(book_id):
    return requests.delete(_url('/books/{:d}'.format(book_id)))


# put
def update_book(book_id, published, author, title, first_sentence):
    url = _url('/books/{:d}'.format(book_id))
    return requests.put(url, json={
        'published': published,
        'author': author,
        'title': title,
        'first_sentence': first_sentence,
        })


resp = add_book(1950, "Bob Bobovic", "My book title", "First sentence")
if resp.status_code != 201:
    raise Exception('Cannot create book: {}'.format(resp.status_code))
print('Created book. ID: {}'.format(resp.json()['book']["id"]))

resp = get_books()
if resp.status_code != 200:
    raise Exception('Cannot fetch all books: {}'.format(resp.status_code))
responseobj = resp.json()
for book_item in responseobj['books']:
    print('{} {}'.format(book_item['id'], book_item['title']))
