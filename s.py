class Book:
    def __init__(self, title, authors, year):
        self.title = title
        self.authors = authors
        self.year = year

    def __str__(self):
        authors_text = ", ".join(self.authors)
        return f"'{self.title}' | Authors: {authors_text} | Year: {self.year}"


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def __str__(self):
        return f"Library: {self.name}\nAddress: {self.address}"

    def show_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
            return

        print("Book List:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    def add_book(self, book):
        self.books.append(book)
        print("Book added!")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed!")
                return

        print("Book not found.")

    def search_by_title(self, title):
        found = False

        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                found = True

        if not found:
            print("\nBook not found.")

    def search_by_author(self, author):
        found = False

        for book in self.books:
            for a in book.authors:
                if author.lower() in a.lower():
                    print(book)
                    found = True

        if not found:
            print("No books by this author found.")


library = Library("Central Library", "Main Street 10")

while True:
    print("\n" + "=" * 40)
    print("           LIBRARY MENU")
    print("=" * 40)

    print("1. Show books")
    print("2. Add book")
    print("3. Remove book")
    print("4. Search by title")
    print("5. Search by author")
    print("6. Library information")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        library.show_books()

    elif choice == "2":
        title = input("Enter book title: ")

        authors_input = input(
            "Enter authors separated by commas: "
        )

        authors = authors_input.split(",")
        authors = [a.strip() for a in authors]

        year = input("Enter publication year: ")

        new_book = Book(title, authors, year)

        library.add_book(new_book)

    elif choice == "3":
        title = input("Enter book title to remove: ")
        library.remove_book(title)

    elif choice == "4":
        title = input("Enter title to search: ")
        library.search_by_title(title)

    elif choice == "5":
        author = input("Enter author to search: ")
        library.search_by_author(author)

    elif choice == "6":
        print(library)

    elif choice == "0":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")