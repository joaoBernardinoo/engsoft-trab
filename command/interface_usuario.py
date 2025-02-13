from command.commands import EmprestimoCommand, ListarUsuariosCommand, ListarLivrosCommand, ConsultaExemplaresLivroCommand, DevolucaoCommand, ObservacaoCommand, ReservaCommand, ConsultaUsuarioCommand, ConsultaNotificacoesCommand

class InterfaceUsuario:
    def __init__(self):
        self.comandos = {
            "emp": EmprestimoCommand(),
            "dev": DevolucaoCommand(),
            "lus": ListarUsuariosCommand(),
            "llv": ListarLivrosCommand(),
            "liv": ConsultaExemplaresLivroCommand(),
            "obs": ObservacaoCommand(),
            "res": ReservaCommand(),
            "usu": ConsultaUsuarioCommand(),
            "ntf": ConsultaNotificacoesCommand()
        }

    def executar_comando(self, str_comando, parametros):
        comando = self.comandos.get(str_comando)
        if comando:
            comando.execute(parametros)
        else:
            print("Comando não reconhecido.")
