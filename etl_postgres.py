import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/fadesp_db')

df_cursos = pd.read_csv('data/MICRODADOS_CADASTRO_CURSOS_2023.CSV', sep=';', encoding='latin1', low_memory=False)
df_cursos = df_cursos[df_cursos['NO_CURSO'].notnull()]

df_cnpq = pd.read_excel('data/Relatorio_de_dados_abertos_CNPq (1º SEM 2023)(snICJ).xlsx', skiprows=5)

df_cursos.to_sql('cursos', engine, if_exists='replace', index=False)
df_cnpq.to_sql('bolsistas', engine, if_exists='replace', index=False)

print("Tabelas 'cursos' e 'bolsistas' salvas no PostgreSQL com sucesso!")
