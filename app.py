import numpy as np
import pandas as pd
import time
import streamlit as st
from st_keyup import st_keyup
from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container 
import io
import scripts.static_objects as static
from scripts.search import search 


st.set_page_config(page_title= "SIDTEC-PB",
                   page_icon= "👨🏽‍🎓",
                   layout = "wide")


dataframe_csv_path = static.url_dbt_2020_file

@st.cache_data
def get_datas() -> pd.DataFrame:
    return pd.read_csv(dataframe_csv_path, encoding = "UTF-8")
dados = get_datas()


def main():
    layout()
    opt_menu()


def layout():
    c1, c2, c3, c4 = st.columns(4)
    col1, col2, col3 = c1.columns(3)   
    coluna1, coluna2, coluna3 = c2.columns(3)
    column1, column2, column3 = c3.columns(3)
    colunas1, colunas2, colunas3 = c4.columns(3)
    column2.image(static.url_fapesq, width = 190)
    col1.image(static.url_logo_facebook, width = 255)
    coluna2.image(static.url_ufpb, width = 160)
    colunas3.image(static.url_lema, width = 130)

    st.write("#")
    st.title("SIDTec-PB")

    st.markdown("""<h5 style = 'color: grey;'>Sistema de Inteligência de Dados 
               em Ciência e Tecnologia na Paraíba</h5>""",
               unsafe_allow_html= True)
    
    st.markdown("""<hr style="height:2px;border:none;color:red;background-color:red;" /> """,
                unsafe_allow_html=True)


def opt_menu():
    selected = option_menu(
        menu_title= None,
        options = ["Home", "Dados"],
        icons = ["house", "database"],
        default_index= 0,
        orientation= "horizontal"
    )

    if selected == "Home":
        search_bar()
    
    elif selected == "Dados":
        df_vis()

def search_bar():

    st.write("#")
    st.markdown("""<h5 style= 'text-align: center; color: grey;'
                    >Pesquise por um tema (Palavras-chave, campos acadêmicos...)</h5>""",
                    unsafe_allow_html= True)
    value = st_keyup("🔎")
    result = search(value)
    dataframe = pd.DataFrame({"Especialista": result[1]})
    st.write("#")
    
    st.dataframe(dataframe["Especialista"].drop_duplicates().head(5),
                 use_container_width= True,
                 hide_index= True)

def df_vis():
    st.write("#")
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):  
        
        st.markdown("""<h5 style= 'text-align: left; color: grey;'
                    >Foram utilizados os dados abertos da plataforma Sucupira, especificamente
                    a base de teses e dissertações da Paraíba no ano de 2020</h5>""", unsafe_allow_html= True)
        
    st.write("#")

    st.link_button("Baixar arquivo Excel",
                    "https://dadosabertos.capes.gov.br/dataset/36d1c92c-f9e0-4da1-a4f0-633e6ebefe03/resource/2a39435e-394e-4406-9b47-6a2bf90a814c/download/br-capes-btd-2017a2020-2021-12-03_2020.xlsx")
    
    st.write("#")

    st.dataframe(dados)

    st.write("#")
    
    with st.container():
        st.markdown("""<h5 style= 'text-align: center; color: grey;'
                    >Principais colunas</h5>""", unsafe_allow_html= True)
        st.write("#")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        ex1 = col1.expander("NM_ORIENTADOR")
        ex1.write("Nome do orientador")
        ex2 = col2.expander("NM_DISCENTE")
        ex2.write("Nome do discente")
        ex3 = col3.expander("NM_PRODUCAO")
        ex3.write("Nome da tese/ dissertação")
        ex4 = col4.expander("NM_PROGRAMA")
        ex4.write("Nome do curso")
        ex5 = col5.expander("DS_RESUMO")
        ex5.write("Resumo da tese")
        ex6 = col6.expander("DS_PALAVRA_CHAVE")
        ex6.write("Palavras-chave da tese")
        
    st.write("#")
    with st.container():
        c1, c2, c3 = st.columns(3)
        col1, col2, col3 = c3.columns(3)
        coluna1, coluna2, coluna3 = c1.columns(3)
        coluna2.image(static.url_plataforma_sucupira_removebg_preview, width = 290)
        col2.image(static.url_capes, width = 150)

    




if __name__ == "__main__":
    main()
