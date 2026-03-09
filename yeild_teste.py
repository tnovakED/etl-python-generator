import pandas as pd
import csv
from datetime import datetime

path = r"D:\Testes Python 2026\dados_operacionais.csv"

dados_csv = pd.read_csv(path)

def extrair_dados_csv(caminho):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            yield linha

def transformar_dados(dados):
    for linha in dados:
        linha['nome_tripulante'] = linha['nome_tripulante'].strip().upper()
        
        linha['status_voo'] = linha['status_voo'].strip().upper()
        
        yield linha
        
        
def transforma_date(dados):
    for linha in dados:
        data_bruta = linha['data_voo']
        
        if not data_bruta or str(data_bruta).lower() == 'nan':
            linha['data_voo'] = 'DATA AUSENTE'
        else:
            dt = None
            try:
                dt = datetime.strptime(data_bruta, '%Y-%m-%d')
            except ValueError:
                try:
                    dt = datetime.strptime(data_bruta, "%d/%m/%Y")
                except ValueError:
                    dt = None
        
            if dt:
                linha['data_voo'] = dt.strftime("%d-%m-%Y")
            else:
                linha['data_voo'] = "Erro no formato"
        
        yield linha

def processamento_final():
    dados = extrair_dados_csv(path)
    dados = transformar_dados(dados)
    dados = transforma_date(dados)    
    return dados


colunas = ['id_voo', 'data_voo', 'nome_tripulante', 'status_voo', 'consumo_combustivel_kg', 'aeroporto_origem']

with open("dados_operacionais_gold", 'w', encoding='utf-8') as saida:
    escrever = csv.DictWriter(saida, fieldnames=colunas)
    escrever.writeheader()
    
    for voo in processamento_final():
        escrever.writerow(voo)

print("arquivo gerado com sucesso")