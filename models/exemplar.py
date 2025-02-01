class Exemplar:
    def __init__(self, book_id, exemplar_id, status):
        self.book_id = book_id
        self.exemplar_id = exemplar_id
        self.status = status
        self.loaned_to = None
        self.loan_date = None
        self.return_date = None
