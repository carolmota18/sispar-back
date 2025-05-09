
from flask import Blueprint,request,jsonify
from src.model import db
from src.model.colaborador_model import Colaborador
from src.security.security import hash_senha, checar_senha
from flasgger import swag_from
#request = trabalha  com as requisições
#jsonify = trabalha com as respostas

bp_colaborador = Blueprint('colaborador', __name__ ,url_prefix='/colaborador')

@bp_colaborador.route('/todos-colaboradores')
def pegar_dados_todos_colaboradores():
    colaboradores = db.session.execute(
        db.select(Colaborador)
    ).scalars().all()
    
    colaboradores = [ colaborador.all_data() for colaborador in colaboradores]
    
    return jsonify(colaboradores), 200

@bp_colaborador.route('/cadastrar', methods=['POST']) 
@swag_from('..docs/colaborador/cadrastar_colaborador.yml')
def cadastrar_novo_colaborador():
    
    dados_colaborador = request.get_json()
    
    novo_colaborador = Colaborador(
        
        nome=dados_colaborador['nome'],
        email=dados_colaborador['email'],
        senha=hash_senha(dados_colaborador['senha']),
        cargo=dados_colaborador['cargo'],
        salario=dados_colaborador['salario']
    )
    db.session.add(novo_colaborador)
    db.session.commit()
  
    
    return jsonify({'mensagem':'colaborador cadastrado com sucesso'}), 201
# SDinaliza que os dados enviados
# enderenço?colaborador?autalixar?10030   
@bp_colaborador.route('/atualizar/<int:id_colaborador>',methods=['PUT'])
def atualizar_dados_colaborador(id_colaborador):

    dados_requisicao = request.get_json()
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.id == id_colaborador)
    )
    for dados_colaborador in colaborador:
        if dados_colaborador['id'] == id_colaborador:
            colaborador_encontrado = dados_colaborador
            break
    if 'nome' in dados_requisicao:
            colaborador_encontrado['nome'] = dados_requisicao['nome']
    if 'nome' in dados_requisicao:
            colaborador_encontrado['cargo'] = dados_requisicao['cargo']
    return jsonify({'mensagem':'Dados do colaborador atualizado com sucesso'}),200

@bp_colaborador.route('/login',methods=['POST'])
def login():
    dados_requisicao = request.get_json()
    
    email = dados_requisicao.get('email')
    senha = dados_requisicao.get('senha')
    
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os dados precisam ser enviados'}),400
    
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.email == email)
    ).scalar()
    
    if not colaborador:
        return jsonify({'mensagem': 'Usuario não encontrado'}),404
    
    colaborador = colaborador.to_dict()
    
    if email == colaborador.get('email') and senha == colaborador.get('senha'):
        return jsonify({'mensagem': 'Login realizado com sucesso'}),200
    
    else:
        return jsonify({'mensagem': 'Credenciais invalidas'}), 400
   