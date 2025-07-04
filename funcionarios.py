
class Funcionarios():

    def __init__(self, funcionario_id, nome, setor):
        self.__funcionario_id = funcionario_id
        self.__nome = nome
        self.__setor = setor

    def get_funcionario_id(self):
        return self.__funcionario_id

    def set_funcionario_id(self, funcionario_id):
        self.__funcionario_id = funcionario_id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_setor(self):
        return self.__setor

    def set_setor(self, setor):
        self.__setor = setor