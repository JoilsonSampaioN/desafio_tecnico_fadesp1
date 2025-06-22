import pandas as pd
from sqlalchemy import create_engine, text, types

# Configuração do banco PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://user:password@localhost:5440/fadesp_db"
)
print("Conectado ao PostgreSQL com sucesso")

# Caminhos dos arquivos
file_cursos = "data/MICRODADOS_CADASTRO_CURSOS_2023.CSV"
file_ies = "data/MICRODADOS_ED_SUP_IES_2023.CSV"
file_cnpq = "data/Relatorio_de_dados_abertos_CNPq (1º SEM 2023)(snICJ).xlsx"

# Tamanho do chunk
chunk_size = 10_000

# Lê apenas cabeçalho do CSV para pegar as colunas
columns = pd.read_csv(file_cursos, sep=';', encoding='latin1', nrows=0).columns

# Dropa tabela se existir e cria nova 100% TEXT
with engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS cursos;"))
    cols_sql = ", ".join([f'"{col}" TEXT' for col in columns])
    conn.execute(text(f'CREATE TABLE cursos ({cols_sql});'))
print("Tabela CURSOS criada forçando tudo como TEXT.")

# Insere em lotes
print(f"Iniciando carga de CURSOS em lotes de {chunk_size} linhas...")
chunks = pd.read_csv(file_cursos, sep=';', encoding='latin1', low_memory=False, chunksize=chunk_size)
for i, chunk in enumerate(chunks):
    chunk.to_sql(
        "cursos",
        con=engine,
        index=False,
        if_exists='append'
    )
    print(f"Lote {i+1} carregado.")
print("Todos os lotes de CURSOS foram carregados com sucesso\n")

# Carrega IES de uma vez
print(" Carregando tabela IES")
df_ies = pd.read_csv(file_ies, sep=';', encoding='latin1', low_memory=False)
df_ies.to_sql(
    "ies",
    con=engine,
    index=False,
    if_exists='replace',
    dtype={col: types.Text() for col in df_ies.columns}
)

df_cnpq = pd.read_excel(file_cnpq, skiprows=5)
df_cnpq.to_sql("bolsistas", con=engine, index=False, if_exists="replace")
print("Tabela BOLSISTAS criada com sucesso.")

print("Tabela IES carregada com sucesso\n")

print("ETL COMPLETO")
