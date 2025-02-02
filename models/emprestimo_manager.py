
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

    def is_devedor(self):
        return any(loan.is_overdue() for loan in self._loans)

    def livros_emprestados_count(self):
        return len(self._loans)

    def has_emprestimo(self, book):
        return any(loan.book_id == book.book_id for loan in self._loans)

    def get_loans(self):
        loans = [{
            "title": loan.book.title,
            "loan_date": loan.loan_date.strftime("%d/%m/%Y") if loan.loan_date else "Data não disponível",
            "status": "Em curso",
            "return_date": loan.return_date.strftime("%d/%m/%Y") if loan.return_date else "Data não disponível"  
        } for loan in self.loans]

        loan_history = [{
            "title": emprestimo.book.title,
            "loan_date": emprestimo.loan_date.strftime("%d/%m/%Y") if emprestimo.loan_date else "Data não disponível",
            "status": "Finalizado",
            "return_date": emprestimo.return_date.strftime("%d/%m/%Y") if emprestimo.return_date else "Data não disponível"
        } for emprestimo in self.loan_history]

        return loans + loan_history