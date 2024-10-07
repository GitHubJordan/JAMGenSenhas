import flet as ft
from jam.ui_components import criar_slider_tamanho, criar_text_field, criar_botao_gerar, criar_texto_senha, criar_area_copiar_senha, criar_lista_senhas, criar_texto_senhas,criar_text_field_password
from jam.logic import gerar_senha_personalizada
from jam.database import criar_tabela, salvar_senha, listar_senhas

def iniciar_aplicacao(page: ft.Page):
    page.title = "JAMy | Gerenciador de Senhas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "auto"
    page.window.width = 600
    page.window.height = 450

    criar_tabela()  # Cria a tabela no banco de dados ao iniciar

    # Atualiza a lista de senhas geradas na interface
    def atualizar_lista_senhas():
        senhas = listar_senhas()
        lista_de_senhas.controls = criar_lista_senhas(senhas, toggle_senha, copiar_senha)
        page.update()

    # Função para armazenar credenciais do usuário
    def armazenar_credenciais(e):
        if palavra_passe.value:
            # Salvar as credenciais do usuário no banco de dados
            salvar_senha(plataforma.value, nome_usuario.value, palavra_passe.value)
            atualizar_lista_senhas()
            senha_gerada.value = "Armazenada com sucesso!"
            limpar_campos()  # Limpar campos após armazenar
            page.update()
        else:
            # Caso a palavra-passe não esteja preenchida, gerar senha
            gerar_senha(e)

    # Função para gerar senha
    def gerar_senha(e):
        senha = gerar_senha_personalizada(
            int(slider_tamanho.value), 
            nome.value, 
            aniversario.value, 
            comida_favorita.value
        )
        senha_gerada.value = senha
        # Salvar a senha no banco de dados
        salvar_senha(plataforma.value, nome_usuario.value, senha)
        atualizar_lista_senhas()
        limpar_campos()  # Limpar campos após gerar
        page.update()

    # Função para limpar os campos
    def limpar_campos():
        nome.value = ""
        aniversario.value = ""
        comida_favorita.value = ""
        plataforma.value = ""
        nome_usuario.value = ""
        palavra_passe.value = ""
        senha_gerada.value = ""

    # Função para copiar senha
    def copiar_senha(e, senha_text):
        page.set_clipboard(senha_text)

    # Função para exibir/ocultar a senha
    def toggle_senha(e, senha_id):
        for item in lista_de_senhas.controls:
            if item.controls[0].data == senha_id:  # Comparar com o ID da senha
                senha_control = item.controls[2]  # Controle que exibe a senha
                if senha_control.value == "******":
                    senha_control.value = item.controls[0].data  # Mostrar a senha
                    item.controls[3].text = "Ocultar"
                else:
                    senha_control.value = "******"  # Ocultar a senha
                    item.controls[3].text = "Exibir"
        page.update()

    # Criação dos componentes da interface
    slider_tamanho = criar_slider_tamanho(on_change_callback=None)
    nome = criar_text_field("Nome (opcional)")
    aniversario = criar_text_field("Data de Aniversário (opcional)")
    comida_favorita = criar_text_field("Comida Favorita (opcional)")
    plataforma = criar_text_field("Plataforma (ex: Facebook, Gmail)")
    nome_usuario = criar_text_field("Nome de Usuário")
    palavra_passe = criar_text_field_password()  # Campo para palavra-passe
    senha_gerada = criar_texto_senha()
    gerar_btn = criar_botao_gerar(armazenar_credenciais)  # Modificado para armazenar
    copiar_btn = criar_area_copiar_senha(copiar_senha)
    senhas = criar_texto_senhas()

    lista_de_senhas = ft.Column()
    atualizar_lista_senhas()

    # Adiciona todos os componentes à página
    page.add(
        slider_tamanho, nome, aniversario, comida_favorita, 
        plataforma, nome_usuario, palavra_passe,  # Novo campo adicionado
        gerar_btn, senha_gerada, copiar_btn,
        ft.Divider(),
        senhas,
        lista_de_senhas
    )
    page.update()

# No main.py, chamamos o ft.app com o target
if __name__ == "__main__":
    ft.app(target=iniciar_aplicacao)
