import pandas as pd
from sqlalchemy import create_engine

usuario = "jacksonls"
senha = "123"
host = "localhost"
porta = "5433"
banco = "jacksondb"

url_conexao = f"postgresql+psycopg://{usuario}:{senha}@{host}:{porta}/{banco}"

print("Conectando ao banco de dados PostgreSQL...")
engine = create_engine(url_conexao)

dados = {
    "produto": ["Notebook", "Mouse Gamer", "Teclado Mecânico", "Monitor 24\""],
    "preco": [4500.00, 150.00, 350.00, 1200.00],
    "quantidade_em_estoque": [10, 50, 30, 15]
}

df = pd.DataFrame(dados)

nome_tabela = "produtos"
print(f"Inserindo dados na tabela '{nome_tabela}'...")

df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

print("Dados inseridos com sucesso!")

print("\nConsultando os dados direto do banco:")
df_consultado = pd.read_sql(f"SELECT * FROM {nome_tabela}", con=engine)
print(df_consultado)