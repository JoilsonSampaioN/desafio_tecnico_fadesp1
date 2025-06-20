import pandas as pd

def carregar_e_filtrar(base_path):
    """
    Carrega os microdados de cursos e instituições do Censo da Educação Superior
    a partir dos arquivos CSV na pasta indicada. Remove registros inválidos.

    Parâmetros:
    ----------
    base_path : str
        Caminho para a pasta onde estão os arquivos CSV.

    Retorno:
    -------
    tuple of DataFrames:
        df_cursos, df_ies
    """

    file_cursos = base_path + 'MICRODADOS_CADASTRO_CURSOS_2023.CSV'
    file_ies = base_path + 'MICRODADOS_ED_SUP_IES_2023.CSV'

    df_cursos = pd.read_csv(file_cursos, sep=';', encoding='latin1', low_memory=False)
    df_ies = pd.read_csv(file_ies, sep=';', encoding='latin1', low_memory=False)

    df_cursos = df_cursos[df_cursos['NO_CURSO'].notnull()]

    return df_cursos, df_ies

from sqlalchemy import create_engine

def salvar_no_banco(df_cursos, df_ies):
    engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/fadesp_db")

    # Exemplo: salva cursos e ies no banco
    df_cursos.to_sql('cursos', con=engine, if_exists='replace', index=False)
    df_ies.to_sql('instituicoes', con=engine, if_exists='replace', index=False)

    print("Dados salvos no banco PostgreSQL com sucesso!")

# Se quiser rodar direto:
if __name__ == "__main__":
    base_path = 'data/'
    df_cursos, df_ies = carregar_e_filtrar(base_path)
    salvar_no_banco(df_cursos, df_ies)
