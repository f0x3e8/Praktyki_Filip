class LibraryBook:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True

    def give_back(self):
        if self.is_borrowed == True:
            self.is_borrowed = False

    def describe(self):
        return f"{self.title}, ({self.year}), {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def available_books(self):
        available_books = []
        for i in self.books:
            if i.is_borrowed == False:
                available_books.append(i)
        return available_books

    def find_by_author(self, author):
        author_books = []
        for i in self.books:
            if i.author == author:
                author_books.append(i)
        return author_books

    def borrow_by_title(self, title):
        title_books = []
        for i in self.books:
            if i.title == title:
                if i.is_borrowed == True:
                    return False
        return True

    def oldest_book(self):
        year = self.books[0].year
        oldest_book = self.books[0]
        for i in self.books:
            if i.year < year:
                year = i.year
                oldest_book = i
        return oldest_book

    def count_by_author(self):
        authors_books = {}
        for i in self.books:
            if i.author in authors_books.keys():
                authors_books[i.author] += 1
            else:
                authors_books[i.author] = 1
        return authors_books

library = Library()
library.add_book(LibraryBook("Wied?min", "Andrzej Sapkowski", 1993))
library.add_book(LibraryBook("Narrenturm", "Andrzej Sapkowski", 2002))
library.add_book(LibraryBook("Solaris", "Stanis?aw Lem", 1961))

print(len(library.get_books()))              # 3
print(library.oldest_book().title)           # Solaris
print(library.count_by_author())
# {"Andrzej Sapkowski": 2, "Stanis?aw Lem": 1}

print(library.borrow_by_title("Solaris"))    # True
print(library.borrow_by_title("Solaris"))    # False
print(len(library.available_books()))        # 2

for book in library.find_by_author("Andrzej Sapkowski"):
    print(book.describe())
# Wied?min (1993), Andrzej Sapkowski
# Narrenturm (2002), Andrzej Sapkowski