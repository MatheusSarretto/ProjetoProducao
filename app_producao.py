from flask import Flask, jsonify, request
from funcionarios_controller import FuncionariosController
from maquinas_controller import MaquinasController
from ordens_producao_controller import OrdensProducaoController

app_producao = Flask(__name__)
funcionario = FuncionariosController()
maquina = MaquinasController()
ordens_producao = OrdensProducaoController()

@app_producao.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    dados = funcionario.listar()
    return jsonify(dados)

@app_producao.route('/funcionarios/<int:id>', methods=['GET'])
def buscar_funcionario(id):
    dados = funcionario.buscar(id)
    if dados:
        return jsonify(dados)
    return jsonify({"erro": "Funcionário não encontrado"}), 404

@app_producao.route('/funcionarios', methods=['POST'])
def adicionar_funcionario():
    dados = request.get_json()
    funcionario.adicionar(dados['nome'], dados['setor'])
    return jsonify({"mensagem": "Funcionário adicionado com sucesso!"}), 201

@app_producao.route('/funcionarios', methods=['PUT'])
def atualizar_funcionario():
    dados = request.get_json()
    funcionario.atualizar(dados['id'], dados['nome'], dados['setor'])
    return jsonify({"mensagem": "Funcionário atualizado com sucesso!"})

@app_producao.route('/funcionarios/<int:id>', methods=['DELETE'])
def remover_funcionario(id):
    dados_funcionario = funcionario.buscar(id)
    if not dados_funcionario:
        return jsonify({"erro": "Funcionário não encontrado"}), 404
    funcionario.excluir(id)
    return jsonify({"mensagem": "Funcionário removido com sucesso!"})

@app_producao.route('/maquinas', methods=['GET'])
def listar_maquinas():
    dados = maquina.listar()
    return jsonify(dados)

@app_producao.route('/maquinas/<int:id>', methods=['GET'])
def buscar_maquina(id):
    dados = maquina.buscar(id)
    if dados:
        return jsonify(dados)
    return jsonify({"erro": "Máquina não encontrada"}), 404

@app_producao.route('/maquinas', methods=['POST'])
def adicionar_maquina():
    dados = request.get_json()
    maquina.adicionar(dados['descricao'], dados['status'])
    return jsonify({"mensagem": "Máquina adicionada com sucesso!"}), 201

@app_producao.route('/maquinas', methods=['PUT'])
def atualizar_maquina():
    dados = request.get_json()
    maquina.atualizar(dados['id'], dados['descricao'], dados['status'])
    return jsonify({"mensagem": "Máquina atualizada com sucesso!"})

@app_producao.route('/maquinas/<int:id>', methods=['DELETE'])
def remover_maquina(id):
    dados_maquina = maquina.buscar(id)
    if not dados_maquina:
        return jsonify({"erro": "Máquina não encontrada"}), 404
    maquina.excluir(id)
    return jsonify({"mensagem": "Máquina removida com sucesso!"})

@app_producao.route('/ordens_producao', methods=['GET'])
def listar_ordens_producao():
    dados = ordens_producao.listar()
    return jsonify(dados)

@app_producao.route('/ordens_producao/<int:id>', methods=['GET'])
def buscar_ordem(id):
    dados = ordens_producao.buscar(id)
    if dados:
        return jsonify(dados)
    return jsonify({"erro": "Ordem de produção não encontrada"}), 404

@app_producao.route('/ordens_producao', methods=['POST'])
def adicionar_ordem_producao():
    dados = request.get_json()
    ordens_producao.adicionar(dados['produto'], dados['quantidade'], dados['status'])
    return jsonify({"mensagem": "Ordem de produção adicionada com sucesso!"}), 201

@app_producao.route('/ordens_producao', methods=['PUT'])
def atualizar_ordem_producao():
    dados = request.get_json()
    ordens_producao.atualizar(dados['id'], dados['produto'], dados['quantidade'], dados['status'])
    return jsonify({"mensagem": "Ordem de produção atualizada com sucesso!"})

@app_producao.route('/ordens_producao/<int:id>', methods=['DELETE'])
def remover_ordem_producao(id):
    dados_ordem = ordens_producao.buscar(id)
    if not dados_ordem:
        return jsonify({"erro": "Ordem de produção não encontrada"}), 404
    ordens_producao.excluir(id)
    return jsonify({"mensagem": "Ordem de produção removida com sucesso!"})

if __name__ == '__main__':
    app_producao.run(debug=True)