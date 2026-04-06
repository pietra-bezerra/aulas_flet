import flet as ft
import random

def main(page: ft.Page):
    page.title = "Jogo de Escolhas Aleatório"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- BANCO DE DADOS (EXPANSÍVEL) ---
    dados_fases = [
        {"pergunta": "Quem faz 'Au Au'?", "correto": "Cachorro", "imagem": "https://picsum.photos/200/200?sig=1"},
        {"pergunta": "Quem vive na água?", "correto": "Peixe", "imagem": "https://picsum.photos/200/200?sig=2"},
        {"pergunta": "Quem gosta de banana?", "correto": "Macaco", "imagem": "https://picsum.photos/200/200?sig=3"},
        {"pergunta": "Quem é o rei da selva?", "correto": "Leão", "imagem": "https://picsum.photos/200/200?sig=4"},
        {"pergunta": "Quem tem um pescoço bem comprido?", "correto": "Girafa", "imagem": "https://picsum.photos/200/200?sig=5"}
    ]
    
    # Estado inicial
    page.fase_atual = random.randint(0, len(dados_fases) - 1)

    # --- COMPONENTES DE INTERFACE ---
    imagem_exibida = ft.Image(src=dados_fases[page.fase_atual]["imagem"], width=200, height=200)
    pergunta_texto = ft.Text(dados_fases[page.fase_atual]["pergunta"], size=24, weight="bold")
    mensagem_feedback = ft.Text("", size=20)
    entrada_usuario = ft.TextField(label="Sua resposta", width=300, on_submit=lambda e: verificar_resposta())

    # --- FUNÇÃO DE MUDANÇA (CORRETO + PERGUNTA + IMAGEM) ---
    def mudar_para_outro_bicho(e=None):
        # Sorteia até ser um bicho diferente do que está na tela agora
        novo_indice = page.fase_atual
        while novo_indice == page.fase_atual:
            novo_indice = random.randint(0, len(dados_fases) - 1)
        
        page.fase_atual = novo_indice

        # ATUALIZAÇÃO TOTAL: Muda a pergunta, a imagem e a resposta correta internamente
        pergunta_texto.value = dados_fases[page.fase_atual]["pergunta"]
        imagem_exibida.src = dados_fases[page.fase_atual]["imagem"]
        
        # Limpa e reseta a interface
        mensagem_feedback.value = ""
        entrada_usuario.value = ""
        entrada_usuario.disabled = False
        btn_proximo.visible = False
        btn_reiniciar.visible = False
        
        page.update()

    def verificar_resposta(e=None):
        resposta = entrada_usuario.value.strip().lower()
        # A resposta correta sempre será baseada no índice 'page.fase_atual'
        correta = dados_fases[page.fase_atual]["correto"].lower()

        if resposta == correta:
            mensagem_feedback.value = "Correto! 🎉"
            mensagem_feedback.color = ft.Colors.GREEN
            entrada_usuario.disabled = True
            btn_proximo.visible = True
            btn_reiniciar.visible = False
        else:
            mensagem_feedback.value = f"Errado! Era o {dados_fases[page.fase_atual]['correto']}."
            mensagem_feedback.color = ft.Colors.RED
            btn_reiniciar.visible = True # Aparece para mudar de bicho após o erro
            btn_proximo.visible = False
        
        page.update()

    # Botões que disparam a mudança total
    btn_proximo = ft.ElevatedButton("Acertou! Próximo Bicho", on_click=mudar_para_outro_bicho, visible=False)
    btn_reiniciar = ft.ElevatedButton("Jogar Novamente (Mudar Bicho)", on_click=mudar_para_outro_bicho, visible=False, bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE)

    # Adicionando os elementos na página
    page.add(
        pergunta_texto,
        imagem_exibida,
        entrada_usuario,
        ft.ElevatedButton("Verificar", on_click=verificar_resposta),
        mensagem_feedback,
        btn_proximo,
        btn_reiniciar
    )

ft.app(target=main)