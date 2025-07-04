
class Ordens_producao():

    def __init__(self, ordem_id, funcionario_id, maquina_id, produto, quantidade, status):
        self.__ordem_id = ordem_id
        self.__funcionario_id = funcionario_id
        self.__maquina_id = maquina_id
        self.__produto = produto
        self.__quantidade = quantidade
        self.__status = status

    def get_ordem_id(self):
        return self.__ordem_id
    
    def set_ordem_id(self, ordem_id):
        self.__ordem_id = ordem_id

    def get_funcionario_id(self):
        return self.__funcionario_id

    def set_funcionario_id(self, funcionario_id):
        self.__funcionario_id = funcionario_id

    def get_maquina_id(self):
        return self.__maquina_id

    def set_maquina_id(self, maquina_id):
        self.__maquina_id = maquina_id

    def get_produto(self):
        return self.__produto

    def set_produto(self, produto):
        self.__produto = produto

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status