from singleton.biblioteca import LibrarySystem
from command.carregador_parametros import CarregadorParametros
from command.interface_usuario import InterfaceUsuario

def main():
    library_system = LibrarySystem.get_instance()
    interface_usuario = InterfaceUsuario()
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
        str_comando = parts[0]
        parametros = CarregadorParametros(parts[1:])
        interface_usuario.executar_comando(str_comando, parametros)

if __name__ == "__main__":
    main()
