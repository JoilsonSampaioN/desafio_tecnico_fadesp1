# Desafio Técnico FADESP — Engenharia e Análise de Dados

## Objetivo

Este projeto foi desenvolvido como parte do processo seletivo para a vaga de Analista de BI na FADESP. O objetivo principal é realizar uma análise exploratória e criar visualizações a partir dos microdados do Censo da Educação Superior 2023, respondendo às principais perguntas de negócio de forma clara e interativa.

## Estrutura do Projeto

- **/data/**: Contém os arquivos de entrada.
- **/notebooks/**: Notebook com toda a análise exploratória, gráficos e comentários.
- **/scripts/**: Scripts em Python modularizados para limpeza de dados e geração de gráficos.
- **/output/**: Pasta de saída com os gráficos salvos em PNG e o dashboard interativo em HTML.

## Como Executar

Instale as dependências:

pip install -r requirements.txt

Execute o notebook:
Abra o arquivo notebooks/01_analise_visualizacao.ipynb no VS Code ou Jupyter e execute célula por célula para ver a análise completa.

Scripts
limpeza.py
Funções para carregar, filtrar e mapear os dados de forma limpa e reaproveitável.

visualizacoes.py
Funções para criar e salvar todos os gráficos em PNG e o dashboard interativo em HTML.

Principais Gráficos
Cursos por UF (barras)

Cursos por Categoria Administrativa (barras)

Cursos por Organização Acadêmica (barras)

Heatmap: relação entre UF e Organização Acadêmica

Gráfico Interativo: distribuição por UF com Plotly

Todos os gráficos estão salvos em /output/graficos e o dashboard interativo em /output/dashboard.html.

## Como abrir o painel interativo

Para abrir o painel interativo em Streamlit:

streamlit run app.py

## geralmente leva alguns minutos para abrir tudo

