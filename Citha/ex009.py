import sqlite3
import pandas as pd

# Função para criar a tabela e inserir dados do CSV no banco de dados SQLite
def atualizar_banco_dados(csv_file, db_file):
    # Conectar ao banco de dados (se não existir, ele será criado)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Criar tabela, se não existir (incluindo o campo "Custo")
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

    # Ler o CSV
    dados_csv = pd.read_csv(csv_file, delimiter=";")
    
    # Inserir dados no banco de dados (incluindo o "Custo")
    for index, row in dados_csv.iterrows():
        cursor.execute("""
        INSERT INTO vendas (Produto, Quantidade, Preco, Vendido, Total_Vendido, Custo)
        VALUES (?, ?, ?, ?, ?, ?);
        """, (row['Produto'], row['Quantidade'], row['Preco'], row['Vendido'], row['Total Vendido Por Produto'], row['Custo']))

    # Salvar as alterações e fechar a conexão
    conn.commit()
    conn.close()
    print("Banco de dados atualizado com sucesso.")

# Função para consultar dados usando pandas.read_sql()
def consultar_banco_dados(db_file):
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(db_file)

    # Consultar os dados (exemplo: listar todas as vendas)
    query = "SELECT * FROM vendas"
    df = pd.read_sql(query, conn)
    
    # Fechar a conexão
    conn.close()
    
    return df

# Caminho para o arquivo CSV e o banco de dados SQLite
csv_file = 'vendas.csv'  # Coloque o caminho do seu arquivo CSV
db_file = 'vendas.db'    # Caminho do banco de dados SQLite

# Atualizar o banco de dados
atualizar_banco_dados(csv_file, db_file)

# Consultar os dados
df_vendas = consultar_banco_dados(db_file)
print("Dados Consultados:")
print(df_vendas)