
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

def test_user_operations(user_object_mock):
    response = user_object_mock.operations(5)
    assert response == {"status": 3, "message": "Logged out."}

    response = user_object_mock.operations(6)
    assert response == {"status": 2, "message": "Invalid input!"}
