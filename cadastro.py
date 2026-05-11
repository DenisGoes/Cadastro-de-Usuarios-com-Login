from email_validator import validate_email, EmailNotValidError #lib para validação de email
from validate_docbr import CPF #lib para vidalção de cpf
import re #lib para expressões regulares

cpf = CPF()
print(cpf.generate()) #Gerador de cpf para teste do sistema!


def validar_nome(nome):
    nome = nome.strip() 
    return not(any(not (v.isalpha() or v.isspace()) for v in nome) or "  " in nome or len(nome.split()) < 2)


def validar_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def validar_cpf(numero):
    cpf = CPF()
    numero = numero.strip()
    return cpf.validate(numero)


def validar_senha(senha):
    if len(senha) < 6:
        raise ValueError("Mínimo 6 caracteres")
    if not re.search(r"[A-Z]", senha):
        raise ValueError("Falta letra maíuscula")
    if not re.search(r"[a-z]", senha):
        raise ValueError("Falta letra minúscula")
    if not re.search(r"[0-9]", senha):
        raise ValueError("Falta número")
    if not re.search(r"[!@#$%&*]", senha):
        raise ValueError("Falta caractere especial")
    





# autenticacao de usuarios, apos o cadastro o user vai poder fazer login 
# controle de tentativas de login e bloqueio 