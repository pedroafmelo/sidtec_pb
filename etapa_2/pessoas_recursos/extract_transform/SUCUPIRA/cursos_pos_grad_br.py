import pandas as pd
from glob import glob
import os

pd.set_option("display.max_columns", 100)

dir_dados = r"/Volumes/SEAGATE_EHD/sidtec_pb/censo_superior/sucupira/cursos_pos"

os.chdir(dir_dados )


lista = glob(f"{os.getcwd()}/*.csv")

lista = sorted(lista)

colunas = ["AN_BASE", "NM_GRANDE_AREA_CONHECIMENTO", "NM_REGIAO", "SG_UF_PROGRAMA",
           "CS_STATUS_JURIDICO", "CD_CONCEITO_CURSO", "NM_GRAU_CURSO"]

lista_outras = ['CIÊNCIAS SOCIAIS APLICADAS', 'LINGÜÍSTICA, LETRAS E ARTES', 'CIÊNCIAS HUMANAS', 'Grande Area Não Informada']

lista_cties = ['CIÊNCIAS AGRÁRIAS', 'CIÊNCIAS DA SAÚDE',
        'ENGENHARIAS', 'CIÊNCIAS EXATAS E DA TERRA',
       'CIÊNCIAS BIOLÓGICAS', 'MULTIDISCIPLINAR']

cti_dict = {}
def read(base):
    file = pd.read_csv(base, sep = ";", encoding = "latin", usecols = colunas)

    file = file[["AN_BASE", "NM_GRANDE_AREA_CONHECIMENTO", "NM_REGIAO", "SG_UF_PROGRAMA",
                 "CS_STATUS_JURIDICO", "CD_CONCEITO_CURSO", "NM_GRAU_CURSO"]]
    
    file.columns = ["ano", "grande_area_conhecimento", "regiao",
                    "UF_curso", "status_juridico", "conceito_curso", "grau_curso"]
    
    file["conceito_curso"] = file["conceito_curso"].replace("A", "5")
    file["conceito_curso"] = file["conceito_curso"].astype(int)

    file["CTI"] = file["grande_area_conhecimento"].apply(lambda x: 0 if x in lista_outras else 1)
    
    return file

def lists(file):

    lista_anos = list(file["ano"].unique())
    lista_total = []
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i}")
        lista_total.append(dados.shape[0])

    lista_nordeste = []
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i} and regiao == 'NORDESTE'")
        lista_nordeste.append(dados.shape[0])

    lista_pb = [] 
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i} and UF_curso == 'PB'")
        lista_pb.append(dados.shape[0])

    lista_conceito_fechado = []
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i} and conceito_curso >= 5")
        lista_conceito_fechado.append(dados.shape[0])
    
    lista_conceito_aberto = []
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i} and conceito_curso > 5")
        lista_conceito_aberto.append(dados.shape[0])

    lista_mestrado = []
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i}")
        dados = dados.query("grau_curso == 'MESTRADO' or grau_curso == 'MESTRADO PROFISSIONAL'")
        lista_mestrado.append(dados.shape[0])
    
    lista_doutorado = []
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i}")
        dados = dados.query(f"grau_curso == 'DOUTORADO' or grau_curso == 'DOUTORADO PROFISSIONAL'")
        lista_doutorado.append(dados.shape[0])

    lista_cti = []
    for i in range(min(list(file["ano"].unique())), max(list(file["ano"].unique())) + 1):
        dados = file.query(f"ano == {i} and CTI == 1")
        lista_cti.append(dados.shape[0])


    new_file = pd.DataFrame({"ano": lista_anos, 
                             "total_cursos": lista_total,
                             "CTI": lista_cti,
                             "nordeste": lista_nordeste,
                             "PB": lista_pb,
                             "mestrado": lista_mestrado,
                             "doutorado": lista_doutorado,
                             "conceito_maior_igual_cinco": lista_conceito_fechado,
                             "conceito_maior_cinco": lista_conceito_aberto})
    
    new_file.set_index("ano")

    new_file.to_excel("/Users/pedroafmelo/Documents/projetos/sidtec_pb/etapa_2/pessoas_recursos/dados/cursos_posgrad_agg.xlsx", 
                    index = False)


lista_df = []

for arquivos in lista:
    lista_df.append(read(arquivos))

final_data = pd.concat(lista_df, ignore_index= True)

lists(final_data) 