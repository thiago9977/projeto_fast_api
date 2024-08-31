from sqlalchemy import select

from projeto_fast_api.models import User


def test_create_user(session):

    user = User(username='Thiago', email='thiago@gmail.com', password='senhasecreta')
    session.add(user)
    session.commit()
    session.scalar(select(User).where(User.email == 'thiagoj@gmail.com'))
    assert user.username == 'Thiago'
