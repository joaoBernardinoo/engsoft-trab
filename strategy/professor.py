from strategy.emprestimo import EmprestimoStrategy

class EmprestimoProfessorStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Regra de Empréstimo para Professores
        if not book.exemplares_disponiveis():
            print(f"Não há exemplares disponíveis para o livro {book.title}")
            return False
        
        if user.is_devedor():
            print(f"O usuário {user.name} está com empréstimos em atraso")
            return False
        
        if user.has_emprestimo(book):
            print(f"O usuário {user.name} já possui um exemplar do livro {book.title}")
            return False
        return True

    def tempo_emprestimo(self):
        return 8
