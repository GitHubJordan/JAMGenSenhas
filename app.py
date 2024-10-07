import flet as ft
import random
import string

def main(page: ft.Page):
    def gerar_senha(e):
        tamanho = slider_tamanho.value
        senha = gerar_senha_personalizada(int(tamanho), nome.value, aniversario.value, comida_favorita.value)
        senha_gerada.value = f"Senha Gerada: {senha}"
        page.update()

    def gerar_senha_personalizada(tamanho, nome="", aniversario="", comida_favorita=""):
        dados_pessoais = (nome + aniversario + comida_favorita).replace(" ", "")
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(dados_pessoais + caracteres) for _ in range(tamanho))
        return senha

    slider_tamanho = ft.Slider(min=8, max=32, label="Tamanho da senha", value=12)
    nome = ft.TextField(label="Nome (opcional)")
    aniversario = ft.TextField(label="Data de Aniversário (opcional)")
    comida_favorita = ft.TextField(label="Comida Favorita (opcional)")
    senha_gerada = ft.Text(value="Senha Gerada:", size=20)
    gerar_btn = ft.ElevatedButton("Gerar Senha", on_click=gerar_senha)
    
    page.add(slider_tamanho, nome, aniversario, comida_favorita, gerar_btn, senha_gerada)

ft.app(target=main)
