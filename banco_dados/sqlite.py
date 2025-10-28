import sqlite3
from pathlib import Path

# Diretório do arquivo atual
BASE_DIR = Path(__file__).resolve().parent
#print(BASE_DIR)

# Caminho completo do banco
DB_PATH = BASE_DIR / "db" / "escola_v2.db"
#print(DB_PATH)

# inicia a conexao com o banco de dados.
db_connection = sqlite3.connect('DB_PATH')

# cria o cursor
cursor = db_connection.cursor()

# executa qualquer comando SQL suportado pelo sqlite
cursor.execute("""
SELECT * 
FROM Aluno
""")

for row in cursor:
        print(row)

rows = cursor.fetchmany(5)

while rows:
    for row in rows:
        print(row)
    rows = cursor.fetchmany(5)
db_connection.close()

# Salva o resultado da query na variável
query_result = cursor.fetchall()

# Imprime o resultado da query
print(query_result)

# Encerra a conexao com o banco de dados
db_connection.close()

#Linha por linha
cursor.fetchone()
