from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session):
    user = User(
        username='test',
        password='minha_senha-legal',
        email='test@test.com',
    )

    session.add(user)  # adiciona
    session.commit()  # insere no banco
    # session.refresh(user)  # atualiza o dado

    result = session.scalar(select(User).where(User.email == 'test@test.com'))

    assert user.id == 1
    assert result.username == 'test'
