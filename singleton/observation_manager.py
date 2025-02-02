from singleton.biblioteca import LibrarySystem
from observer.observers import NotificacaoObserver

class ObservationManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ObservationManager._instance is None:
            ObservationManager()
        return ObservationManager._instance

    def __init__(self):
        if ObservationManager._instance is not None:
            raise Exception("Esta classe é um singleton!")
        else:
            ObservationManager._instance = self
            self.observadores = {}  # ID do professor -> Conjunto de livros observados
            self.notificacao_observer = NotificacaoObserver()  # Gerencia notificações

    def adicionar_observador(self, professor_id, livro_id):
        """Adiciona um professor como observador de um livro."""
        if professor_id not in self.observadores:
            self.observadores[professor_id] = set()
        self.observadores[professor_id].add(livro_id)

    def verificar_reservas(self, livro_id):
        """Verifica se um livro tem mais de duas reservas e notifica os professores observadores."""
        library = LibrarySystem.get_instance()
        livro = next((b for b in library.books if b.id == livro_id), None)

        if livro and len(livro.reservas) > 2:  # Se houver mais de duas reservas
            for professor_id, livros in self.observadores.items():
                if livro_id in livros:
                    self.notificacao_observer.atualizar(professor_id)
