from strategies import EmprestimoAlunoGraduacaoStrategy, EmprestimoAlunoPosGraduacaoStrategy, EmprestimoProfessorStrategy
class User:
    def __init__(self, user_id, user_type, name):
        self.user_id = user_id
        self.user_type = user_type
        self.name = name
        self.loans = []
        self.reservations = []
        self.notifications = 0

        if self.user_type == "Aluno Graduação":
            self.emprestimo = EmprestimoAlunoGraduacaoStrategy()
        elif self.user_type == "Aluno Pós-Graduação":
            self.emprestimo = EmprestimoAlunoPosGraduacaoStrategy()
        elif self.user_type == "Professor":
            self.emprestimo = EmprestimoProfessorStrategy()
        else:
            self.emprestimo = None
            raise Exception("Tipo de usuário desconhecido.")
        
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

class Exemplar:
    def __init__(self, book_id, exemplar_id, status):
        self.book_id = book_id
        self.exemplar_id = exemplar_id
        self.status = status
        self.loaned_to = None
        self.loan_date = None
        self.return_date = None
