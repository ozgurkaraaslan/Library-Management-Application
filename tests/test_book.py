
def test_search_by_title_is_success(book_search_object_mock):

    title = "1984"

    response = book_search_object_mock.title(title)

    assert response == {
        "status": 0,
        "message": "Book exists.",
        "data": [{'title': '1984', 'id': 0, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Free'}]
    }


def test_search_by_title_is_fail(book_search_object_mock):
    title = "1983"

    response = book_search_object_mock.title(title)

    assert response == {
        "status": 1,
        "message": "Book does not exist.",
        "data": [],
    }


def test_search_by_author_is_success(book_search_object_mock):
    author = "George Orwell"
    response = book_search_object_mock.author(author)

    assert response == {
        "status": 0,
        "message": "Book exists.",
        "data": [{'title': '1984', 'id': 0, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Free'}],
    }


def test_search_by_author_is_fail(book_search_object_mock):
    author = "Yasar Kemal"
    response = book_search_object_mock.author(author)

    assert response == {
        "status": 1,
        "message": "Book does not exist.",
        "data": [],
    }


def test_search_by_subject_category_is_success(book_search_object_mock):
    subject_category = "Novel"
    response = book_search_object_mock.subject_category(subject_category)
    assert response == {
        "status": 0,
        "message": "Book exists.",
        "data": [{'title': '1984', 'id': 0, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Free'}],
    }


def test_search_by_subject_category_is_fail(book_search_object_mock):
    subject_category = "Religion"
    response = book_search_object_mock.subject_category(subject_category)

    assert response == {
        "status": 1,
        "message": "Book does not exist.",
        "data": [],
    }


def test_search_by_publication_date_is_success(book_search_object_mock):
    publication_date = "2012"
    response = book_search_object_mock.publication_date(publication_date)

    assert response == {
        "status": 0,
        "message": "Book exists.",
        "data": [{'title': '1984', 'id': 0, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Free'}],
    }


def test_search_by_publication_date_is_fail(book_search_object_mock):
    publication_date = "2024"
    response = book_search_object_mock.publication_date(publication_date)

    assert response == {
        "status": 1,
        "message": "Book does not exist.",
        "data": [],
    }

def test_reserve(book_object_mock):
    id_ = 0
    response = book_object_mock.reserve(id_)
    assert response == {"status": 0, "message": "The book is reserved successfully."}

    response = book_object_mock.reserve(id_)
    assert response == {"status": 1, "message": "The book is not free."}

    id_ = -1
    response = book_object_mock.reserve(id_)
    assert response == {"status": 1, "message": "The book not found."}

def test_occupy(book_object_mock):
    id_ = 0
    response = book_object_mock.occupy(id_)
    assert response == {"status": 0, "message": "The book is occupied successfully."}
    
    response = book_object_mock.occupy(id_)
    assert response == {"status": 1, "message": "The book is not free."}

    id_ = -1
    response = book_object_mock.occupy(id_)
    assert response == {"status": 1, "message": "The book not found."}

def test_return_(book_object_mock):
    id_ = 0
    book_object_mock.occupy(id_)

    response = book_object_mock.return_(id_)
    assert response == {"status": 0, "message": "The book is returned succesfully."}

    response = book_object_mock.return_(id_)
    assert response == {"status": 1, "message": "The book is already free."}

    id_ = -1
    response = book_object_mock.return_(id_)
    assert response == {"status": 1, "message": "The book not found."}

def test_show(book_object_mock):
    response = book_object_mock.show()

    assert response == {
        "status": 0,
        "message": "The books are listed.",
        "data": [{'title': '1984', 'id': 0, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Free'}],
    }

def test_add_is_success(book_object_mock):
    response = book_object_mock.add("Improbable","Adam Fawer", "Science-Fiction", "2016", "AA333")

    assert response == {"status": 0, "message": "The new book is added."}

"""
def test_add_is_fail(book_object_mock):
    response = book_object_mock.add("Improbable","Adam Fawer", "Science-Fiction", "2016")

    assert response == {
                "status": 1,
                "message": "The new book could not be added.",
            }
"""

def test_remove(book_object_mock):
    response = book_object_mock.remove(1)

    assert response == {"status": 0, "message": "The book is deleted."}
