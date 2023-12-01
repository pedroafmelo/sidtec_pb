"""
Routine responsible for
static variables.

__author__ = "Nercino Neto"
"""


import os
import re


# Directories
url_input_dir = os.path.dirname(os.path.abspath(__file__)) + "/input/"
url_output_dir = os.path.dirname(os.path.abspath(__file__)) + "/output/"

# Input files
url_dbt_2020_file = url_input_dir + "dbt_2020.csv"

# Output files
url_data_for_search_pt_br = url_output_dir + "data_for_search_pt_br.csv"

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
