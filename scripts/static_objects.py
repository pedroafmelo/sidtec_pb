"""
Routine responsible for
static objects.

__author__ = "Nercino Neto"
"""


import os
import re
from unidecode import unidecode


# Default url
url_static_objects = os.path.abspath(__file__)

# Directories
url_scripts = os.path.dirname(url_static_objects)
url_sidtec_pb = os.path.dirname(url_scripts)
url_raw_data = os.path.join(url_sidtec_pb, "raw_data")
url_processed_data = os.path.join(url_sidtec_pb, "processed_data")
url_img = os.path.join(url_sidtec_pb, "img")

# raw_data files
url_dbt_2020_file = os.path.join(url_raw_data, "dbt_2020.csv")


# processed_data files
url_data_for_search_pt_br = os.path.join(
    url_processed_data, "data_for_search_pt_br.csv"
)

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
