class Book():
    def __init__ (self, title, author):
        self.title = title
        self.author = author

class BookCollection():
    def __init__ (self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def display(self):
        print ("My Books")
        print ("--------")

        for book in self.collection:
            print ("Title:", "'" + book.title + "'","by", book.author)

book_a = Book ("Othello", "William Shakespeare")
book_b = Book ("Lord of the Flies", "William Golding")

my_collection = BookCollection()
my_collection.add_book(book_a)
my_collection.add_book(book_b)

my_collection.display()


