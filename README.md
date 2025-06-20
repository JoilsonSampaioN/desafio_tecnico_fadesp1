# Desafio Técnico FADESP — Engenharia e Análise de Dados

Este projeto foi desenvolvido como parte do processo seletivo para a vaga de Analista de BI na FADESP.  
O objetivo é realizar uma análise exploratória completa relacionando dados do **Censo da Educação Superior (INEP)** com os **Bolsistas de Pesquisa do CNPq**, identificando padrões e gerando insights práticos para tomada de decisão.

---

## 📁 **Estrutura do Repositório**

- **/data/** → Contém os arquivos de entrada:
  - `MICRODADOS_CADASTRO_CURSOS_2023.CSV`
  - `MICRODADOS_ED_SUP_IES_2023.CSV`
  - `Relatorio_de_dados_abertos_CNPq (1º SEM 2023)(snICJ).xlsx`
- **/notebooks/** → Notebook com toda a análise, gráficos interativos e comentários.
- **/scripts/** → Scripts Python para carga, limpeza e organização dos dados.
- **app.py** → Aplicação interativa com Streamlit.
- **requirements.txt** → Lista de bibliotecas necessárias.

---

##  **Pré-Requisitos**
>  **Atenção:**  
##  Pré-requisitos
1. Baixe o arquivo ZIP: [Link para o download](https://nuvem.cnpq.br/index.php/s/fLrSsC9wfeL8HWZ/download)
2. Extraia o conteúdo na pasta `data/` do projeto



##  **Como Executar o Projeto**

1️ **Clone o repositório**

git clone https://github.com/SEU_USUARIO/desafio_tecnico_fadesp.git
cd desafio_tecnico_fadesp

python -m venv venv
Ative:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

 Instale as dependências

pip install -r requirements.txt
 Execute o notebook

Abra o arquivo notebooks/analise_exploratoria.ipynb e rode célula por célula.

 Ou execute a aplicação Streamlit

## geralmente leva alguns segundos para abrir tudo

streamlit run app.py
 Principais Funcionalidades
Pré-visualização de dados limpos.

Gráficos interativos (Plotly) com análise por UF, categoria administrativa e organização acadêmica.

Heatmap para identificar distribuições relevantes.

Comparação cruzada entre cursos cadastrados e número de bolsistas do CNPq.

Código robusto para lidar com colunas inconsistentes.

## ETL e Banco de Dados

Este projeto usa **PostgreSQL** via **Docker** para armazenar os dados limpos.

- O `docker-compose.yml` sobe o container do banco.
- O script `limpeza.py` trata os dados e exporta para o PostgreSQL usando `SQLAlchemy`.
- O esquema relacional está definido no `db_schema.sql` para consultas normalizadas.

**Passos rápidos:**

# Subir o banco:
docker-compose up -d

# Criar tabelas:
psql -h localhost -U user -d fadesp_db -f db_schema.sql

# Rodar ETL:
python scripts/limpeza.py


 Observações Finais
Não esqueça: Os arquivos originais devem estar em /data/.

O projeto foi estruturado para ser modular, documentado e fácil de entender.

Para executar em outro computador, basta clonar o repositório, instalar as dependências e colocar os arquivos na pasta certa.
