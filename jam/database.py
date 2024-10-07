import sqlite3

# Função para criar a tabela de senhas
def criar_tabela():
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plataforma TEXT,
            nome_usuario TEXT,
            senha TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para salvar uma senha no banco de dados
def salvar_senha(plataforma, nome_usuario, senha):
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO senhas (plataforma, nome_usuario, senha)
        VALUES (?, ?, ?)
    ''', (plataforma, nome_usuario, senha))
    conn.commit()
    conn.close()

# Função para listar todas as senhas armazenadas no banco de dados
def listar_senhas():
    conn = sqlite3.connect("senhas.db")
    cursor = conn.cursor()
    cursor.execute('SELECT id, plataforma, nome_usuario, senha FROM senhas')
    senhas = cursor.fetchall()
    conn.close()
    return senhas
