class CarregadorParametros:
    def __init__(self, parametros):
        self.parametros = parametros

    def get_parametro(self, index):
        return self.parametros[index] if index < len(self.parametros) else None
