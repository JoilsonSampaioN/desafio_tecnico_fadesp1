import pandas as pd

def carregar_e_filtrar(base_path):
    file_cursos = base_path + 'MICRODADOS_CADASTRO_CURSOS_2023.CSV'
    file_ies = base_path + 'MICRODADOS_ED_SUP_IES_2023.CSV'

    df_cursos = pd.read_csv(file_cursos, sep=';', encoding='latin1', low_memory=False)
    df_ies = pd.read_csv(file_ies, sep=';', encoding='latin1', low_memory=False)


    df_cursos = df_cursos[df_cursos['NO_CURSO'].notnull()]

    cat_map = {
        1: 'Pública Federal',
        2: 'Pública Estadual',
        3: 'Pública Municipal',
        4: 'Privada',
        5: 'Privada Comunitária',
        6: 'Privada Confessional',
        7: 'Privada Lucrativa'
    }
    df_cursos['CATEGORIA_ADMINISTRATIVA'] = df_cursos['TP_CATEGORIA_ADMINISTRATIVA'].map(cat_map)

    org_map = {
        1: 'Universidade',
        2: 'Centro Universitário',
        3: 'Faculdade',
        4: 'Instituto Federal',
        5: 'Centro de Educação Tecnológica'
    }
    df_cursos['ORGANIZACAO_ACADEMICA'] = df_cursos['TP_ORGANIZACAO_ACADEMICA'].map(org_map)

    return df_cursos, df_ies
