from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_devr_retornar_ok_e_ola_mundo():
    """ 
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUT)
    - A: Assert  - Garanta que A é A
    """
    # arrange
    client = TestClient(app)
    # act
    response = client.get('/')
    # assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}
