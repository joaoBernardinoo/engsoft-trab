from strategy.aluno_graduacao import EmprestimoAlunoGraduacaoStrategy
from strategy.aluno_pos_graduacao import EmprestimoAlunoPosGraduacaoStrategy
from strategy.professor import EmprestimoProfessorStrategy

class User:
    def __init__(self, user_id, user_type, name):
        self._user_id = user_id
        self._user_type = user_type
        self._name = name
        self._loans = []
        self._reservations = []
        self._notifications = 0

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

    def add_loan(self, loan):
        self._loans.append(loan)

    def add_reservation(self, reservation):
        self._reservations.append(reservation)

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