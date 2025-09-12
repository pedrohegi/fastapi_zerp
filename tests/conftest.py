import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture  # funcao para passar o client para os testes
def client():
    """
    Funcao criada para aplicar o DRY,
    pois precisamos do client em todos os testes.
    """
    return TestClient(app)
