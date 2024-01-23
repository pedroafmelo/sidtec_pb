import pandas as pd
import scripts.static_objects as static

dict_grande_area = {"MULTIDISCIPLINAR": "CTI", "CIÊNCIAS AGRÁRIAS": "CTI", "CIÊNCIAS SOCIAIS APLICADAS": "OUTRAS",
                    "CIÊNCIAS EXATAS E DA TERRA": "CTI", "CIÊNCIAS DA SAÚDE": "CTI", "Grande Area Não Informada": "OUTRAS",
                    "CIÊNCIAS BIOLÓGICAS": "CTI", "ENGENHARIAS": "CTI", "CIÊNCIAS HUMANAS": "OUTRAS", 
                    "LINGÜÍSTICA, LETRAS E ARTES": "OUTRAS"}


def read(file) -> pd.DataFrame:
    data = pd.read_excel(file)
    data = data.query("ANO >= 2005 and ANO <= 2022")
    data = data.sort_values(by = "ANO")
    return data

bolsas_posgrad_capes_br_1995a2022 = read(static.bolsas_posgrad_capes_br_1995a2022)
bolsas_posgrad_capes_PB_1995a2022 = read(static.bolsas_posgrad_capes_pb_1995a2022)
cnpq_mes_doc_br_2005a2023 = read(static.cnpq_mes_doc_br_2005a2023)
cnpq_ppq_br_2005a2023 = read(static.cnpq_ppq_br_2005a2023)
populacao = pd.read_excel(static.pop, dtype = int).query("2005 <= ANO < 2023")

# Years list
lista_anos = list(range(2005, 2023))

# Populations lists
lista_pop_br = [pop for pop in populacao["POP_BR"]] 
lista_pop_ne = [pop for pop in populacao["POP_NE"]] 
lista_pop_pb = [pop for pop in populacao["POP_PB"]] 

# CAPES POST GRADUATION LISTS (BRAZIL)

bolsas_posgrad_capes_br_1995a2022["CTI"] = bolsas_posgrad_capes_br_1995a2022["GRANDEAREA"].map(dict_grande_area)

lista_CTI_br = []
for i in range(min(list(bolsas_posgrad_capes_br_1995a2022["ANO"].unique())), max(list(bolsas_posgrad_capes_br_1995a2022["ANO"].unique())) + 1):
    dados = bolsas_posgrad_capes_br_1995a2022.query(f"ANO == {i}")
    dados = dados.query("CTI == 'CTI'")
    total = dados["REFERENCIAL"].sum()
    lista_CTI_br.append(total)

lista_outras_br = []
for i in range(min(list(bolsas_posgrad_capes_br_1995a2022["ANO"].unique())), max(list(bolsas_posgrad_capes_br_1995a2022["ANO"].unique())) + 1):
    dados = bolsas_posgrad_capes_br_1995a2022.query(f"ANO == {i}")
    dados = dados.query("CTI == 'OUTRAS'")
    total = dados["REFERENCIAL"].sum()
    lista_outras_br.append(total)

# CAPES POST GRADUATION LISTS (PB)

bolsas_posgrad_capes_PB_1995a2022["CTI"] = bolsas_posgrad_capes_PB_1995a2022["GRANDEAREA"].map(dict_grande_area)

lista_CTI_pb = []
for i in range(min(list(bolsas_posgrad_capes_PB_1995a2022["ANO"].unique())), max(list(bolsas_posgrad_capes_PB_1995a2022["ANO"].unique())) + 1):
    dados = bolsas_posgrad_capes_PB_1995a2022.query(f"ANO == {i}")
    dados = dados.query("CTI == 'CTI'")
    total = dados["REFERENCIAL"].sum()
    lista_CTI_pb.append(total)

lista_outras_pb = []
for i in range(min(list(bolsas_posgrad_capes_PB_1995a2022["ANO"].unique())), max(list(bolsas_posgrad_capes_PB_1995a2022["ANO"].unique())) + 1):
    dados = bolsas_posgrad_capes_PB_1995a2022.query(f"ANO == {i}")
    dados = dados.query("CTI == 'OUTRAS'")
    total = dados["REFERENCIAL"].sum()
    lista_outras_pb.append(total)

# CAPES POST GRADUATION LISTS (NE)

bolsas_posgrad_capes_ne_1995a2022 = read(static.bolsas_posgrad_capes_br_1995a2022)
bolsas_posgrad_capes_ne_1995a2022 = bolsas_posgrad_capes_ne_1995a2022.query("REGIAO == 'NORDESTE'")

bolsas_posgrad_capes_ne_1995a2022.index = range(bolsas_posgrad_capes_ne_1995a2022.shape[0])

bolsas_posgrad_capes_ne_1995a2022["CTI"] = bolsas_posgrad_capes_ne_1995a2022["GRANDEAREA"].map(dict_grande_area)

lista_CTI_ne = []
for i in range(min(list(bolsas_posgrad_capes_ne_1995a2022["ANO"].unique())), max(list(bolsas_posgrad_capes_ne_1995a2022["ANO"].unique())) + 1):
    dados = bolsas_posgrad_capes_ne_1995a2022.query(f"ANO == {i}")
    dados = dados.query("CTI == 'CTI'")
    total = dados["REFERENCIAL"].sum()
    lista_CTI_ne.append(total)

lista_outras_ne = []
for i in range(min(list(bolsas_posgrad_capes_ne_1995a2022["ANO"].unique())), max(list(bolsas_posgrad_capes_ne_1995a2022["ANO"].unique())) + 1):
    dados = bolsas_posgrad_capes_ne_1995a2022.query(f"ANO == {i}")
    dados = dados.query("CTI == 'OUTRAS'")
    total = dados["REFERENCIAL"].sum()
    lista_outras_ne.append(total)

# MESTER AND DOCTOR POST GRADUATION CNPQ LISTS (BR)
lista_mes_doc_cnpq_br = []
for i in range(min(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())), max(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())) + 1):
    dados = cnpq_mes_doc_br_2005a2023.query(f"ANO == {i} and REGIAO != 'Exterior'")
    lista_mes_doc_cnpq_br.append(dados.shape[0])

# MESTER AND DOCTOR POST GRADUATION CNPQ LISTS (NE)

lista_mes_doc_cnpq_ne = []
for i in range(min(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())), max(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())) + 1):
    dados = cnpq_mes_doc_br_2005a2023.query(f"ANO == {i} and REGIAO == 'Nordeste'")
    lista_mes_doc_cnpq_ne.append(dados.shape[0])

# MESTER AND DOCTOR POST GRADUATION CNPQ LISTS (PB)
    
lista_mes_doc_cnpq_pb = []
for i in range(min(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())), max(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())) + 1):
    dados = cnpq_mes_doc_br_2005a2023.query(f"ANO == {i} and IDUF == 'PB'")
    lista_mes_doc_cnpq_pb.append(dados.shape[0])

# PRODUCTIVITY IN SCIENTIFIC RESEARCH CNPQ LISTS (BR)
lista_pq_cnpq_br = []
for i in range(min(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())), max(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())) + 1):
    dados = cnpq_ppq_br_2005a2023.query(f"ANO == {i} and REGIAO != 'Exterior'")
    lista_pq_cnpq_br.append(dados.shape[0])

# PRODUCTIVITY IN SCIENTIFIC RESEARCH CNPQ LISTS (NE)

lista_pq_cnpq_ne = []
for i in range(min(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())), max(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())) + 1):
    dados = cnpq_ppq_br_2005a2023.query(f"ANO == {i} and REGIAO == 'Nordeste'")
    lista_pq_cnpq_ne.append(dados.shape[0])

# PRODUCTIVITY IN SCIENTIFIC RESEARCH CNPQ LISTS (PB)

lista_pq_cnpq_pb = []
for i in range(min(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())), max(list(cnpq_mes_doc_br_2005a2023["ANO"].unique())) + 1):
    dados = cnpq_ppq_br_2005a2023.query(f"ANO == {i} and IDUF == 'PB'")
    lista_pq_cnpq_pb.append(dados.shape[0])

# CRRATING NEW DATAFRAME

new_data = pd.DataFrame({"ANO": lista_anos, "POP_BR": lista_pop_br,"POP_PB": lista_pop_pb, 
                         "POP_NE": lista_pop_ne,"CAPES_CTI_BR": lista_CTI_br, 
                         "CAPES_OUTRAS_BR": lista_outras_br, "CAPES_CTI_PB": lista_CTI_pb, 
                        "CAPES_OUTRAS_PB": lista_outras_pb,"CAPES_CTI_NE": lista_CTI_ne,
                        "CAPES_OUTRAS_NE": lista_outras_ne, "CNPQ_MES_DOC_BR": lista_mes_doc_cnpq_br, 
                        "CNPQ_MES_DOC_PB": lista_mes_doc_cnpq_pb,"CNPQ_MES_DOC_NE" : lista_mes_doc_cnpq_ne, 
                        "CNPQ_PQ_BR": lista_pq_cnpq_br, "CNPQ_PQ_PB": lista_pq_cnpq_pb, "CNPQ_PQ_NE": lista_pq_cnpq_ne})
 
new_data["cti/outras_BR"] = new_data["CAPES_CTI_BR"] / new_data["CAPES_OUTRAS_BR"]
new_data["cti/outras_PB"] = new_data["CAPES_CTI_PB"] / new_data["CAPES_OUTRAS_PB"]
new_data["cti/outras_NE"] = new_data["CAPES_CTI_NE"] / new_data["CAPES_OUTRAS_NE"]

new_data["bolsas_capes/pop10_BR"] = (new_data["CAPES_CTI_BR"] / new_data["POP_BR"]) * 10000
new_data["bolsas_capes/pop10_PB"] = (new_data["CAPES_CTI_PB"] / new_data["POP_PB"]) * 10000
new_data["bolsas_capes/pop10_NE"] = (new_data["CAPES_CTI_NE"] / new_data["POP_NE"]) * 10000

new_data["bolsas_capes/pop100_BR"] = (new_data["CAPES_CTI_BR"] / new_data["POP_BR"]) * 100000
new_data["bolsas_capes/pop100_PB"] = (new_data["CAPES_CTI_PB"] / new_data["POP_PB"]) * 100000
new_data["bolsas_capes/pop100_NE"] = (new_data["CAPES_CTI_NE"] / new_data["POP_NE"]) * 100000

new_data["bolsas_md/pop10_BR"] = (new_data["CNPQ_MES_DOC_BR"] / new_data["POP_BR"]) * 10000
new_data["bolsas_md/pop10_PB"] = (new_data["CNPQ_MES_DOC_PB"] / new_data["POP_PB"]) * 10000
new_data["bolsas_md/pop10_NE"] = (new_data["CNPQ_MES_DOC_NE"] / new_data["POP_NE"]) * 10000

new_data["bolsas_md/pop100_BR"] = (new_data["CNPQ_MES_DOC_BR"] / new_data["POP_BR"]) * 100000
new_data["bolsas_md/pop100_PB"] = (new_data["CNPQ_MES_DOC_PB"] / new_data["POP_PB"]) * 100000
new_data["bolsas_md/pop100_NE"] = (new_data["CNPQ_MES_DOC_NE"] / new_data["POP_NE"]) * 100000

new_data["bolsas_pq/pop10_BR"] = (new_data["CNPQ_PQ_BR"] / new_data["POP_BR"]) * 10000
new_data["bolsas_pq/pop10_PB"] = (new_data["CNPQ_PQ_PB"] / new_data["POP_PB"]) * 10000
new_data["bolsas_pq/pop10_NE"] = (new_data["CNPQ_PQ_NE"] / new_data["POP_NE"]) * 10000

new_data["bolsas_pq/pop100_BR"] = (new_data["CNPQ_PQ_BR"] / new_data["POP_BR"]) * 100000
new_data["bolsas_pq/pop100_PB"] = (new_data["CNPQ_PQ_PB"] / new_data["POP_PB"]) * 100000
new_data["bolsas_pq/pop100_NE"] = (new_data["CNPQ_PQ_NE"] / new_data["POP_NE"]) * 100000


# RETURNING AN EXCEL TABLE 

new_data.to_excel("/Users/pedroafmelo/Documents/projetos/sidtec_pb/etapa_2/pessoas_recursos/dados/bolsas_geral.xlsx", index = False) 
