
def test_search_by_title_is_success(book_search_object_mock):

    title = "1984"

    response = book_search_object_mock.title(title)

    assert response == {
        "status": 0,
        "message": "Book exists.",
        "data": [{'title': '1984', 'id': 16, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Reserved'}]
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
        "data": [{'title': '1984', 'id': 16, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Reserved'}],
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
        "data": [{'title': '1984', 'id': 16, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Reserved'}],
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
        "data": [{'title': '1984', 'id': 16, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Reserved'}],
    }


def test_search_by_publication_date_is_fail(book_search_object_mock):
    publication_date = "2024"
    response = book_search_object_mock.publication_date(publication_date)

    assert response == {
        "status": 1,
        "message": "Book does not exist.",
        "data": [],
    }


def test_show(book_object_mock):
    response = book_object_mock.show()

    assert response == {
        "status": 0,
        "message": "The books are listed.",
        "data": [{'title': '1984', 'id': 16, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Reserved'}],
    }
