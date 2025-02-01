from strategy.emprestimo import EmprestimoStrategy

class EmprestimoProfessorStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para professores
        # ...existing code...
        pass

    def tempo_emprestimo(self):
        return 8
