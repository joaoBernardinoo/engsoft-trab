from singleton.biblioteca import LibrarySystem
from datetime import datetime, timedelta
from models.emprestimo import Emprestimo

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
        exemplar = next((e for e in book.exemplars if e.status == "Disponível"), None)
        
        if not (user and book):
            print("Usuário ou livro não encontrado.")
            return
            
        strategy = user.emprestimo

        if not strategy.pode_emprestar(user, book):
            print(f"Empréstimo de '{book.title}' não permitido para {user.name}")
            return
        
        if not exemplar:
            print(f"Não há exemplares disponíveis para o livro {book.title}")
            return
        
        # Verificar se o usuário possui uma reserva para o livro, se existir, remova a reserva
        self.handleReserva(user,book)
        
        exemplar.status = "Emprestado"
        exemplar.loaned_to = user
        exemplar.loan_date = datetime.now()
        exemplar.return_date = datetime.now() + timedelta(days=strategy.tempo_emprestimo())
        user.add_loan(exemplar)
        
        print(f"Empréstimo realizado com sucesso para {user.name} - {book.title}")

    def handleReserva(self,user,book):
        reservation = next((r for r in user.reservations if r.book.book_id == book.book_id), None)
        if reservation:
            user.remove_reservation(book.book_id)
            book.remove_reservation(user.user_id)

class DevolucaoCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        book_id = int(carregador_parametros.get_parametro(1))
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        book = next((b for b in library_system.books if b.book_id == book_id), None)
        
        if not (user and book):
            print("Usuário ou livro não encontrado.")
            return

        exemplar = next((e for e in book.exemplars if e.loaned_to == user), None)
        if not exemplar:
            print(f"Não há empréstimo em aberto para o livro {book.title} e o usuário {user.name}")
            return
        
        emprestimo = Emprestimo(exemplar.book, exemplar.loan_date, datetime.now())

        exemplar.status = "Disponível"
        exemplar.loaned_to = None
        exemplar.loan_date = None
        user.return_loan(exemplar)
        user.add_loan_history(emprestimo)
        print(f"Devolução realizada com sucesso para {user.name} - {book.title}")

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
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        book_id = int(carregador_parametros.get_parametro(0))
        book = next((b for b in library_system.books if b.book_id == book_id), None)

        if not book:
            print("Livro não encontrado.")
            return

        print(f"\nExemplares do livro '{book.title}':")
        for exemplar in book.exemplars:
            status = exemplar.status
            if status == "Disponível":
                print(f"  - Exemplar ID: {exemplar.exemplar_id} - Disponível")
            elif status == "Emprestado":
                print(f"  - Exemplar ID: {exemplar.exemplar_id} - Emprestado para {exemplar.loaned_to.name}")
                print(f"    Data de Empréstimo: {exemplar.loan_date.strftime('%d/%m/%Y')}")
                print(f"    Data de Devolução: {exemplar.return_date.strftime('%d/%m/%Y')}")
            elif status == "Reservado":
                print(f"  - Exemplar ID: {exemplar.exemplar_id} - Reservado por {exemplar.reserved_by.name}")

        if book.reservations:
            print("\nUsuários que reservaram este livro:")
            for reservation in book.reservations:
                print(f" ID: {reservation}")
        else:
            print("\nNenhuma reserva para este livro.")

class ReservaCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        book_id = int(carregador_parametros.get_parametro(1))
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        book = next((b for b in library_system.books if b.book_id == book_id), None)
        
        if not (user and book):
            print("Usuário ou livro não encontrado.")
            return

        if len(user.reservations) >= 3:
            print(f"Reserva não permitida para {user.name} - Limite de reservas atingido")
            return

        if any(reservation.book.book_id == book.book_id for reservation in user.reservations):
            print(f"Reserva não permitida para {user.name} - Usuário já possui reserva para o livro {book.title}")
            return
        
        if book.reservas_count() >= len(book.exemplars):
            print(f"Reserva não permitida para {user.name} - Todas as reservas estão preenchidas")
            return

        book.add_reservation(user)
        user.add_reservation(book)
        
        print(f"Reserva realizada com sucesso para {user.name} - {book.title}")

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

class ConsultaUsuarioCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        
        if user:
            print(f"Usuário: {user.name}, Tipo: {user.user_type}")

            loans = user.emprestimo_manager.get_loans()
            reservations = user.reserva_manager.get_reservations()

            print("Empréstimos:")
            if loans:
                for loan in loans:
                    print(f"  - Título: {loan['title']}")
                    print(f"    Data de Empréstimo: {loan['loan_date']}")
                    print(f"    Status: {loan['status']}")
                    return_date_label = "Data de Devolução Prevista" if loan['status'] == 'Em curso' else "Data de Devolução"
                    print(f"    {return_date_label}: {loan['return_date']}\n")
            else:
             print("  Não há empréstimos.")

            print("Reservas:")
            if reservations:
                for reservation in reservations:
                    print(f"  - Título: {reservation['title']}")
                    print(f"    Data de Reserva: {reservation['reservation_date']}\n")
            else:
                print("  Não há reservas.")
        else:
            print("Usuário não encontrado.")

class ConsultaNotificacoesCommand(Command):
    def execute(self, carregador_parametros):
        library_system = LibrarySystem.get_instance()
        user_id = int(carregador_parametros.get_parametro(0))
        
        user = next((u for u in library_system.users if u.user_id == user_id), None)
        
        if user:
            print(f"O professor {user.name} recebeu {user.observador.notifications} notificações de múltiplas reservas simultâneas.")
        else:
            print("Usuário não encontrado.")

