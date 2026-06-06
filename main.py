import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

caminho_arquivo = "alimentos.txt"
valores_principais = []

url_base = 'http://www.tbca.net.br/base-dados/composicao_alimentos.php'

cod_alimentos = []

parametros = {'pagina': 1}

continuar_loop = True

while continuar_loop:
    response = requests.get(url_base, params=parametros)

    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        tbody_element = soup.find('tbody')

        if tbody_element:

            tr_elements = tbody_element.find_all('tr')

            if tr_elements:

                for tr in tr_elements:
                    td_elements = tr.find_all('td')
                    cod_alimento = td_elements[0].text.strip()
                    classe_alimento = td_elements[4].text.strip()
                    # Extract the link to the detail page
                    link_element = td_elements[0].find('a')
                    if link_element:
                        produto_link = link_element.get('href')
                        cod_alimentos.append((cod_alimento, classe_alimento, produto_link))
            else:

                continuar_loop = False
        else:

            continuar_loop = False

        parametros['pagina'] += 1

    else:
        continuar_loop = False

result = []

for cod_alimento, classe_alimento, produto_link in cod_alimentos:

    url = urljoin(url_base, produto_link)

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    description_element = soup.find('h5', {'id': 'overview'})
    if description_element is None:
        print(f"Warning: Could not find description element for product {cod_alimento}. Skipping...")
        continue
    
    descricao = description_element.text.split('Descrição:')[1].split('<<')[0].strip()

    table = soup.find('table')

    thead = table.find('thead')
    headers = thead.find_all('th')[:3]

    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    nutrientes = []

    for row in rows:
        values = row.find_all('td')[:3]
        row_data = {}
        for i, header in enumerate(headers):
            row_data[header.text.strip()] = values[i].text.strip()
        nutrientes.append(row_data)

    alimento_json = {
        'codigo': cod_alimento,
        'classe': classe_alimento,
        'descricao': descricao,
        'nutrientes': nutrientes
    }

    with open(caminho_arquivo, "a") as file:

        produto_json_str = json.dumps(alimento_json)

        file.write(produto_json_str + "\n")
