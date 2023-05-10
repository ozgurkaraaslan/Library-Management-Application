
def test_login_is_success(librarian_object_mock):
    librarian_password = "13579"

    response = librarian_object_mock.login(librarian_password)

    assert response == {"status": 0, "message": "Login is successful."}

def test_login_is_fail(librarian_object_mock):
    librarian_password = "02468"

    response = librarian_object_mock.login(librarian_password)

    assert response == {"status": 1, "message": "Login is not successful."}

def test_librarian_operations(librarian_object_mock, mocker):
    mocker.patch("src.classes.book.Book.show", return_value=1)
    response = librarian_object_mock.operations(1)
    assert response == 1

    response = librarian_object_mock.operations(2)
    assert response == {
                    "status": 0,
                    "message": "All the users are listed",
                    "data": [{"username": "Ozgur", "password": "1234", "occupied_books": ["-1"]}],
                }
    
    response = librarian_object_mock.operations(5)
    assert response == {"status": 3, "message": "Logged out"}

    response = librarian_object_mock.operations(6)
    assert response == {"status": 2, "message": "Invalid input!"}