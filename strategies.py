class EmprestimoStrategy:
    def pode_emprestar(self, user, book):
        pass

class EmprestimoAlunoGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para alunos de graduação
        # ...código existente...
        pass

class EmprestimoAlunoPosGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para alunos de pós-graduação
        # ...código existente...
        pass

class EmprestimoProfessorStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para professores
        # ...código existente...
        pass
