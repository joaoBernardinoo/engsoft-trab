from singleton.biblioteca import LibrarySystem
from command.commands import EmprestimoCommand, ListarUsuariosCommand, ListarLivrosCommand
from command.carregador_parametros import CarregadorParametros

def main():
    library_system = LibrarySystem.get_instance()
    # ...código existente...
    print("Comandos disponíveis:")
    print("emp [user_id] [book_id] - Empréstimo de livro")
    print("dev [user_id] [book_id] - Devolução de livro")
    print("res [user_id] [book_id] - Reserva de livro")
    print("obs [user_id] [book_id] - Observação de livro")
    print("liv [book_id] - Consulta de informações de livro")
    print("usu [user_id] - Consulta de informações de usuário")
    print("ntf [user_id] - Consulta de notificações recebidas")
    print("lus - Listar todos os usuários cadastrados")
    print("llv - Listar todos os livros disponíveis")
    print("sair - Sair do sistema")
    while True:
        command = input("Digite o comando: ")
        if command == "sair":
            break
        parts = command.split()
        if parts[0] == "emp" and len(parts) == 3:
            user_id = parts[1]
            book_id = parts[2]
            carregador_parametros = CarregadorParametros(user_id, book_id)
            EmprestimoCommand().execute(carregador_parametros)
        elif parts[0] == "lus":
            ListarUsuariosCommand().execute()
        elif parts[0] == "llv":
            ListarLivrosCommand().execute()
        # Processar outros comandos
        # ...código existente...

if __name__ == "__main__":
    main()
