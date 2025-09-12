from http import HTTPStatus


def test_root_devr_retornar_ok_e_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUT)
    - A: Assert  - Garanta que A é A
    """
    # act
    response = client.get('/')
    # assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'testusername',
            'email': 'teste@teste.com',
            'password': 'password',
        },
    )
    # Validar o UserPublic
    # voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'testusername', 'email': 'teste@teste.com', 'id': 1}
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'teste2@teste.com',
            'id': 1,
            'password': '123',
        },
    )
    assert response.json() == {
        'username': 'testusername2',
        'email': 'teste2@teste.com',
        'id': 1,
    }


def test_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'testusername2',
            'email': 'teste2@teste.com',
            'id': 2,
            'password': '123',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User Deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/123')
    assert response.status_code == HTTPStatus.NOT_FOUND
