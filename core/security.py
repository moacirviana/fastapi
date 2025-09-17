from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')
''''
FUNCAO PARA VERIFICAR SE A SENHA ESTA CORRETA, COMPARANDO
A SENHA EM TEXTO PURO E O HASH DA SENHA
'''
def verificar_senha (senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

''''
RETORNA O HASH DA SENHA
'''
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)
