"""
Creating a search function
using Levenshtein Distance.

__author__ = "Nercino Neto"
"""


import os
from thefuzz import fuzz
import pandas as pd
import static_variables as static
from organizing_for_research import cleaning_string


def get_df() -> pd.DataFrame:
    """
    Return a DataFrame
    from the file "dbt_2020"
    """

    df = pd.read_csv(
        static.url_data_for_search_pt_br,
        sep=static.sep,
        encoding=static.encoding)

    return df


def fuzz_filter(text: str, pesq_list: list[str]) -> list[(int, float)]:
    """
    Apply the Levenshtein Distance method
    """

    fuzz_results = []

    for index, pesq_text in enumerate(pesq_list):
        fuzz_results.append((index, fuzz.partial_ratio(text, pesq_text)))

    return fuzz_results


def score_filter(
    results: list[(int, float)], min_score: float = 90.0
) -> list[int]:
    """
    Returns indexes with
    scores greater than or
    equal to "min_score"
    """

    return [index for index, score in results if score >= min_score]


def separate_results_NM_columns(
    df: pd.DataFrame, indexs: list[int]
) -> (list[str], list[str]):
    """
    Returns the names
    of people present
    in the results
    """

    nm_discente = []
    nm_orientador = []

    for index in indexs:
        row = df.iloc[index]
        nm_discente.append(row.NM_DISCENTE)
        nm_orientador.append(row.NM_ORIENTADOR)

    return (nm_discente, nm_orientador)


def search(text: str) -> (list[str], list[str]) or None:
    """
    Search text in a DataFrame
    using the Levenshtein Distance
    method and return the names in
    "NM_DISCENTE" and "NM_ORIENTADOR"
    """
    
    # Preparing base variables
    text = cleaning_string(text)
    df = get_df()
    pesq_list = df.PESQ_PT.values
    
    # Applying search
    fuzz_results = fuzz_filter(text, pesq_list)
    filtered_choices = score_filter(fuzz_results)
    search_result = separate_results_NM_columns(df, indexs=filtered_choices)

    return search_result

if __name__ == '__main__':
    print(search('Energia solar'))
        