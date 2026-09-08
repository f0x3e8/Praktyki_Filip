class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"{self.title}, {self.author}, {self.pages} stron"

book_1 = Book("Dżuma", "Albert Camus", 200)
book_2 = Book("Niezwyciężony", "Stanisław Lem", 400)
book_3 = Book("Biesy", "Fiodor Dostojewski", 600)

print(book_1.describe())
print(book_2.describe())
print(book_3.describe())
