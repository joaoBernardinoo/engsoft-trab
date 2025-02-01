class Book:
    def __init__(self, book_id, title, publisher, authors, edition, year):
        self.book_id = book_id
        self.title = title
        self.publisher = publisher
        self.authors = authors
        self.edition = edition
        self.year = year
        self.exemplars = []
        self.reservations = []