from datetime import datetime
from models.emprestimo import Emprestimo

class EmprestimoManager:
    def __init__(self):
        self._loans = []
        self._loan_history = []

    @property
    def loans(self):
        return self._loans

    @property
    def loan_history(self):
        return self._loan_history

    def add_loan(self, loan):
        self._loans.append(loan)

    def return_loan(self, loan):
        self._loans.remove(loan)
        emprestimo = Emprestimo(loan.book, loan.loan_date, datetime.now())
        self._loan_history.append(emprestimo)

    def is_devedor(self):
        return any(loan.is_overdue() for loan in self._loans)

    def livros_emprestados_count(self):
        return len(self._loans)

    def has_emprestimo(self, book):
        return any(loan.book_id == book.book_id for loan in self._loans)
