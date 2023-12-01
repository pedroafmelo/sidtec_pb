"""
Organizing the "dbt_2020" file for search.

__author__ = "Nercino Neto"
"""
import pandas as pd
import static_objects as static


def get_df() -> pd.DataFrame:
    """
    Return a DataFrame
    from the file "dbt_2020"
    """

    df = pd.read_csv(
        static.url_dbt_2020_file,
        sep=static.sep,
        encoding=static.encoding,
        usecols=static.useful_columns,
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

    return df.loc[:, static.useful_columns_pt_br]


def clear_strings_from_a_column(
    df: pd.DataFrame, column=static.pt_br_column
) -> pd.DataFrame:
    """
    clear data from a
    column with the
    "cleaning_string" function
    """

    df.loc[:, column] = df[column].apply(static.cleaning_string)

    return df


def create_csv(df: pd.DataFrame) -> None:
    """
    Create a "data_for_search_pt_br.csv" file
    """

    df.to_csv(static.url_data_for_search_pt_br, index=False)


def organizing_for_research() -> None:
    """
    Create a csv file
    with a research column
    """

    df = get_df()
    df = build_search_column_PT_BR(df)
    df = filter_useful_columns(df)
    df = clear_strings_from_a_column(df)
    create_csv(df)


if __name__ == "__main__":
    organizing_for_research()
