from flask import Blueprint,request,jsonify
from src.model import db
from src.model.reembolso_model import Reembolso

bp_reembolso = Blueprint('reembolso',__name__,url_prefix='/reembolso')

@bp_reembolso.route('/visualizar' , methods=['GET'])
def visualizar_reembolsos():
    meus_reembolsos = db.session.execute(
        db.select(Reembolso)
    ).scalars().all()
    
    meus_reembolsos = [ reembolso.to_dict() for reembolso in meus_reembolsos]
    
    return jsonify (meus_reembolsos)

@bp_reembolso.route('/Solicitar' , methods=['POST'])
def solicitar_reembolso():
    
    dados_reembolso = request.get_json()
    
    solicitacao = Reembolso(
        coloborador = dados_reembolso['coloborador'],
        empresa= dados_reembolso['empresa'],
        num_prestacao= dados_reembolso['num_prestacao'],
        descricao= dados_reembolso['descricao'],
        data= dados_reembolso['data'],
        tipo_reembolso= dados_reembolso['tio_reembolso'],
        centro_custo= dados_reembolso['centro_custo'],
        ordem_interna= dados_reembolso['ordem_interna'],
        divisao= dados_reembolso['divisao'],
        pep= dados_reembolso['pep'],
        moeda= dados_reembolso['moeda'],
        distancia_km= dados_reembolso['distancia_km'],
        valor_km= dados_reembolso['valor_km'],
        valor_faturado= dados_reembolso['valor_faturado'],
        dispesa= dados_reembolso['dispesa']
        
        
    )
    db.session.add(solicitacao)
    db.session.commit()
    
    return jsonify ({'mensagem: solicitacao enviada com sucesso'}) , 201