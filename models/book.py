from observer.observable import Observable

class Book(Observable):
    def __init__(self, book_id, title, publisher, authors, edition, year):
        super().__init__()
        self._book_id = book_id
        self._title = title
        self._publisher = publisher
        self._authors = authors
        self._edition = edition
        self._year = year
        self._exemplars = []
        self._reservations = []
        self._reservation_count = 0

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

    @property
    def reservation_count(self):
        return self._reservation_count

    def add_exemplar(self, exemplar):
        exemplar.book = self  # Definir a referência ao livro
        self._exemplars.append(exemplar)

    def add_reservation(self, user):
        self._reservations.append(user.user_id)
        self._reservation_count += 1
        if self._reservation_count > 2:
            self.notify_observers()

    def remove_reservation(self, user_id):
        self._reservations = [reservation for reservation in self._reservations if reservation != user_id]
        self._reservation_count -= 1

    def exemplares_disponiveis(self):
        return any(exemplar.status == "Disponível" for exemplar in self._exemplars)

    def reservas_count(self):
        return self._reservation_count

    def exemplares_count(self):
        return len(self._exemplars)
        
    def is_loaned_to(self, user):
        return any(exemplar.loaned_to == user for exemplar in self._exemplars if exemplar.status == "Emprestado")

