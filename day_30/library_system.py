book_ids = []
book_names = []
authors = []
quantities = []

def add_book():
    book_ids.append(int(input("Enter Book ID: ")))
    book_names.append(input("Enter Book Name: "))
    authors.append(input("Enter Author Name: "))
    quantities.append(int(input("Enter Quantity: ")))
    print("Book Added Successfully!")

def display_books():
    if len(book_ids) == 0:
        print("No books available.")
        return

    for i in range(len(book_ids)):
        print("\nBook ID:", book_ids[i])
        print("Book Name:", book_names[i])
        print("Author:", authors[i])
        print("Quantity:", quantities[i])

def search_book():
    name = input("Enter Book Name: ")

    for i in range(len(book_names)):
        if book_names[i] == name:
            print("Book Found!")
            print("Book ID:", book_ids[i])
            print("Author:", authors[i])
            print("Quantity:", quantities[i])
            return

    print("Book Not Found!")

def issue_book():
    book_id = int(input("Enter Book ID: "))

    for i in range(len(book_ids)):
        if book_ids[i] == book_id:
            if quantities[i] > 0:
                quantities[i] -= 1
                print("Book Issued Successfully!")
            else:
                print("Book Not Available!")
            return

    print("Book ID Not Found!")

def return_book():
    book_id = int(input("Enter Book ID: "))

    for i in range(len(book_ids)):
        if book_ids[i] == book_id:
            quantities[i] += 1
            print("Book Returned Successfully!")
            return

    print("Book ID Not Found!")

while True:
    print("\n***** LIBRARY MANAGEMENT SYSTEM *****")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        display_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        issue_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")