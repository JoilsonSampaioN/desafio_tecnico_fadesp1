# Desafio Técnico FADESP

Este repositório contém uma solução completa para o desafio técnico proposto, envolvendo engenharia de dados, análise exploratória, visualização e modelagem preditiva com dados de instituições de ensino superior e bolsas científicas no Brasil.

---

## Estrutura do Projeto

- **scripts/**  
  Scripts de ETL para extração, transformação e carregamento dos dados no banco PostgreSQL.

- **notebooks/**  
  Notebooks organizados para exploração de dados, análises estatísticas, visualizações e experimentos de machine learning.

- **data/**  
  Diretório onde os arquivos CSV devem ser colocados. Para execução local, baixe os dados oficiais e extraia na pasta `data/`.

- **docker-compose.yml**  
  Define o ambiente do banco PostgreSQL, volumes e rede para garantir persistência e isolamento.

---

## Pré-Requisitos

- Docker e Docker Compose instalados
- Python 3.10+
- Ambiente virtual configurado (opcional, mas recomendado)

---

## Como executar

1. **Clone o repositório**

   git clone https://github.com/SEU_USUARIO/desafio_tecnico_fadesp.git
   cd desafio_tecnico_fadesp

Coloque os arquivos CSV

Baixe e extraia os arquivos:

MICRODADOS_CADASTRO_CURSOS_2023.CSV

MICRODADOS_ED_SUP_IES_2023.CSV

Salve na pasta data/.

Suba o banco de dados com Docker

docker compose up -d
Isso cria um container PostgreSQL, pronto para receber os dados.

Crie e ative o ambiente virtual

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
Instale as dependências

pip install -r requirements.txt
Execute o ETL

python scripts/etl_postgres.py
Isso carregará os dados em lotes no banco PostgreSQL.

Rode os notebooks

Abra os notebooks na pasta notebooks/ para explorar as análises, gráficos, mapas e modelo preditivo.

Principais Funcionalidades
Extração e carga de grandes arquivos CSV em banco relacional.

Limpeza, normalização e padronização de informações.

Análise exploratória com gráficos interativos.

Heatmaps, distribuições e mapas geográficos.

Regressão linear para investigar relações entre cursos e bolsas.

Ambiente Docker para fácil replicação.

Desafios e Recomendações
A solução lida com dados extensos, sendo necessária divisão em lotes para evitar sobrecarga de memória.

Algumas colunas possuem inconsistências de tipos e valores ausentes; tratamento foi realizado no ETL.

Recomenda-se evoluir o modelo preditivo com mais variáveis institucionais para projeções mais precisas.

Investir em padronização de bases públicas pode facilitar futuras análises.

Apresentação
Este repositório inclui uma apresentação em PDF resumindo a abordagem metodológica, os principais desafios, descobertas e recomendações para melhorar a produção científica com base nos dados analisados. O repositório se encontra dentro da pasta docs.

