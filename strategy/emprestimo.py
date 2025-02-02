class EmprestimoStrategy:
    def pode_emprestar(self, user, book):
        raise NotImplementedError

    def tempo_emprestimo(self):
        raise NotImplementedError
