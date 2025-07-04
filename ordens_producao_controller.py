from conexao import Conexao

class OrdensProducaoController():

    def __init__(self):
        db = Conexao()
        self.conn = db.get_conexao()
        self.cursor = db.get_cursor()

    def get_conn(self):
        return self.conn

    def get_cursor(self):
        return self.cursor

    def listar(self):
        self.get_cursor().execute("SELECT * FROM ordens_producao;")
        linhas = self.get_cursor().fetchall()
        lista = []
        for linha in linhas:
            dicionario = {
                'ordem_id':linha[0],
                'funcionario_id': linha[1],
                'maquina_id':linha[2],
                'produto':linha[3],
                'quantidade':linha[4],
                'status':linha[5]
            }
            lista.append(dicionario)
        return lista

    def buscar(self, id):
        self.get_cursor().execute("SELECT * FROM ordens_producao WHERE ordem_id = %s;", (id,))
        linha = self.get_cursor().fetchone()
        dicionario = {
            'ordem_id':linha[0],
            'funcionario_id': linha[1],
            'maquina_id':linha[2],
            'produto':linha[3],
            'quantidade':linha[4],
            'status':linha[5]
            }
        return dicionario

    def adicionar(self, funcionario_id, maquina_id, produto, quantidade, status):
        self.get_cursor().execute("INSERT INTO ordens_producao (funcionario_id, maquina_id, produto, quantidade, status) VALUES (%s, %s, %s, %s, %s);", (funcionario_id, maquina_id, produto, quantidade, status))
        self.get_conn().commit()
        return {"mensagem": "Ordem cadastrada com sucesso!"}

    def atualizar(self, ordem_id, funcionario_id, maquina_id, produto, quantidade, status):
        self.get_cursor().execute("UPDATE ordens_producao SET funcionario_id = %s, maquina_id = %s, produto = %s, quantidade = %s, status = %s WHERE ordem_id = %s;", (funcionario_id, maquina_id, produto, quantidade, status, ordem_id))
        self.get_conn().commit()
        return {"mensagem": "Ordem atualizada com sucesso!"}

    def excluir(self, id):
        self.get_cursor().execute("DELETE FROM ordens_producao WHERE ordem_id = %s;",(id,))
        self.get_conn().commit()
        return {"mensagem": "Ordem excluída com sucesso!"}