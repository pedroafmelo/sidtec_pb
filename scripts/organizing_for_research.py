"""
Organizing the "dbt_2020" file for search.

__author__ = "Nercino Neto"
"""


import os
import re
import pandas as pd
from unidecode import unidecode


input_file = os.path.dirname(os.path.abspath(__file__)) + "/input/dbt_2020.csv"
output_dir = os.path.dirname(os.path.abspath(__file__)) + "/output/"


def get_df() -> pd.DataFrame:
    """
    Return a DataFrame
    from the file "dbt_2020"
    """

    df = pd.read_csv(
        input_file,
        sep=",",
        encoding="UTF-8",
        usecols=[
            "NM_ORIENTADOR",
            "NM_DISCENTE",
            "NM_PRODUCAO",
            "NM_PROGRAMA",
            "DS_RESUMO",
            "DS_PALAVRA_CHAVE",
        ],
    )

    return df


def build_search_column_PT_BR(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column by
    joining columns about
    Theses and Dissertations
    """

    df_new = df.assign(
        PESQ_PT=df.NM_PROGRAMA
        + df.NM_PRODUCAO
        + df.DS_RESUMO
        + df.DS_PALAVRA_CHAVE
    )

    return df_new


def filter_useful_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters only currently
    useful columns
    """

    return df[["NM_ORIENTADOR", "NM_DISCENTE", "PESQ_PT"]]


def cleaning_string(texto: str) -> str:
    """
    Cleaning string to
    facilitate application
    of the method
    Levenshtein Distance
    """

    # Removing special characters
    texto = unidecode(texto)

    # Applying uppercase for security
    texto = texto.upper()

    # Get only uppercase letters and numbers
    texto = re.sub(r"[^A-Z0-9]", "", texto)

    return texto


def clear_strings_from_a_column(
    df: pd.DataFrame, column="PESQ_PT"
) -> pd.DataFrame:
    """
    clear data from a
    column with the
    "cleaning_string" function
    """

    df.loc[:, column] = df[column].apply(cleaning_string)

    return df


def create_csv(df: pd.DataFrame) -> None:
    """
    Create a CSV file
    """

    df.to_csv("p1esq_test.csv")


def organizing_for_research() -> None:
    """
    Main routine,
    calls other functions
    """

    df = get_df()
    df = build_search_column_PT_BR(df)
    df = filter_useful_columns(df)
    df = clear_strings_from_a_column(df)
    create_csv(df)


if __name__ == "__main__":
    organizing_for_research()
