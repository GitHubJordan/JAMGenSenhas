import random
import string

def gerar_senha_personalizada(tamanho, nome="", aniversario="", comida_favorita=""):
    dados_pessoais = (nome + aniversario + comida_favorita).replace(" ", "")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(dados_pessoais + caracteres) for _ in range(tamanho))
    return senha
