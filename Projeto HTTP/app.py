import requests
import json
import os

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

nome_da_pasta = 'Projeto HTTP'
os.makedirs(nome_da_pasta, exist_ok=True)
caminho_arquivo = os.path.join(nome_da_pasta, f'{nome_do_restaurante}.json')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    caminho_completo = os.path.join(nome_da_pasta, nome_do_arquivo)
    with open(caminho_completo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)