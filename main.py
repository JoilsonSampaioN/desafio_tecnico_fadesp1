from scripts.limpeza import carregar_e_filtrar
from scripts.visualizacoes import plotar_graficos

BASE_PATH = 'data/'

print("Carregando e limpando dados...")
df_cursos, df_ies = carregar_e_filtrar(BASE_PATH)
print("Limpeza concluída.")

print("Gerando gráficos e dashboard...")
plotar_graficos(df_cursos)
print("Gráficos salvos em /output.")