from strategy.emprestimo import EmprestimoStrategy

class EmprestimoAlunoPosGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Regra de Empréstimo para Alunos de Pós Graduação
        if not book.exemplares_disponiveis():
            return False
        if user.is_devedor():
            return False
        if user.livros_emprestados_count() >= 3:
            return False
        if book.reservas_count() >= book.exemplares_count() and not book.is_reserved_by(user):
            return False
        if user.has_emprestimo(book):
            return False
        return True

    def tempo_emprestimo(self):
        return 5
