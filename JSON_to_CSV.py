import json
import csv

with open('arquivo.json', 'r') as arquivo_json: #Subistitua arquivo.json para o caminho do seu arquivo
    dados = json.load(arquivo_json)

with open('arquivo.csv', 'w', newline='') as arquivo_csv: #Subistitua arquivo.csv por um nome desejavel do seu arquivo CSV
    escrever = csv.writer(arquivo_csv)

    if dados:
        cabecalhos = dados[0].keys()
        escrever.writerow(cabecalhos)

    for linha in dados:
        escrever.writerow(linha.values())