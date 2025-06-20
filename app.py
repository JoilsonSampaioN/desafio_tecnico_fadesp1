"""
Aplicação principal do desafio técnico FADESP.
Este script inicializa o Streamlit, carrega os dados,
gera os gráficos interativos e permite comparação
entre cursos e bolsas de pesquisa.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import sys

sys.path.append('scripts')

from scripts.limpeza import carregar_e_filtrar

st.set_page_config(layout="wide")

st.title("Análise do Censo da Educação Superior 2023")

base_path = 'data/'
df_cursos, df_ies = carregar_e_filtrar(base_path)

cols_preview = [
    'NU_ANO_CENSO', 'SG_UF', 'NO_CURSO',
    'CATEGORIA_ADMINISTRATIVA', 'ORGANIZACAO_ACADEMICA'
]
df_preview = df_cursos[df_cursos['SG_UF'].notnull()].copy()

st.subheader("Prévia dos Dados de Cursos")
st.dataframe(df_preview.head(20))

st.subheader("Cursos por UF")
uf_counts = df_cursos['SG_UF'].value_counts().reset_index()
uf_counts.columns = ['UF', 'Quantidade']
fig_uf = px.bar(
    uf_counts, 
    x='UF', 
    y='Quantidade', 
    text_auto='.3s', 
    color='UF',
    title="Cursos por UF",
    width=1000,
    height=500
)
st.plotly_chart(fig_uf)

st.subheader("Cursos por Categoria Administrativa")
cat_counts = df_cursos['CATEGORIA_ADMINISTRATIVA'].value_counts().reset_index()
cat_counts.columns = ['Categoria', 'Quantidade']
fig_cat = px.bar(
    cat_counts,
    x='Categoria',
    y='Quantidade',
    text_auto=True,
    color='Categoria',
    title="Cursos por Categoria Administrativa",
    width=800,
    height=500
)
st.plotly_chart(fig_cat)

st.subheader("Cursos por Organização Acadêmica")
org_counts = df_cursos['ORGANIZACAO_ACADEMICA'].value_counts().reset_index()
org_counts.columns = ['Organização', 'Quantidade']
fig_org = px.bar(
    org_counts,
    x='Organização',
    y='Quantidade',
    text_auto=True,
    color='Organização',
    title="Cursos por Organização Acadêmica",
    width=800,
    height=500
)
st.plotly_chart(fig_org)

st.subheader("Heatmap: Cursos por UF vs Organização Acadêmica")
heatmap_data = df_cursos.pivot_table(
    index='SG_UF',
    columns='ORGANIZACAO_ACADEMICA',
    values='NO_CURSO',
    aggfunc='count',
    fill_value=0
).sort_index()

fig_heatmap = px.imshow(
    heatmap_data,
    text_auto=True,
    aspect="auto",
    color_continuous_scale='Blues',
    labels=dict(color="Cursos"),
    width=1000,
    height=600
)
st.plotly_chart(fig_heatmap)

st.subheader("Comparação de Cursos e Bolsistas CNPq por UF")
file_cnpq = base_path + 'Relatorio_de_dados_abertos_CNPq (1º SEM 2023)(snICJ).xlsx'
df_cnpq = pd.read_excel(file_cnpq, skiprows=5)
df_cnpq_grouped = df_cnpq.groupby('Sigla UF Destino').size().reset_index(name='Bolsistas')

df_merged = pd.merge(
    uf_counts,
    df_cnpq_grouped,
    left_on='UF',
    right_on='Sigla UF Destino',
    how='inner'
)

df_merged = df_merged[['UF', 'Quantidade', 'Bolsistas']].sort_values(by='Quantidade', ascending=False)

fig_relation = px.bar(
    df_merged.melt(id_vars='UF', value_vars=['Quantidade', 'Bolsistas']),
    x='UF',
    y='value',
    color='variable',
    barmode='group',
    text_auto=True,
    labels={'value': 'Quantidade', 'variable': 'Indicador'},
    title="Comparação de Cursos e Bolsistas CNPq por UF",
    width=1000,
    height=600
)
st.plotly_chart(fig_relation)
