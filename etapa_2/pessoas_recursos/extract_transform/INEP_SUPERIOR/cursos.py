import pandas as pd
from glob import glob

dir_dados = r"/Volumes/SEAGATE_EHD/sidtec_pb/censo_superior"

lista = glob(f"{dir_dados}/*/dados/*.CSV")

lista = [i for i in lista if "CURSOS" in i]

lista = sorted(lista)

colunas_extended = ["NU_ANO_CENSO", "NO_REGIAO", "CO_REGIAO", "SG_UF", "CO_UF", 
           "NO_MUNICIPIO", "CO_MUNICIPIO", "TP_ORGANIZACAO_ACADEMICA",
           "TP_CATEGORIA_ADMINISTRATIVA", "TP_REDE", "CO_IES", "NO_CINE_ROTULO",
           "CO_CINE_ROTULO", "CO_CINE_AREA_GERAL", "NO_CINE_AREA_GERAL", "TP_GRAU_ACADEMICO",
           "TP_MODALIDADE_ENSINO", "TP_NIVEL_ACADEMICO", "QT_VG_TOTAL", "QT_VG_TOTAL_DIURNO",
           "QT_VG_TOTAL_NOTURNO", "QT_VG_TOTAL_EAD", "QT_INSCRITO_TOTAL", "QT_INSCRITO_TOTAL_DIURNO",
           "QT_INSCRITO_TOTAL_NOTURNO", "QT_INSCRITO_TOTAL_EAD", "QT_ING", "QT_ING_FEM", "QT_ING_MASC",
           "QT_ING_DIURNO", "QT_ING_NOTURNO", "QT_ING_ENEM", "QT_ING_0_17", "QT_ING_18_24", "QT_ING_25_29",
           "QT_ING_30_34", "QT_ING_35_39", "QT_ING_40_49", "QT_ING_50_59", "QT_ING_60_MAIS", "QT_ING_BRANCA",
           "QT_ING_PRETA", "QT_ING_PARDA", "QT_ING_AMARELA", "QT_ING_INDIGENA", "QT_ING_CORND",
           "QT_MAT", "QT_MAT_FEM", "QT_MAT_MASC", "QT_MAT_DIURNO", "QT_MAT_NOTURNO", "QT_MAT_0_17",
           "QT_MAT_18_24", "QT_MAT_25_29", "QT_MAT_30_34", "QT_MAT_35_39", "QT_MAT_40_49",
           "QT_MAT_50_59", "QT_MAT_60_MAIS", "QT_MAT_BRANCA", "QT_MAT_PRETA", "QT_MAT_PARDA",
           "QT_MAT_AMARELA", "QT_MAT_INDIGENA", "QT_MAT_CORND", "QT_CONC", "QT_CONC_FEM", "QT_CONC_MASC",
           "QT_CONC_DIURNO", "QT_CONC_NOTURNO", "QT_CONC_ENEM", "QT_CONC_0_17", "QT_CONC_18_24", "QT_CONC_25_29",
           "QT_CONC_30_34", "QT_CONC_35_39", "QT_CONC_40_49", "QT_CONC_50_59", "QT_CONC_60_MAIS", "QT_CONC_BRANCA",
           "QT_CONC_PRETA", "QT_CONC_PARDA", "QT_CONC_AMARELA", "QT_CONC_INDIGENA", "QT_CONC_CORND",
           "QT_ING_NACBRAS", "QT_ING_NACESTRANG", "QT_MAT_NACBRAS", "QT_MAT_NACESTRANG", "QT_CONC_NACBRAS",
           "QT_CONC_NACESTRANG", "QT_ALUNO_DEFICIENTE", "QT_ING_DEFICIENTE", "QT_MAT_DEFICIENTE", 
           "QT_CONC_DEFICIENTE", "QT_ING_FINANC", "QT_ING_FINANC_REEMB", "QT_ING_FINANC_NREEMB", 
           "QT_MAT_FINANC", "QT_MAT_FINANC_REEMB", "QT_MAT_FINANC_NREEMB", "QT_CONC_FINANC", "QT_CONC_FINANC_REEMB",
           "QT_MAT_FINANC_NREEMB", "QT_ING_RESERVA_VAGA", "QT_MAT_RESERVA_VAGA", "QT_CONC_RESERVA_VAGA", 
           "QT_SIT_TRANCADA", "QT_SIT_DESVINCULADO", "QT_SIT_TRANSFERIDO", "QT_SIT_FALECIDO", 
           "QT_ING_PROCESCPUBLICA", "QT_ING_PROCESCPRIVADA", "QT_ING_PROCNAOINFORMADA", "QT_MAT_PROCESCPUBLICA", 
           "QT_MAT_PROCESCPRIVADA", "QT_MAC_PROCNAOINFORMADA", "QT_CONC_PROCESCPUBLICA", "QT_CONC_PROCESCPRIVADA", 
           "QT_CONC_PROCNAOINFORMADA", "QT_APOIO_SOCIAL", "QT_ING_APOIO_SOCIAL", "QT_MAT_APOIO_SOCIAL"
           "QT_CONC_APOIO_SOCIAL"
           ]

mapa_org_acad = {1: "Universidade", 2: "Centro Universitário", 3: "Faculdade",
                 4: "Instituto Federal de Educação, Ciência e Tecnologia",
                 5: "Centro Federal de Educação Tecnológica"}

mapa_cat_adm = {1: "Pública Federal", 2: "Pública Estadual", 3: "Pública Municipal", 4: "Privada com fins lucrativos", 
                5: "Privada sem fins lucrativos", 6: "Privada - Particular em sentido estrito", 
                7: "Especial", 8: "Privada comunitária", 9: "Privada confessional"}


def read(base):
    file = pd.read_csv(base, sep = ";", encoding = "latin", usecols = colunas_extended)
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
       'tec_adm_especializacao', 'tec_adm_mestrado', 'tec_adm_doutorado', 'QT_DOC_TOTAL', 'QT_DOC_EXE', 'QT_DOC_EX_ESP',
       'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT']]

 
    
    file.columns = ["ano", "regiao_ies", "sigla_uf", "municipio", "capital", "nome_ies", "sigla_ies", "org_academica", "cat_administrativa", "total_tec_adm", "tec_adm_especializacao", "tec_adm_mestrado", "tec_adm_doutorado", "total_docentes", "docentes_exercicio", "docentes_esp_exercicio", "docentes_mest_exercicio", "docentes_dout_exercicio"]
    

    return file


lista_df = []

for arquivos in lista:
    lista_df.append(read(arquivos))

final_data = pd.concat(lista_df, ignore_index= True)

final_data.to_excel("trabalhadores_ies.xlsx", index = False)
