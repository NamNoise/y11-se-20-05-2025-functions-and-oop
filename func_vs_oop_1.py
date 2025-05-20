book_a = {"title": "Othello", "author": "William Shakespeare"}
book_b = {"title": "Lord of the Flies", "author": "William Golding"}

my_book_collection = []

def add_book_to_collection(collection, book):
    collection.append(book)

def display_collection(collection):
    print ("My Books")
    print ("--------")

    for book in collection:
        print ("Title:", "'" + book["title"] + "'","by", book["author"])

add_book_to_collection(my_book_collection, book_a)
add_book_to_collection(my_book_collection, book_b)

print(my_book_collection)
display_collection(my_book_collection)

