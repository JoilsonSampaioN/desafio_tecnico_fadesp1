import pandas as pd

def carregar_e_filtrar(base_path):
   

    file_cursos = base_path + 'MICRODADOS_CADASTRO_CURSOS_2023.CSV'
    file_ies = base_path + 'MICRODADOS_ED_SUP_IES_2023.CSV'

    df_cursos = pd.read_csv(file_cursos, sep=';', encoding='latin1', low_memory=False)
    df_ies = pd.read_csv(file_ies, sep=';', encoding='latin1', low_memory=False)

    df_cursos = df_cursos[df_cursos['NO_CURSO'].notnull()]

    return df_cursos, df_ies

from sqlalchemy import create_engine

def salvar_no_banco(df_cursos, df_ies):
    engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/fadesp_db")

    df_cursos.to_sql('cursos', con=engine, if_exists='replace', index=False)
    df_ies.to_sql('instituicoes', con=engine, if_exists='replace', index=False)

    print("Dados salvos no banco PostgreSQL com sucesso!")


if __name__ == "__main__":
    base_path = 'data/'
    df_cursos, df_ies = carregar_e_filtrar(base_path)
    salvar_no_banco(df_cursos, df_ies)
