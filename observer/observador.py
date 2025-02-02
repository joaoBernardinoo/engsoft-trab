class Observador:
    def __init__(self, user):
        self.user = user
        self.notifications = 0

    def update(self, book):
        self.notifications += 1
        # print(f"Notificação para {self.user.name}: O livro {book.title} atingiu mais de duas reservas simultâneas.")
