from strategy.emprestimo import EmprestimoStrategy

class EmprestimoAlunoPosGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para alunos de pós-graduação
        # ...existing code...
        pass

    def tempo_emprestimo(self):
        return 5
