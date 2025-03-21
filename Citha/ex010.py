import os
import time
import pandas as pd
import sqlite3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Função para processar o CSV (análise e geração de relatório)
def processar_csv(caminho_csv):
    print(f"Processando arquivo: {caminho_csv}")
    
    # Lê o arquivo CSV
    df = pd.read_csv(caminho_csv, delimiter=";")
    
    # Aqui você pode fazer qualquer análise com o pandas
    print(df.describe())  # Exemplo: mostrando estatísticas descritivas
    
    # Exemplo: criar um gráfico de barras (como mencionado anteriormente)
    import matplotlib.pyplot as plt
    df.plot(kind='bar', x='Produto', y='Vendido', color='skyblue')
    plt.title("Vendas por Produto")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade Vendida")
    
    # Salvar o gráfico
    plt.savefig('grafico_vendas.png')
    
    # Exemplo de relatório adicional: salvar como um arquivo Excel
    df.to_excel("relatorio_vendas.xlsx", index=False)

    print("Relatório gerado com sucesso!")

# Função para inserir dados no banco de dados SQLite
def atualizar_banco_dados(caminho_csv, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Criar tabela se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Produto TEXT,
        Quantidade INTEGER,
        Preco REAL,
        Vendido INTEGER,
        Total_Vendido REAL,
        Custo REAL
    );
    """)

    # Ler os dados do CSV
    df = pd.read_csv(caminho_csv, delimiter=";")
    
    # Inserir os dados no banco
    for index, row in df.iterrows():
        cursor.execute("""
        INSERT INTO vendas (Produto, Quantidade, Preco, Vendido, Total_Vendido, Custo)
        VALUES (?, ?, ?, ?, ?, ?);
        """, (row['Produto'], row['Quantidade'], row['Preco'], row['Vendido'], row['Total Vendido Por Produto'], row['Custo']))

    # Salvar e fechar a conexão
    conn.commit()
    conn.close()

    print(f"Dados do arquivo {caminho_csv} inseridos no banco de dados.")

# Classe que vai monitorar a pasta
class MonitorPastaHandler(FileSystemEventHandler):
    def __init__(self, pasta_monitorada, db_file):
        self.pasta_monitorada = pasta_monitorada
        self.db_file = db_file

    def on_created(self, event):
        # Verifica se o arquivo é um CSV
        if event.is_directory:
            return
        
        if event.src_path.endswith(".csv"):
            print(f"Novo arquivo CSV detectado: {event.src_path}")
            
            # Processar o arquivo CSV
            processar_csv(event.src_path)
            
            # Atualizar o banco de dados
            atualizar_banco_dados(event.src_path, self.db_file)

# Função para iniciar o monitoramento da pasta
def monitorar_pasta(pasta_monitorada, db_file):
    event_handler = MonitorPastaHandler(pasta_monitorada, db_file)
    observer = Observer()
    observer.schedule(event_handler, pasta_monitorada, recursive=False)
    
    print(f"Monitorando a pasta: {pasta_monitorada}")
    
    observer.start()
    try:
        while True:
            time.sleep(1)  # Monitorar a pasta continuamente
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Caminho da pasta que você quer monitorar e o banco de dados SQLite
pasta_monitorada = "C:/caminho/para/sua/pasta"  # Altere para o caminho da sua pasta
db_file = "vendas.db"  # Caminho do banco de dados SQLite

# Iniciar o monitoramento
monitorar_pasta(pasta_monitorada, db_file)
