from singleton.biblioteca import LibrarySystem
from datetime import datetime, timedelta

class Command:
    def execute(self, carregador_parametros):
        pass

class EmprestimoCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro_um())
        book_id = int(carregador_parametros.get_parametro_dois())
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        book = next((b for b in library_system.books if b.book_id == book_id), None)
        
        if user and book:
            strategy = user.get_emprestimo_strategy()
            if strategy.pode_emprestar(user, book):
                exemplar = next((e for e in book.exemplars if e.status == "Disponível"), None)
                if exemplar:
                    exemplar.status = "Emprestado"
                    exemplar.loaned_to = user
                    exemplar.loan_date = datetime.now()
                    exemplar.return_date = datetime.now() + timedelta(days=strategy.tempo_emprestimo())
                    user.add_loans(exemplar)
                    print(f"Empréstimo realizado com sucesso para {user.name} - {book.title}")
                    print(user.loans)
                else:
                    print(f"Não há exemplares disponíveis para o livro {book.title}")
            else:
                print(f"Empréstimo não permitido para {user.name} - {book.title}")
        else:
            print("Usuário ou livro não encontrado.")

class DevolucaoCommand(Command):
    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def execute(self):
        # Implementar lógica de devolução aqui
        # ...código existente...
        pass

class ReservaCommand(Command):
    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def execute(self):
        # Implementar lógica de reserva aqui
        # ...código existente...
        pass

class ObservacaoCommand(Command):
    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

    def execute(self):
        # Implementar lógica de observação aqui
        # ...código existente...
        pass

class ConsultaLivroCommand(Command):
    def __init__(self, book_id):
        self.book_id = book_id

    def execute(self):
        # Implementar lógica de consulta de livro aqui
        # ...código existente...
        pass

class ConsultaUsuarioCommand(Command):
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        # Implementar lógica de consulta de usuário aqui
        # ...código existente...
        pass

class ConsultaNotificacoesCommand(Command):
    def __init__(self, user_id):
        self.user_id = user_id

    def execute(self):
        # Implementar lógica de consulta de notificações aqui
        # ...código existente...
        pass
