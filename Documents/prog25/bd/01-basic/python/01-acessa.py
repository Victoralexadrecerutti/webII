# importação da biblioteca do sqlite
import sqlite3

# conectar o banco de dados; se o arquivo não existe, será criado
conn = sqlite3.connect('example.db')

# o cursos é um objeto que pode ser usado para executar comandos SQL
cursor = conn.cursor()

# criar a tabela; com 3 aspas pode-se utilizar comandos SQL em múltiplas linhas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# inserir dados
# o uso de interrogações prevê ataques de SQL injection
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))

# criar dados para inserir múltiplas linhas, com o comando executemany
users_data = [
    ('Charlie', 35),
    ('Diana', 28)
]

# inserindo múltiplas linhas :-)
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)

# confirmar a gravação de dados
conn.commit()

# executar um SELECT
cursor.execute("SELECT * FROM users ORDER BY age")

# obter os resultados
rows = cursor.fetchall()

# mostrar os resultados
print("Usuários:")
for row in rows:
    print(row) # Each row is a tuple

# criar uma consulta específica
cursor.execute("SELECT * FROM users WHERE name = ?", ('Alice',))

# obter somente uma linha e mostrar
alice_data = cursor.fetchone() 
print("\nDados de Alice:", alice_data)

# fechar a conexão
conn.close()

print("\nFIM")