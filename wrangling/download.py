import os
import requests

dbt_url = "https://dadosabertos.capes.gov.br/dataset/36d1c92c-f9e0-4da1-a4f0-633e6ebefe03/resource/e37df31a-f250-4405-8b21-ca7e5c7c1696/download/br-capes-btd-2017a2020-2021-12-03_2020.csv"

def download(url, local):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        with open(local, "wb") as new_file:
            new_file.write(response.content)
            print("Done.")
    else:
        response.raise_for_status()



if __name__ == "__main__":
    
    output_dir = os.getcwd()
    download(dbt_url, os.path.join(output_dir, "2020.csv"))