from http import HTTPStatus

from projeto_fast_api.schemas import UserPublic


def test_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):

    response = client.post('/users/', json={'username': 'alice', 'email': 'alice@example.com', 'password': 'secpipret', },)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'username': 'alice', 'email': 'alice@example.com', 'id': 1, }


def test_create_user_error_username(client, user):

    response = client.post('/users/', json={'username': 'Teste', 'email': 'teste@test.com', 'password': 'testtest', },)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_user_error_email(client, user):

    response = client.post('/users/', json={'username': 'thiago', 'email': 'teste@test.com', 'password': 'testtest', },)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_usersf_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user_error(client, user, token):
    response = client.put(f'/users/{user.id + 1}', headers={'Authorization': f'Bearer {token}'},
                json={'username': 'thiago', 'email': 'thiafo@rmai.com', 'password': 'awer', 'id': 2})
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_update_user(client, user, token):
    response = client.put('/users/1', headers={'Authorization': f'Bearer {token}'},
        json={'username': 'bob', 'email': 'bob@example.com', 'password': 'mynewpassword', },)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'username': 'bob', 'email': 'bob@example.com', 'id': 1, }


def test_delete_user_error(client, user, token):
    response = client.delete(f'/users/{user.id + 2}', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_delete_user(client, user, token):
    response = client.delete(f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_get_token(client, user):
    response = client.post('/token', data={'username': user.email, 'password': user.clean_password},)
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token
