from strategy.emprestimo import EmprestimoStrategy

class EmprestimoAlunoGraduacaoStrategy(EmprestimoStrategy):
    def pode_emprestar(self, user, book):
        reserva_manager = user.reserva_manager
        emprestimo_manager = user.emprestimo_manager
        # Regra de Empréstimo para Alunos de Graduação
        if not book.exemplares_disponiveis():
            print(f"Não há exemplares disponíveis para o livro {book.title}")
            return False
        
        if emprestimo_manager.is_devedor():
            print(f"O usuário {user.name} está com empréstimos em atraso")
            return False
        
        if emprestimo_manager.livros_emprestados_count() >= 2:
            print(f"O usuário {user.name} já possui 2 empréstimos")
            return False
        
        if book.reservas_count() >= book.exemplares_count() and not reserva_manager.has_reservation(book):
            print(f"O livro {book.title} possui {book.reservas_count()} reservas e não está reservado por {user.name}")
            return False
        
        if emprestimo_manager.has_emprestimo(book):
            print(f"O usuário {user.name} já possui um exemplar do livro {book.title}")
            return False
        
        return True

    def tempo_emprestimo(self):
        return 4
