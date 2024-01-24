import pandas as pd
from glob import glob

dir_dados = r"/Volumes/SEAGATE_EHD/sidtec_pb/censo_superior"

lista = glob(f"{dir_dados}/*/dados/*.CSV")

lista = [i for i in lista if "CURSOS" in i]

lista = sorted(lista)

colunas = ['NU_ANO_CENSO', 'NO_REGIAO_IES', 'SG_UF_IES', 'NO_MUNICIPIO_IES', 
            'IN_CAPITAL_IES', 'TP_ORGANIZACAO_ACADEMICA', 'TP_CATEGORIA_ADMINISTRATIVA', 
            'NO_IES', 'SG_IES', 'QT_TEC_TOTAL', 'QT_TEC_ESPECIALIZACAO_FEM', 
            'QT_TEC_ESPECIALIZACAO_MASC','QT_TEC_MESTRADO_FEM', 'QT_TEC_MESTRADO_MASC', 
            'QT_TEC_DOUTORADO_FEM', 'QT_TEC_DOUTORADO_MASC', 'QT_DOC_TOTAL','QT_DOC_EXE', 
            'QT_DOC_EX_ESP', 'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT']

mapa_org_acad = {1: "Universidade", 2: "Centro Universitário", 3: "Faculdade",
                 4: "Instituto Federal de Educação, Ciência e Tecnologia",
                 5: "Centro Federal de Educação Tecnológica"}

mapa_cat_adm = {1: "Pública Federal", 
                2: "Pública Estadual", 
                3: "Pública Municipal", 
                4: "Privada com fins lucrativos", 
                5: "Privada sem fins lucrativos", 
                6: "Privada - Particular em sentido estrito", 
                7: "Especial", 
                8: "Privada comunitária", 
                9: "Privada confessional"}


def read(base):
    file = pd.read_csv(base, sep = ";", encoding = "latin", usecols = colunas)
    file["ORGANIZACAO_ACADEMICA"] = file["TP_ORGANIZACAO_ACADEMICA"].map(mapa_org_acad)
    file["CATEGORIA_ADMINISTRATIVA"] = file["TP_CATEGORIA_ADMINISTRATIVA"].map(mapa_cat_adm)

    del file["TP_ORGANIZACAO_ACADEMICA"]
    del file["TP_CATEGORIA_ADMINISTRATIVA"]

    file = file.query("CATEGORIA_ADMINISTRATIVA == 'Pública Federal' or CATEGORIA_ADMINISTRATIVA == 'Pública Estadual' \
                      or CATEGORIA_ADMINISTRATIVA == 'Pública Municipal' or \
                      CATEGORIA_ADMINISTRATIVA == 'Privada com fins lucrativos'")
    
    file["tec_adm_especializacao"] = file["QT_TEC_ESPECIALIZACAO_FEM"] + file["QT_TEC_ESPECIALIZACAO_MASC"]
    del file["QT_TEC_ESPECIALIZACAO_FEM"]
    del file["QT_TEC_ESPECIALIZACAO_MASC"]

    file["tec_adm_mestrado"] = file["QT_TEC_MESTRADO_FEM"] + file["QT_TEC_MESTRADO_MASC"]
    del file["QT_TEC_MESTRADO_FEM"]
    del file["QT_TEC_MESTRADO_MASC"]

    file["tec_adm_doutorado"] = file["QT_TEC_DOUTORADO_FEM"] + file["QT_TEC_DOUTORADO_MASC"]
    del file["QT_TEC_DOUTORADO_FEM"]
    del file["QT_TEC_DOUTORADO_MASC"]


    file = file[['NU_ANO_CENSO', 'NO_REGIAO_IES', 'SG_UF_IES', 'NO_MUNICIPIO_IES',
       'IN_CAPITAL_IES', 'NO_IES', 'SG_IES', 'ORGANIZACAO_ACADEMICA',
       'CATEGORIA_ADMINISTRATIVA', 'QT_TEC_TOTAL',
       'tec_adm_especializacao', 'tec_adm_mestrado', 'tec_adm_doutorado',
       'QT_DOC_TOTAL', 'QT_DOC_EXE', 'QT_DOC_EX_ESP',
       'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT']]

 
    
    file.columns = ["ano", "regiao_ies", "sigla_uf", "municipio", "capital", 
                    "nome_ies", "sigla_ies", "org_academica", "cat_administrativa",
                    "total_tec_adm", "tec_adm_especializacao", "tec_adm_mestrado",
                    "tec_adm_doutorado", "total_docentes", "docentes_exercicio",
                    "docentes_esp_exercicio", "docentes_mest_exercicio",
                    "docentes_dout_exercicio"]
    
    return file


lista_df = []

for arquivos in lista:
    lista_df.append(read(arquivos))

final_data = pd.concat(lista_df, ignore_index= True)

final_data.to_excel("trabalhadores_ies.xlsx", index = False)
