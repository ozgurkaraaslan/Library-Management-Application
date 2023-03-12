
def test_login_is_success(user_object_mock):
    username = "Ozgur"
    password = "1234"

    response = user_object_mock.login(username, password)

    assert response == {"status": 0, "message": "Login is successful."}


def test_login_is_fail(user_object_mock):
    username = "Ozgur"
    password = "123456"

    response = user_object_mock.login(username, password)

    assert response == {"status": 1, "message": "Login is not successful."}
