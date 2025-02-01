from strategy.emprestimo import EmprestimoStrategy

class EmprestimoAlunoGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Implementar regras específicas para alunos de graduação
        # ...existing code...
        pass

    def tempo_emprestimo(self):
        return 4
