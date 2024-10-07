import flet as ft

def criar_lista_senhas(senhas, toggle_senha_callback, copiar_senha_callback):
    lista = []
    for senha in senhas:
        id_senha, plataforma, nome_usuario, senha_text = senha
        senha_oculta = ft.Text(value="******", data=id_senha)  # Adiciona o ID da senha ao data
        botao_toggle_senha = ft.ElevatedButton("Exibir", on_click=lambda e, senha_id=id_senha: toggle_senha_callback(e, senha_id))
        botao_copiar = ft.IconButton(ft.icons.COPY, on_click=lambda e, senha_text=senha_text: copiar_senha_callback(e, senha_text))

        # Adicionar elementos à lista
        lista.append(
            ft.Row(
                controls=[
                    ft.Text(f"Plataforma: {plataforma}"),
                    ft.Text(f"Usuário: {nome_usuario}"),
                    ft.Text("Senha:"),
                    senha_oculta,
                    botao_toggle_senha,
                    botao_copiar
                ]
            )
        )
    return lista


def criar_slider_tamanho(on_change_callback):
    return ft.Slider(min=8, max=32, label="Tamanho da senha", value=12, on_change=on_change_callback)

def criar_text_field(label, on_change_callback=None):
    return ft.TextField(label=label, on_change=on_change_callback)

def criar_botao_gerar(on_click_callback):
    return ft.ElevatedButton("Gerar Senha", on_click=on_click_callback)

def criar_texto_senha():
    return ft.Text(value="Senha Gerada:", size=20)

def criar_texto_senhas():
    return ft.Text(value="Senhas", size=22)

def criar_area_copiar_senha(on_click_callback):
    return ft.IconButton(ft.icons.COPY, on_click=on_click_callback)

def criar_text_field_password():
    return ft.TextField(label="Palavra-Passe (opcional)", password=True)
