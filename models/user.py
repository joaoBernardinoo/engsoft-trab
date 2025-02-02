from datetime import datetime
from strategy.aluno_graduacao import EmprestimoAlunoGraduacaoStrategy
from strategy.aluno_pos_graduacao import EmprestimoAlunoPosGraduacaoStrategy
from strategy.professor import EmprestimoProfessorStrategy
from observer.observador import Observador
from models.emprestimo_manager import EmprestimoManager
from models.reserva_manager import ReservaManager
from models.reservation import Reservation

class User:
    def __init__(self, user_id, user_type, name):
        self._user_id = user_id
        self._user_type = user_type
        self._name = name
        self._observador = Observador(self)
        self._emprestimo = self.get_emprestimo_strategy()
        self._notifications = 0
        self._observed_books = []  # Lista de livros observados pelo usuário
        self._emprestimo_manager = EmprestimoManager()
        self._reserva_manager = ReservaManager()

    @property
    def observador(self):
        return self._observador
        
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
        return self._emprestimo_manager.loans

    @property
    def reservations(self):
        return self._reserva_manager.reservations

    @property
    def notifications(self):
        return self._notifications
    
    @property
    def observed_books(self):
        return self._observed_books

    def add_loan(self, loan):
        self._emprestimo_manager.add_loan(loan)

    def return_loan(self, loan):
        self._emprestimo_manager.return_loan(loan)

    def add_loan_history(self, emprestimo):
        self._emprestimo_manager.loan_history.append(emprestimo)

    def add_reservation(self, book):
        self._reserva_manager.add_reservation(book)

    def remove_reservation(self, book_id):
        self._reserva_manager.remove_reservation(book_id)

    def increment_notifications(self):
        self._notifications += 1

    def is_devedor(self):
        return self._emprestimo_manager.is_devedor()

    def livros_emprestados_count(self):
        return self._emprestimo_manager.livros_emprestados_count()

    def has_emprestimo(self, book):
        return self._emprestimo_manager.has_emprestimo(book)

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
            book.add_observer(self._observador)
            print(f"{self.name} agora está observando o livro {book.title}.")

    def get_user_loans_and_reservations(self):
        loans = [{
            "title": loan.book.title,
            "loan_date": loan.loan_date.strftime("%d/%m/%Y") if loan.loan_date else "Data não disponível",
            "status": "Em curso",
            "return_date": "Não devolvido"  
        } for loan in self._emprestimo_manager.loans]

        loan_history = [{
            "title": emprestimo.book.title,
            "loan_date": emprestimo.loan_date.strftime("%d/%m/%Y") if emprestimo.loan_date else "Data não disponível",
            "status": "Finalizado",
            "return_date": emprestimo.return_date.strftime("%d/%m/%Y") if emprestimo.return_date else "Data não disponível"
        } for emprestimo in self._emprestimo_manager.loan_history]

        reservations = [{
            "title": reservation.book.title,
            "reservation_date": reservation.date.strftime("%d/%m/%Y") if reservation.date else "Data não disponível"
        } for reservation in self._reserva_manager.reservations]

        return loans + loan_history, reservations