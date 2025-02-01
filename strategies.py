class EmprestimoStrategy:
    def pode_emprestar(self, user, book):
        pass

    def tempo_emprestimo(self):
        pass

class EmprestimoAlunoGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para alunos de graduação
        # ...código existente...
        pass

    def tempo_emprestimo(self):
        return 4

class EmprestimoAlunoPosGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para alunos de pós-graduação
        # ...código existente...
        pass

    def tempo_emprestimo(self):
        return 5

class EmprestimoProfessorStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para professores
        # ...código existente...
        pass

    def tempo_emprestimo(self):
        return 8
