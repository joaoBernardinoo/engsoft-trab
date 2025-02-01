class Book:
    def __init__(self, book_id, title, publisher, authors, edition, year):
        self._book_id = book_id
        self._title = title
        self._publisher = publisher
        self._authors = authors
        self._edition = edition
        self._year = year
        self._exemplars = []
        self._reservations = []

    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def publisher(self):
        return self._publisher

    @property
    def authors(self):
        return self._authors

    @property
    def edition(self):
        return self._edition

    @property
    def year(self):
        return self._year

    @property
    def exemplars(self):
        return self._exemplars

    @property
    def reservations(self):
        return self._reservations

    def add_exemplar(self, exemplar):
        self._exemplars.append(exemplar)

    def add_reservation(self, reservation):
        self._reservations.append(reservation)

    def exemplares_disponiveis(self):
        return any(exemplar.status == "Disponível" for exemplar in self._exemplars)

    def reservas_count(self):
        return len(self._reservations)

    def exemplares_count(self):
        return len(self._exemplars)

    def is_reserved_by(self, user):
        return any(reservation.user_id == user.user_id for reservation in self._reservations)

    def is_loaned_to(self, user):
        return any(exemplar.loaned_to == user for exemplar in self._exemplars if exemplar.status == "Emprestado")

