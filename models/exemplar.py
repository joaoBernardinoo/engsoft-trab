from datetime import datetime

class Exemplar:
    def __init__(self, book_id, exemplar_id, status):
        self._book_id = book_id
        self._exemplar_id = exemplar_id
        self._status = status
        self._loaned_to = None
        self._loan_date = None
        self._return_date = None

    @property
    def book_id(self):
        return self._book_id
    
    @property
    def exemplar_id(self):
        return self._exemplar_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def loaned_to(self):
        return self._loaned_to

    @loaned_to.setter
    def loaned_to(self, user):
        self._loaned_to = user

    @property
    def loan_date(self):
        return self._loan_date

    @loan_date.setter
    def loan_date(self, date):
        self._loan_date = date

    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, date):
        self._return_date = date

    def is_overdue(self):
        if self._return_date and datetime.now() > self._return_date:
            return True
        return False
