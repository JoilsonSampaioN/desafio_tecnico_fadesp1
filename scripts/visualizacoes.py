import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Pasta para salvar gráficos
OUTPUT_DIR = 'output/graficos/'

# Cria se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plotar_graficos(df_cursos):
    """
    Gera e salva gráficos principais: barras, heatmap, interativo.
    """

    # 1️⃣ Cursos por UF
    plt.figure(figsize=(15, 6))
    sns.countplot(
        data=df_cursos,
        x='SG_UF',
        order=df_cursos['SG_UF'].value_counts().index,
        palette='viridis',
        hue=None
    )
    plt.title('Quantidade de Cursos por UF')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'cursos_por_uf.png')
    plt.show()

    # 2️⃣ Categoria Administrativa
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=df_cursos,
        x='CATEGORIA_ADMIN',
        palette='pastel',
        hue=None
    )
    plt.title('Cursos por Categoria Administrativa')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'categoria_admin.png')
    plt.show()

    # 3️⃣ Organização Acadêmica
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=df_cursos,
        x='ORGANIZACAO_ACADEMICA',
        palette='Set2',
        hue=None
    )
    plt.title('Cursos por Organização Acadêmica')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'organizacao_academica.png')
    plt.show()

    # 4️⃣ Heatmap
    pivot = df_cursos.pivot_table(
        index='SG_UF',
        columns='ORGANIZACAO_ACADEMICA',
        values='NO_CURSO',
        aggfunc='count',
        fill_value=0
    )
    plt.figure(figsize=(15, 10))
    sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Heatmap: Cursos por UF vs Organização Acadêmica')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + 'heatmap_uf_org_academica.png')
    plt.show()

    # 5️⃣ Plotly Interativo — salva em HTML
    uf_counts = df_cursos['SG_UF'].value_counts().reset_index()
    uf_counts.columns = ['UF', 'Quantidade']

    fig = px.bar(
        uf_counts,
        x='UF',
        y='Quantidade',
        labels={'UF': 'UF', 'Quantidade': 'Quantidade de Cursos'},
        title='Quantidade de Cursos por UF (Interativo)',
        text_auto=True,
        color='UF'
    )
    fig.write_html('output/dashboard.html')
    fig.show()
