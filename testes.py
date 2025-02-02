from singleton.biblioteca import LibrarySystem
from command.carregador_parametros import CarregadorParametros
from command.interface_usuario import InterfaceUsuario

# crie uma função que executa um comando ex: "execute("emp 123 100")
def addCommand(command):
    # print(command)
    library_system = LibrarySystem.get_instance()
    interface_usuario = InterfaceUsuario()
    parts = command.split()
    str_comando = parts[0]
    parametros = CarregadorParametros(parts[1:])
    interface_usuario.executar_comando(str_comando, parametros)

def main():
    addCommand("res 123 200")
    addCommand("liv 200")
    addCommand("emp 123 200")
    # print("----")
    # addCommand("res 123 100")
    # addCommand("liv 100")
    # addCommand("emp 123 100")
    # addCommand("res 456 101")
    # addCommand("emp 456 101")
    # addCommand("dev 123 101")
    # addCommand("res 456 101")
    # addCommand("emp 456 101")
if __name__ == "__main__":
    main()
