import sqlite3
from database.connection import get_connection

def salvar_usuario(nome, email, cpf, senha_hash):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO usuarios (nome, email, cpf, senha) Values(?, ?, ?, ?)''', (nome, email, cpf, senha_hash))
        conn.commit()
        print("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("CPF ou Email já cadastrado!")    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        conn.close()