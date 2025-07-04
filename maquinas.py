
class Maquinas():

    def __init__(self, maquina_id, descricao, status):
        self.__maquina_id = maquina_id
        self.__descricao = descricao
        self.__status = status

    def get_maquina_id(self):
        return self.__maquina_id

    def set_maquina_id(self, maquina_id):
        set.__maquina_id = maquina_id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        set.__descricao = descricao

    def get_status(self):
        return self.__status

    def set_status(self, status):
        set.__status = status