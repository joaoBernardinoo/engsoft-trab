from datetime import datetime
from strategy.aluno_graduacao import EmprestimoAlunoGraduacaoStrategy
from strategy.aluno_pos_graduacao import EmprestimoAlunoPosGraduacaoStrategy
from strategy.professor import EmprestimoProfessorStrategy

class Reservation:
    def __init__(self, book, date):
        self.book = book
        self.date = date

class User:
    def __init__(self, user_id, user_type, name):
        self._user_id = user_id
        self._user_type = user_type
        self._name = name
        self._emprestimo = self.get_emprestimo_strategy()
        self._observed_books = []  # Lista de livros observados pelo usuário
        self._loans = []
        self._reservations = []
        self._notifications = 0
        self._loan_history = []  # Histórico de empréstimos
        
    @property
    def emprestimo(self):
        return self._emprestimo

    @property
    def user_id(self):
        return self._user_id

    @property
    def user_type(self):
        return self._user_type

    @property
    def name(self):
        return self._name

    @property
    def loans(self):
        return self._loans

    @property
    def reservations(self):
        return self._reservations

    @property
    def notifications(self):
        return self._notifications
    
    @property
    def observed_books(self):
        return self._observed_books

    def add_loan(self, loan):
        self._loans.append(loan)

    def return_loan(self, loan):
        self._loans.remove(loan)
        self._loan_history.append(loan)

    def add_reservation(self, book):
        self._reservations.append(Reservation(book, datetime.now()))

    def remove_reservation(self, book_id):
        self._reservations = [reservation for reservation in self._reservations if reservation.book.book_id != book_id]

    def increment_notifications(self):
        self._notifications += 1

    def is_devedor(self):
        return any(loan.is_overdue() for loan in self._loans)

    def livros_emprestados_count(self):
        return len(self._loans)

    def has_emprestimo(self, book):
        return any(loan.book_id == book.book_id for loan in self._loans)

    def get_emprestimo_strategy(self):
        strategies = {
            "Aluno Graduação": EmprestimoAlunoGraduacaoStrategy,
            "Aluno Pós-Graduação": EmprestimoAlunoPosGraduacaoStrategy,
            "Professor": EmprestimoProfessorStrategy
        }
        return strategies[self._user_type]()
    
    def observar(self, book):
        if book not in self._observed_books:
            self._observed_books.append(book)
            book.add_observer(self)  # Supondo que o livro tenha um método para adicionar observadores
            print(f"{self.name} agora está observando o livro {book.title}.")

    def update(self, book):
        print(f"Notificação para {self.name}: O livro {book.title} foi atualizado.")

    def get_user_loans_and_reservations(self):
        loans = [{
            "title": loan.book.title,
            "loan_date": loan.loan_date,
            "status": "Em curso",
            "return_date": None  # Data de devolução como None para empréstimos em curso
        } for loan in self._loans]

        loan_history = [{
            "title": loan.book.title,
            "loan_date": loan.loan_date,
            "status": "Finalizado",
            "return_date": loan.return_date
        } for loan in self._loan_history]

        reservations = [{
            "title": reservation.book.title,
            "reservation_date": reservation.date
        } for reservation in self._reservations]

        return loans + loan_history, reservations