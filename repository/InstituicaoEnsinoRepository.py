from psycopg2 import OperationalError
from helpers.logger import logger
from helpers.database import get_connection
from models.instituicaoensino import InstituicaoEnsino


class InstituicaoEnsinoRepository():

    def row_to_instituicao(self, row):
        return InstituicaoEnsino(
            no_entidade=row[0],
            co_entidade=row[1],
            no_uf=row[2],
            sg_uf=row[3],
            co_uf=row[4],
            no_municipio=row[5],
            co_municipio=row[6],
            nu_ano_censo=row[7],
            qt_mat_bas=row[8],
            qt_mat_inf=row[9],
            qt_mat_fund=row[10],
            qt_mat_med=row[11],
            qt_mat_prof=row[12],
            qt_mat_eja=row[13],
            qt_mat_esp=row[14],
        )

    def get_all_Instituicoes(self, per_page, page_current):



        connection = get_connection()

        
        try:


            logger.info("Recuperando a conexão com o Banco de dados")


            cursor = connection.cursor()


            cursor.execute("""
                SELECT no_entidade, co_entidade, no_uf, sg_uf, co_uf, no_municipio, co_municipio, nu_ano_censo, qt_mat_bas, qt_mat_inf,
                    qt_mat_fund, qt_mat_med, qt_mat_prof, qt_mat_eja, qt_mat_esp
                FROM instituicoes
                LIMIT %s OFFSET %s
            """, (per_page, (page_current - 1) * per_page))
            rows = cursor.fetchall()



# instituicao trasnformacoes de objetos
            instituicoes = [
                self.row_to_instituicao(row)
                for row in rows
            ]


        except OperationalError:
            logger.error("Erro no processamento dos dados no Banco de Dados")
            connection.rollback()
            raise


        finally:
            
            cursor.close()

            
        return instituicoes

    def getInstituicao(self, id):



        connection = get_connection()


        try:
            cursor = connection.cursor()

            
            cursor.execute("""
                SELECT no_entidade, co_entidade, no_uf, sg_uf, co_uf, no_municipio, co_municipio, nu_ano_censo, qt_mat_bas, qt_mat_inf,
                    qt_mat_fund, qt_mat_med, qt_mat_prof, qt_mat_eja, qt_mat_esp
                FROM instituicoes
                WHERE co_entidade = %s
            """, (id,))
            row = cursor.fetchone()




            if row is None:
                return None

            instituicao = self.row_to_instituicao(row)




        except OperationalError:
            connection.rollback()
            raise


        finally:
            
            cursor.close()

        return instituicao