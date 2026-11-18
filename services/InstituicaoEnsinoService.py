
from helpers.database import get_connection
from repository.InstituicaoEnsinoRepository import InstituicaoEnsinoRepository
from models.instituicaoensino import InstituicaoEnsino


class InstituicaoEnsinoService():
    def __init__(self):


        self.instituicaoEnsinoRepository = InstituicaoEnsinoRepository()





    def get_all(self, per_page, page_current):

        return self.instituicaoEnsinoRepository.get_all_Instituicoes(per_page, page_current)






    def get_by_id(self, id):

        return self.instituicaoEnsinoRepository.getInstituicao(id)