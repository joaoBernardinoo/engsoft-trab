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

    def get_reservations(self):
        reservations = [{
            "title": reservation.book.title,
            "reservation_date": reservation.date.strftime("%d/%m/%Y") if reservation.date else "Data não disponível"
        } for reservation in self.reservations]
        return reservations
    
    def has_reservation(self, book):
        return any(reservation.book.book_id == book.book_id for reservation in self.reservations)
    