from models.book import Book
from models.user import User
from models.exemplar import Exemplar

class LibrarySystem:
    _instance = None

    @staticmethod
    def get_instance():
        if LibrarySystem._instance is None:
            LibrarySystem()
        return LibrarySystem._instance

    def __init__(self):
        if LibrarySystem._instance is not None:
            raise Exception("Esta classe é um singleton!")
        else:
            LibrarySystem._instance = self
            self.users = []
            self.books = []
            self._initialize_test_data()

    def _initialize_test_data(self):
        # Usuários
        self.users.append(User(123, "Aluno Graduação", "João da Silva"))
        self.users.append(User(456, "Aluno Pós-Graduação", "Luiz Fernando Rodrigues"))
        self.users.append(User(789, "Aluno Graduação", "Pedro Paulo"))
        self.users.append(User(100, "Professor", "Carlos Lucena"))

        # Livros
        books_data = [
            (100, "Engenharia de Software", "Addison Wesley", "Ian Sommerville", "6ª", 2000, 3),
            (101, "UML - Guia do Usuário", "Campus", "Grady Booch, James Rumbaugh, Ivar Jacobson", "7ª", 2000, 1),
            (200, "Code Complete", "Microsoft Press", "Steve McConnell", "2ª", 2014, 1),
            (201, "Agile Software Development, Principles, Patterns and Practices", "Prentice Hall", "Robert Martin", "1ª", 2002, 1),
            (300, "Refactoring: Improving the Design of Existing Code", "Addison Wesley", "Martin Fowler", "1ª", 1999, 1),
            (301, "Software Metrics: A rigorous and Practical Approach", "CRC Press", "Norman Fenton, James Bieman", "3ª", 2014, 0),
            (400, "Design Patterns: Elements of Reusable Object-Oriented Software", "Addison Wesley", "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", "1ª", 1994, 0),
            (401, "UML Distilled: A Brief Guide to the Standard Object Modeling Language", "Addison Wesley", "Martin Fowler", "3ª", 2003, 0)
        ]

        exemplar_id_counter = 1
        for book_data in books_data:
            book_id, title, publisher, authors, edition, year, exemplars_count = book_data
            book = Book(book_id, title, publisher, authors, edition, year)
            for _ in range(exemplars_count):
                book.add_exemplar(Exemplar(book_id, exemplar_id_counter, "Disponível"))
                exemplar_id_counter += 1
            self.books.append(book)
