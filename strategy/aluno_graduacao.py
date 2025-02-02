from strategy.emprestimo import EmprestimoStrategy

class EmprestimoAlunoGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        # Regra de Empréstimo para Alunos de Graduação
        if not book.exemplares_disponiveis():
            print(f"Não há exemplares disponíveis para o livro {book.title}")
            return False
        if user.is_devedor():
            print(f"O usuário {user.name} está com empréstimos em atraso")
            return False
        if user.livros_emprestados_count() >= 2:
            print(f"O usuário {user.name} já possui 2 empréstimos")
            return False
        if book.reservas_count() >= book.exemplares_count() and not book.is_reserved_by(user):
            print(f"O livro {book.title} possui {book.reservas_count()} reservas e não está reservado por {user.name}")
            return False
        if user.has_emprestimo(book):
            print(f"O usuário {user.name} já possui um exemplar do livro {book.title}")
            return False
        return True

    def tempo_emprestimo(self):
        return 4
