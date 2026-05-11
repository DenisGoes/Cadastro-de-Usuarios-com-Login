from database.db_init import init_db
from database.user_repository import salvar_usuario
from cadastro import validar_nome, validar_email, validar_cpf, validar_senha
import bcrypt 

init_db()

nome = input("Digite seu nome completo: ")
if not validar_nome(nome):
    exit("Nome inválido")

email = input("Digite seu email: ")
if not validar_email(email):
    exit("Email inválido")

cpf = input("Digite seu CPF: ")
if not validar_cpf(cpf):
    exit("CPF inválido")

try:
    senha = input("Digite sua senha: ").strip()
    validar_senha(senha)

    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode() #Transformando senha em hash
except ValueError as e:
    exit(f"Erro: {e}")


salvar_usuario(nome, email, cpf, senha_hash)
