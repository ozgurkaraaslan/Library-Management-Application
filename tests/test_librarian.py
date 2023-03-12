
def test_login_is_success(librarian_object_mock):
    librarian_password = "13579"

    response = librarian_object_mock.login(librarian_password)

    assert response == {"status": 0, "message": "Login is successful."}


def test_login_is_fail(librarian_object_mock):
    librarian_password = "02468"

    response = librarian_object_mock.login(librarian_password)

    assert response == {"status": 1, "message": "Login is not successful."}
