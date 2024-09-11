from jwt import decode

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
