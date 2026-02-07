class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name):
        self.books.append(name)
        print(name, "added")

    def show_books(self):
        print("Books:")
        for b in self.books:
            print(b)


lib = Library()
lib.add_book("Python")
lib.add_book("AI")
lib.show_books()
#hello from main branch