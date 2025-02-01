from strategy.strategies import EmprestimoAlunoGraduacaoStrategy, EmprestimoAlunoPosGraduacaoStrategy, EmprestimoProfessorStrategy

class User:
    def __init__(self, user_id, user_type, name):
        self.user_id = user_id
        self.user_type = user_type
        self.name = name
        self.loans = []
        self.reservations = []
        self.notifications = 0

    def get_emprestimo_strategy(self):
        strategies = {
            "Aluno Graduação": EmprestimoAlunoGraduacaoStrategy,
            "Aluno Pós-Graduação": EmprestimoAlunoPosGraduacaoStrategy,
            "Professor": EmprestimoProfessorStrategy
        }
        return strategies[self.user_type]()