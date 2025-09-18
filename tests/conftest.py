from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models import table_registry


@pytest.fixture  # funcao para passar o client para os testes
def client():
    """
    Funcao criada para aplicar o DRY,
    pois precisamos do client em todos os testes.
    """
    return TestClient(app)


@pytest.fixture  # funcao para passar a session para os test_db
def session():
    engine = create_engine('sqlite:///:memory:')

    table_registry.metadata.create_all(engine)

    # gerenciamento de contexto
    with Session(engine) as session:
        yield session
        session.close()

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def mock_db_time():
    """Fixture que retorna um context manager para mockar timestamps."""

    @contextmanager
    def _mock(model, time=datetime(2024, 1, 1)):
        def fake_time_handler(mapper, connection, target):
            if hasattr(target, 'created_at'):
                target.created_at = time
            if hasattr(target, 'updated_at'):
                target.updated_at = time

        event.listen(model, 'before_insert', fake_time_handler)
        yield time
        event.remove(model, 'before_insert', fake_time_handler)

    return _mock
