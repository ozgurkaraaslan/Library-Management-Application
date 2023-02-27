"""
Module for all book operations
"""
from .status import Status


class BookSearch:
    """A sub class for book searching from database"""

    def __init__(self, books_col):
        self.books_col = books_col

    def title(self, title):
        """
        Function for searching books according to the book title

        Parameters
        ----------
        title: str, default: None
            Title of the book that will be searched

        Returns
        -------
        dict
            Dictionary that includes "status", "message" and "data" keys
        """
        msg = []
        data = self.books_col.find({"title": title}, {"_id": 0})
        _data = None

        for _data in data:
            msg.append(_data)

        if not _data:
            return {
                "status": Status.Fail,
                "message": "Book does not exist.",
                "data": [],
            }
        else:
            return {"status": Status.Success, "message": "Book exists.", "data": msg}

    def author(self, author):
        """
        Function for searching books according to the book author

        Parameters
        ----------
        author: str, default: None
            Author of the book that will be searched

        Returns
        -------
        dict
            Dictionary that includes "status", "message" and "data" keys
        """
        msg = []
        data = self.books_col.find({"author": author}, {"_id": 0})
        _data = None

        for _data in data:
            msg.append(_data)

        if not _data:
            return {
                "status": Status.Fail,
                "message": "Book does not exist.",
                "data": [],
            }
        else:
            return {"status": Status.Success, "message": "Book exists.", "data": msg}

    def subject_category(self, subject_category):
        """
        Function for searching books according to the book subject category

        Parameters
        ----------
        subject_category: str, default: None
            Subject category of the book that will be searched

        Returns
        -------
        dict
            Dictionary that includes "status", "message" and "data" keys
        """
        msg = []

        data = self.books_col.find({"subject_category": subject_category}, {"_id": 0})
        _data = None
        for _data in data:
            msg.append(_data)

        if not _data:
            return {
                "status": Status.Fail,
                "message": "Book does not exist.",
                "data": [],
            }
        else:
            return {"status": Status.Success, "message": "Book exists.", "data": msg}

    def publication_date(self, publication_date):
        """
        Function for searching books according to the book publication date

        Parameters
        ----------
        publication_date: str, default: None
            Publication date of the book that will be searched

        Returns
        -------
        dict
            Dictionary that includes "status", "message" and "data" keys
        """
        msg = []
        data = self.books_col.find({"publication_date": publication_date}, {"_id": 0})
        _data = None
        for _data in data:
            msg.append(_data)

        if not _data:
            return {
                "status": Status.Fail,
                "message": "Book does not exist.",
                "data": [],
            }
        else:
            return {"status": Status.Success, "message": "Book exists.", "data": msg}
