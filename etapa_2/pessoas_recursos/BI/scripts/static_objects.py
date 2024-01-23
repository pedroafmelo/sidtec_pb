"""
Routine responsible for
static objects.

__author__ = "Nercino Neto"
"""


import os
import re
from unidecode import unidecode

# url dados ehd
url_ehd = "/Volumes/SEAGATE_EHD/sidtec_pb/pesquisa/drive_sid/"


# Default url
url_static_objects = os.path.abspath(__file__)

# Directories
url_scripts = os.path.dirname(url_static_objects)
url_BI = os.path.dirname(url_scripts)
url_perspectiva = os.path.dirname(url_BI)
url_img = os.path.join(url_BI, "img")

# Img files
url_capes = os.path.join(url_img, "capes.png")
url_fapesq = os.path.join(url_img, "fapesq.jpg")
url_lema = os.path.join(url_img, "lema.png")
url_logo_facebook = os.path.join(url_img, "logo_facebook.jpg")
url_plataforma_sucupira = os.path.join(url_img, "plataforma-sucupira.jpg")
url_plataforma_sucupira_removebg_preview = os.path.join(
    url_img, "plataforma-sucupira-removebg-preview.png"
)
url_ufpb = os.path.join(url_img, "ufpb.png")

# Drive files
bolsas_posgrad_capes_br_1995a2022 = os.path.join(url_ehd, 
                                                 "bolsas_pos_graduacao_capes_brasil_1995-2022.xlsx")
bolsas_posgrad_capes_pb_1995a2022 = os.path.join(url_ehd,
                                                 "bolsas_pos_graduacao_capes_pb_1995-2022.xlsx")
cnpq_mes_doc_br_2005a2023 = os.path.join(url_ehd,
                                         "cnpq_mestrado_doutorado_brasil_2005-2023.xlsx")
cnpq_ppq_br_2005a2023 = os.path.join(url_ehd,
                                     "cnpq_produtividade_pesquisa_brasil_2005-2023.xlsx")
orcamento_uni =  os.path.join(url_ehd,
                              "orçamento_universidades_2000_2023.xlsx")

pop = os.path.join(url_perspectiva, "/dados/POPULAÇÃO_1995A2022.xlsx")

# Useful columns
useful_columns = [
    "NM_ORIENTADOR",
    "NM_DISCENTE",
    "NM_PRODUCAO",
    "NM_PROGRAMA",
    "DS_RESUMO",
    "DS_PALAVRA_CHAVE",
]
useful_columns_pt_br = ["NM_ORIENTADOR", "NM_DISCENTE", "PESQ_PT"]
pt_br_column = "PESQ_PT"

# CSV reading
sep = ","
encoding = "UTF-8"

# Regex
regex_letters_numbers = r"[^A-Z0-9]"


def cleaning_string(text: str) -> str:
    """
    Cleaning string to
    facilitate application
    of the method
    Levenshtein Distance
    """

    # Removing special characters
    text = unidecode(text)

    # Applying uppercase for security
    text = text.upper()

    # Get only uppercase letters and numbers
    text = re.sub(regex_letters_numbers, "", text)

    return text



