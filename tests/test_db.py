from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,  # Exercício
    }


def test_create_user_2(session, mock_db_time):
    with mock_db_time(model=User) as time:
        user = User(
            username='test',
            password='minha_senha-legal',
            email='test@test.com',
        )
        session.add(user)  # adiciona
        session.commit()  # insere no banco
        # session.refresh(user)  # atualiza o dado

        result = session.scalar(
            select(User).where(User.email == 'test@test.com')
        )

    assert asdict(result) == {
        'id': 1,
        'username': 'test',
        'password': 'minha_senha-legal',
        'email': 'test@test.com',
        'created_at': time,
        'updated_at': time,
    }
    session.close()
