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
    # addCommand("res 123 101")
    # addCommand("res 456 101")
    # addCommand("emp 456 101")
    # addCommand("emp 123 101")
    # addCommand("dev 123 101")
    # addCommand("res 456 101")
    # addCommand("emp 456 101")

    addCommand("lus")
    addCommand("llv")

    print("\nTestar Observação")
    addCommand("obs 100 100")
    addCommand("obs 100 101")
    addCommand("res 123 100")
    addCommand("res 456 100")
    addCommand("res 123 101")
    addCommand("ntf 100")
    addCommand("res 789 100")
    addCommand("ntf 100")
    addCommand("res 456 101")
    addCommand("res 789 101")
    addCommand("ntf 100")





    print("\nTestar Consulta Livros")
    addCommand("liv 100")
    addCommand("liv 101")


    print("\nTestar Histórico de Emprestimo")
    addCommand("emp 123 101")
    addCommand("dev 123 101")
    addCommand("emp 123 100")
    
    print("\nTeste Consulta Usuario")
    addCommand("res 123 100")
    addCommand("usu 123")


if __name__ == "__main__":
    main()
