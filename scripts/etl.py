import pandas as pd
import sqlite3
import os

def executar_etl(base_path='data/'):

    file_cursos = os.path.join(base_path, 'MICRODADOS_CADASTRO_CURSOS_2023.CSV')
    file_ies = os.path.join(base_path, 'MICRODADOS_ED_SUP_IES_2023.CSV')
    file_cnpq = os.path.join(base_path, 'Relatorio_de_dados_abertos_CNPq.xlsx')

    df_cursos = pd.read_csv(file_cursos, sep=';', encoding='latin1', low_memory=False)
    df_ies = pd.read_csv(file_ies, sep=';', encoding='latin1', low_memory=False)
    df_cnpq = pd.read_excel(file_cnpq, skiprows=5)

    df_cursos = df_cursos[df_cursos['SG_UF'].notnull()].copy()
    df_ies = df_ies[df_ies['SG_UF'].notnull()].copy()
    df_cnpq = df_cnpq[df_cnpq['Sigla UF Destino'].notnull()].copy()

    if 'NO_IES' in df_ies.columns:
        df_ies['NO_IES'] = df_ies['NO_IES'].str.upper().str.strip()

    conn = sqlite3.connect('database.db')
    df_cursos.to_sql('cursos', conn, if_exists='replace', index=False)
    df_ies.to_sql('instituicoes', conn, if_exists='replace', index=False)
    df_cnpq.to_sql('bolsistas', conn, if_exists='replace', index=False)
    conn.close()

    print("ETL executado com sucesso! Dados salvos em database.db")

if __name__ == '__main__':
    executar_etl()
