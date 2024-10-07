def validar_tamanho_senha(tamanho):
    if tamanho < 8:
        raise ValueError("O tamanho da senha deve ser de pelo menos 8 caracteres.")
    return True
