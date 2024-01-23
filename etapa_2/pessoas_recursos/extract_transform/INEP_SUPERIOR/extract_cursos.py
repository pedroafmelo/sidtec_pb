import os
import pandas as pd 
import wget
from zipfile import ZipFile
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



def baixar_censo():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    diretorio_dados = os.path.join(os.getcwd(), "dados")
    if not os.path.exists(diretorio_dados):
        os.makedirs(diretorio_dados)

    os.chdir(diretorio_dados)

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor = 0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    for i in range(1995, 2023):
        url = f"https://download.inep.gov.br/microdados/microdados_censo_da_educacao_superior_{i}.zip"
        nome_arquivo = f"{i}.zip"

        response = session.get(url, verify = False)
        with open(f"{i}.zip", "wb") as year_file:
            year_file.write(response.content)

        with ZipFile(nome_arquivo, "r") as zip_ref:
            zip_ref.extractall(f"{i}")

        time.sleep(2)

if __name__ == "__main__":
    baixar_censo()

