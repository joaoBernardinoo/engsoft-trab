from singleton.biblioteca import LibrarySystem
from datetime import datetime, timedelta

class Command:
    def execute(self, carregador_parametros):
        pass

class EmprestimoCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        book_id = int(carregador_parametros.get_parametro(1))
        
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
                    user.add_loan(exemplar)
                    print(f"Empréstimo realizado com sucesso para {user.name} - {book.title}")
                    print([emprestado.exemplar_id for emprestado in user.loans])
                else:
                    print(f"Não há exemplares disponíveis para o livro {book.title}")
            else:
                print(f"Empréstimo não permitido para {user.name} - {book.title}")
        else:
            print("Usuário ou livro não encontrado.")

class DevolucaoCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        book_id = int(carregador_parametros.get_parametro(1))
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        book = next((b for b in library_system.books if b.book_id == book_id), None)
        
        if user and book:
            exemplar = next((e for e in book.exemplars if e.loaned_to == user), None)
            if exemplar:
                exemplar.status = "Disponível"
                exemplar.loaned_to = None
                exemplar.loan_date = None
                exemplar.return_date = None
                user.loans.remove(exemplar)
                print(f"Devolução realizada com sucesso para {user.name} - {book.title}")
            else:
                print(f"Não há empréstimo em aberto para o livro {book.title} e o usuário {user.name}")
        else:
            print("Usuário ou livro não encontrado.")

class ListarUsuariosCommand(Command):
    def execute(self, carregador_parametros=None):
        library_system = LibrarySystem.get_instance()
        if not library_system.users:
            print("Nenhum usuário cadastrado.")
            return
        print("Usuários cadastrados:")
        for user in library_system.users:
            print(f"ID: {user.user_id}, Nome: {user.name}, Tipo: {user.user_type}")

class ListarLivrosCommand(Command):
    def execute(self, carregador_parametros=None):
        library_system = LibrarySystem.get_instance()
        if not library_system.books:
            print("Nenhum livro cadastrado.")
            return
        print("Livros disponíveis:")
        for book in library_system.books:
            print(f"ID: {book.book_id}, Título: {book.title}, Autor(es): {book.authors}, Editora: {book.publisher}, Ano: {book.year}")

class ConsultaExemplaresLivroCommand(Command):
    def execute(self,carregador_parametros):
        library_system = LibrarySystem.get_instance()
        book_id = int(carregador_parametros.get_parametro(0))
        book = next((b for b in library_system.books if b.book_id == book_id), None)
        if not book:
            print("Livro não encontrado.")
            return
        print(f"Exemplares do livro '{book.title}':")
        for exemplar in book.exemplars:
            status = exemplar.status
            if status == "Disponível":
                print(f"Exemplar ID: {exemplar.exemplar_id} - Disponível")
            elif status == "Emprestado":
                print(f"Exemplar ID: {exemplar.exemplar_id} - Emprestado para {exemplar.loaned_to.name}")
            elif status == "Reservado":
                print(f"Exemplar ID: {exemplar.exemplar_id} - Reservado por {exemplar.reserved_by.name}")

class ReservaCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        book_id = int(carregador_parametros.get_parametro(1))
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        book = next((b for b in library_system.books if b.book_id == book_id), None)
        
        if user and book:
            exemplar = next((e for e in book.exemplars if e.status == "Disponível"), None)
            
            if not exemplar:
                print(f"Não há exemplares disponíveis para o livro {book.title}")

            if len(user.reservations) >= 3:
                print(f"Reserva não permitida para {user.name} - Limite de reservas atingido")
                return

            if any(reservation.user_id == user.user_id for reservation in book.reservations):
                print(f"Reserva não permitida para {user.name} - Usuário já possui reserva para o livro {book.title}")
                return
            
            if len(book.reservations) >= len(book.exemplars):
                    print(f"Reserva não permitida para {user.name} - Todas as reservas estão preenchidas")
                    return

            book.add_reservation(user_id)
            user.add_reservation(book_id)
            
            print(f"Reserva realizada com sucesso para {user.name} - {book.title}")
            
        else:
            print("Usuário ou livro não encontrado.")

class ObservacaoCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        book_id = int(carregador_parametros.get_parametro(1))
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        book = next((b for b in library_system.books if b.book_id == book_id), None)
        
        if user and book:
            user.observar(book)
        else:
            print("Usuário ou livro não encontrado.")

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

