from singleton.biblioteca import LibrarySystem
from command.carregador_parametros import CarregadorParametros
from command.interface_usuario import InterfaceUsuario

# crie uma função que executa um comando ex: "execute("emp 123 100")
def execute(command):
    library_system = LibrarySystem.get_instance()
    interface_usuario = InterfaceUsuario()
    parts = command.split()
    str_comando = parts[0]
    parametros = CarregadorParametros(parts[1:])
    interface_usuario.executar_comando(str_comando, parametros)

def main():
    library_system = LibrarySystem.get_instance()
    interface_usuario = InterfaceUsuario()

if __name__ == "__main__":
    main()
