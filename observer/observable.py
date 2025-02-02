class Observable:
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

class NotificacaoObserver:
    def __init__(self):
        self.notificacoes = {}  # Armazena a quantidade de notificações por professor

    def atualizar(self, professor_id):
        """Incrementa o contador de notificações para um professor."""
        if professor_id not in self.notificacoes:
            self.notificacoes[professor_id] = 0
        self.notificacoes[professor_id] += 1

