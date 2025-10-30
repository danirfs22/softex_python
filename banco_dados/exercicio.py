# 1- Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db

import sqlite3

DB_PATH = 'escola_v2.db'

db_connection = sqlite3.connect(DB_PATH)

# 2 - Faça a query para pegar toda a tabela alunos e imprima na tela.
cursor = db_connection.cursor()
query_sql = 'SELECT * FROM Aluno'
cursor.execute(query_sql)
query_result = cursor.fetchall()
print(query_result)

