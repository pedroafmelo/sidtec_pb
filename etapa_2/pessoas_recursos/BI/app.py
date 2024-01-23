import pandas as pd
import streamlit as st
import os
import scripts.static_objects as static
import plotly.express as pex
import json

dados_main = "/Users/pedroafmelo/Documents/projetos/sidtec_pb/etapa_2/pessoas_recursos/dados/new_data.xlsx"

colunas_br = ['ANO', 'POP_BR', 'POP_BR_10K', 'POP_BR_100K', 'POP_PB', 'POP_PB_10K',
       'POP_PB_100K', 'POP_NE', 'POP_NE_10K', 'POP_NE_100K', 'CAPES_CTI_BR',
       'CAPES_OUTRAS_BR', 'CNPQ_MES_DOC_BR', 'CNPQ_PQ_BR']

colunas_pb = ['ANO', 'POP_BR', 'POP_BR_10K', 'POP_BR_100K', 'POP_PB', 'POP_PB_10K',
       'POP_PB_100K', 'POP_NE', 'POP_NE_10K', 'POP_NE_100K', 'CAPES_CTI_PB', 'CAPES_OUTRAS_PB',
       'CNPQ_MES_DOC_PB', 'CNPQ_PQ_PB']

colunas_ne = ['ANO', 'POP_BR', 'POP_BR_10K', 'POP_BR_100K', 'POP_PB', 'POP_PB_10K',
       'POP_PB_100K', 'POP_NE', 'POP_NE_10K', 'POP_NE_100K', 'CAPES_CTI_NE',
       'CAPES_OUTRAS_NE','CNPQ_MES_DOC_NE', 'CNPQ_PQ_NE']

st.set_page_config(page_title= "FOMENTO",
                   page_icon= "💵",
                   layout = "wide",
                   initial_sidebar_state= "collapsed")

def main():
    layout()
    dashboard()

@st.cache_data
def get_datas(data) -> pd.DataFrame:
    return pd.read_excel(data)

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
    


def dashboard():

    total_grande_area_br_df = pd.read_excel(static.url_perspectiva, "dados/grande_area_br_df.xlsx")
    total_grande_area_pb_df = pd.read_excel(static.url_perspectiva, "/dados/grande_area_pb_df.xlsx")
    total_grande_area_ne_df = pd.read_excel(static.url_perspectiva, "/dados/grande_area_ne_df.xlsx")

    c1, c2 = st.columns(2)
    c1.write("#")
    c2.write("#")
    
    dados_main = "/Users/pedroafmelo/Documents/projetos/sidtec_pb/etapa_2/pessoas_recursos/dados/new_data.xlsx"
    

    dados_main = get_datas(dados_main)


    nome_categorias = {
        "ANO": "Ano",
        "Valor": "CTI/Outras",
        "Categoria": "Abrangência Territorial"
    }


    dados_longos = pd.melt(dados_main, id_vars=['ANO'], value_vars=["cti/outras_br", "cti/outras_pb", "cti/outras_ne"],
                           var_name='Categoria', value_name='Valor')

    graph_bolsas_capes = pex.line(dados_longos, x="ANO", y="Valor", color='Categoria',markers = True,
                                  labels= nome_categorias)

    c1.markdown("""<h5 style = 'color: grey;'>Bolsas CAPES em CTI/Outras Áreas</h5>""",
                  unsafe_allow_html= True)
    c1.plotly_chart(graph_bolsas_capes)


    coluna1, coluna2, coluna3 = c2.columns([1,4,1])
    coluna2.markdown("""<h5 style = 'color: grey;'>Quantidade de Bolsas CAPES por grande área</h5>""",
                  unsafe_allow_html= True)

    
    col1, col2, col3 = c2.columns(3)
    col2.write("#")
    ab_geog = coluna2.selectbox("Abrangência Geográfica", options = ["Brasil", "Nordeste", "PB"])
    if ab_geog == "Brasil":
        coluna2.dataframe(total_grande_area_br_df)
    elif ab_geog == "Nordeste":
        coluna2.dataframe(total_grande_area_ne_df)
    elif ab_geog == "PB":
        coluna2.dataframe(total_grande_area_pb_df)

    column1, column2 = st.columns(2)
    column1.metric("Porcentagem de Bolsas CAPES CTI", "67 %")
    column2.metric("Porcentagem de Bolsas CAPES na PB com relação ao total", "3%")


    c1, c2 = st.columns(2)
    c1.write("#")
    c1.write("#")

    tog = c1.toggle("Por 100 mil habitantes")


    if not tog:

        nome_categorias = {
        "ANO": "Ano",
        "Valor": "Bolsas por 10 mil ",
        "Categoria": "Abrangência Territorial"
    }
        dados_longos = pd.melt(dados_main, id_vars=['ANO'], value_vars=["bolsas/pop10_BR", "bolsas/pop10_PB", "bolsas/pop10_NE"],
                               var_name='Categoria', value_name='Valor')

        graph_bolsas_capes = pex.line(dados_longos, x="ANO", y="Valor", color='Categoria',markers = True,
                                      labels= nome_categorias)
        st.markdown("""<h5 style = 'color: grey;'>Bolsas Capes por 10 mil habitantes </h5>""",
                  unsafe_allow_html= True)
        st.plotly_chart(graph_bolsas_capes, use_container_width= True)
    else: 
        nome_categorias = {
        "ANO": "Ano",
        "Valor": "Bolsas por 100 mil",
        "Categoria": "Abrangência Territorial"
    }
        dados_longos = pd.melt(dados_main, id_vars=['ANO'], value_vars=["bolsas/pop100_BR", "bolsas/pop100_PB", "bolsas/pop100_NE"],
                               var_name='Categoria', value_name='Valor')

        graph_bolsas_capes = pex.line(dados_longos, x="ANO", y="Valor", color='Categoria',markers = True,
                                      labels= nome_categorias)
        st.markdown("""<h5 style = 'color: grey;'>Bolsas Capes por 100 mil habitantes </h5>""",
                  unsafe_allow_html= True)
        st.plotly_chart(graph_bolsas_capes, use_container_width= True)

    c1, c2 = st.columns(2)
    c1.write("#")

    tog = c1.toggle("Produtividade em pesquisa")
    if not tog:
        nome_categorias = {
        "ANO": "Ano",
        "Valor": "Bolsas MES/DOC por 10 mil habitantes",
        "Categoria": "Abrangência Territorial"
    }
        dados_longos = pd.melt(dados_main, id_vars=['ANO'], value_vars=["bolsas_md/pop10_br", "bolsas_md/pop10_pb", "bolsas_md/pop10_ne"],
                               var_name='Categoria', value_name='Valor')

        graph_bolsas_capes = pex.line(dados_longos, x="ANO", y="Valor", color='Categoria',markers = True,
                                      labels= nome_categorias)
        st.markdown("""<h5 style = 'color: grey;'>Bolsas CNPQ de Mestrado e Doutorado por 10 mil habitantes </h5>""",
                  unsafe_allow_html= True)
        st.plotly_chart(graph_bolsas_capes, use_container_width= True)
    else: 
        nome_categorias = {
        "ANO": "Ano",
        "Valor": "Bolsas PQ por 10 mil habitantes",
        "Categoria": "Abrangência Territorial"
    }
        dados_longos = pd.melt(dados_main, id_vars=['ANO'], value_vars=["bolsas_pq/pop10_br", "bolsas_pq/pop10_pb", "bolsas_pq/pop10_ne"],
                               var_name='Categoria', value_name='Valor')

        graph_bolsas_capes = pex.line(dados_longos, x="ANO", y="Valor", color='Categoria',markers = True,
                                      labels= nome_categorias)
        st.markdown("""<h5 style = 'color: grey;'>Bolsas CNPQ de Produtividade em Pesquisa por 10 mil habitantes</h5>""",
                  unsafe_allow_html= True)
        st.plotly_chart(graph_bolsas_capes, use_container_width= True)
    


if __name__ == "__main__":
    main()