import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
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

    table_registry.metadata.drop_all(engine)
