class Book:

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def add_book(self, new_book_id, new_title, new_author):
        self.book_id = new_book_id
        self.title = new_title
        self.author = new_author

    def issue_book(self):
        if self.quantity > 0:
            self.quantity -= 1
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self):
        self.quantity += 1
        print("Book returned")

    def book_details(self):
        print("BOOK ID =", self.book_id)
        print("TITLE =", self.title)
        print("AUTHOR =", self.author)
        print("QUANTITY =", self.quantity)


book = Book(101, "The Jungle Book", "Peter", 5)

book.book_details()
print("*"*20)
book.issue_book()
book.return_book()
print("*"*20)
book.book_details()