from datetime import datetime
from models.reservation import Reservation

class ReservaManager:
    def __init__(self):
        self._reservations = []

    @property
    def reservations(self):
        return self._reservations

    def add_reservation(self, book):
        self._reservations.append(Reservation(book, datetime.now()))

    def remove_reservation(self, book_id):
        self._reservations = [reservation for reservation in self._reservations if reservation.book.book_id != book_id]
