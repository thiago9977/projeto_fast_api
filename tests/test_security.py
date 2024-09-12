from jwt import decode
from http import HTTPStatus
from projeto_fast_api.security import (
    ALGORITHM,
    SECRET_KEY,
    create_access_token,
)


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, SECRET_KEY, ALGORITHM)

    assert decoded['test'] == data['test']
    assert decoded['exp']  # testa se o valor de exp foi adicionado ao  token

def test_jwt_invalid_token(client):
    response = client.delete('/users/1', headers= {'Authorization': 'Bearer token-invalido'})
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
    