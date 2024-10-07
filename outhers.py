import random
import string

def gerar_senha_personalizada(tamanho, nome="", aniversario="", comida_favorita="", maiusculas=True, minusculas=True, numeros=True, simbolos=True):
    caracteres = ""
    
    # Dados pessoais fornecidos
    dados_pessoais = (nome + aniversario + comida_favorita).replace(" ", "")
    
    if maiusculas:
        caracteres += string.ascii_uppercase  # Letras maiúsculas
    if minusculas:
        caracteres += string.ascii_lowercase  # Letras minúsculas
    if numeros:
        caracteres += string.digits  # Números
    if simbolos:
        caracteres += string.punctuation  # Símbolos especiais
    
    # Se o usuário fornecer dados pessoais, mistura os dados com caracteres aleatórios
    if dados_pessoais:
        senha = ''.join(random.choice(dados_pessoais + caracteres) for _ in range(tamanho))
    else:
        # Caso contrário, apenas usa os caracteres escolhidos
        if not caracteres:
            raise ValueError("É necessário selecionar pelo menos uma categoria de caracteres.")
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Exemplo de uso:
tamanho_senha = int(input("Digite o tamanho da senha: "))
nome = input("Digite seu nome (opcional): ")
aniversario = input("Digite sua data de aniversário (opcional): ")
comida_favorita = input("Digite sua comida favorita (opcional): ")
usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

senha_gerada = gerar_senha_personalizada(
    tamanho_senha, 
    nome=nome, 
    aniversario=aniversario, 
    comida_favorita=comida_favorita,
    maiusculas=usar_maiusculas, 
    minusculas=usar_minusculas, 
    numeros=usar_numeros, 
    simbolos=usar_simbolos
)

print("Senha gerada:", senha_gerada)
