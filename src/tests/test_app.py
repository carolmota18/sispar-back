import pytest
from src.app import create_app
from src.model.colaborador_model import Colaborador

@pytest.fixture #cofigurar os testes
def app():
    app = create_app()
    yield app # armazenar o valor em memoria
    
    
@pytest.fixture #configura nosso testes de requisicao
def client(app):
    return app.test_client()

def test_pegar_todos_colaboradores(client):
    resposta = client.get('/colaborador/todos-colaboradores')
    
    assert resposta.status_code == 200