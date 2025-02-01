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