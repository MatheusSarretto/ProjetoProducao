import mysql.connector as db

class Conexao():
    def __init__(self):
        self.conn = db.connect (
            host='localhost',
            user='root',
            password='senai',
            database='db_producao'
        )

    def get_conexao(self):
        return self.conn

    def get_cursor(self):
        return self.get_conexao().cursor()

    def close(self):
        if self.conn.is_connected():
            self.conn.close()