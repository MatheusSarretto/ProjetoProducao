from conexao import Conexao

class MaquinasController():

    def __init__(self):
        db = Conexao()
        self.conn = db.get_conexao()
        self.cursor = db.get_cursor()

    def get_conn(self):
        return self.conn

    def get_cursor(self):
        return self. cursor

    def listar(self):
        self.get_cursor().execute("SELECT * FROM maquinas;")
        linhas = self.get_cursor().fetchall()
        lista = []
        for linha in linhas:
            dicionario = {
                'id':linha[0],
                'descricao':linha[1],
                'status':linha[2]
            }
            lista.append(dicionario)
        return lista

    def buscar(self, id):
        self.get_cursor().execute("SELECT * FROM maquinas WHERE maquina_id = %s;",(id,))
        linha = self.get_cursor().fetchone()
        dicionario = {
            'id': linha[0],
            'descricao': linha[1],
            'status': linha[2]
        }
        return dicionario

    def adicionar(self, descricao, status):
        self.get_cursor().execute("INSERT INTO maquinas (descricao, status) VALUES (%s, %s);", (descricao, status))
        self.get_conn().commit()
        return {"mensagem": "Máquina cadastrada com sucesso!"}

    def atualizar(self, id, descricao, status):
        self.get_cursor().execute("UPDATE maquinas SET descricao = %s, status = %s WHERE maquina_id = %s;", (descricao, status, id))
        self.get_conn().commit()
        return {"mensagem": "Máquina atualizada com sucesso!"}

    def excluir(self, id):
        self.get_cursor().execute("DELETE FROM maquinas WHERE maquina_id = %s;", (id,))
        self.get_conn().commit()
        return {"mensagem": "Máquina excluída com sucesso!"}