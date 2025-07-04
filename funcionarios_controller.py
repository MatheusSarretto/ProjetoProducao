from conexao import Conexao

class FuncionariosController():

    def __init__(self):
        db = Conexao()
        self.conn = db.get_conexao()
        self.cursor = db.get_cursor()

    def get_conn(self):
        return self.conn

    def get_cursor(self):
        return self.cursor

    def listar(self):
        self.get_cursor().execute("SELECT * FROM funcionarios;")
        linhas = self.get_cursor().fetchall()
        lista = []
        for linha in linhas:
            dicionario = {
                'id':linha[0],
                'nome':linha[1],
                'setor':linha[2]
            }
            lista.append(dicionario)
        return lista

    def buscar(self, id):
        self.get_cursor().execute("SELECT * FROM funcionarios WHERE funcionario_id = %s;",(id,))
        linha = self.get_cursor().fetchone()
        dicionario = {
            'id': linha[0],
            'nome': linha[1],
            'setor': linha[2]
        }
        return dicionario

    def adicionar(self, nome, setor):
        self.get_cursor().execute("INSERT INTO funcionarios (nome, setor) VALUES(%s, %s);",(nome,setor))
        self.get_conn().commit()
        return {"mensagem": "Funcionário cadastrado com sucesso!"}

    def atualizar(self, id, nome, setor):
        self.get_cursor().execute("UPDATE funcionarios SET nome = %s, setor = %s WHERE funcionario_id = %s;", (nome, setor, id))
        self.get_conn().commit()
        return {"mensagem": "Funcionário atualizado com sucesso!"}

    def excluir(self, id):
        self.get_cursor().execute("DELETE FROM funcionarios WHERE funcionario_id = %s;", (id,))
        self.get_conn().commit()
        return {"mensagem": "Funcionário excluído com sucesso!"}