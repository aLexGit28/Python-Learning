class Book:

    # Constructor
    def __init__(self):
        self.pages = []

    # Method to add a new page
    def add_page(self, page):
        self.pages.append(page)

    # Method to display all pages
    def show(self):
        for page in self.pages:
            print(page)


# Creating an object of Book
book = Book()

# Adding pages
book.add_page("Page 1: Introduction to Python")
book.add_page("Page 2: Variables and Data Types")
book.add_page("Page 3: Object-Oriented Programming")
book.add_page("Page 4: Lists and Tuples")

# Displaying all pages
book.show()