import flet as ft
import random # Importante para o sorteio

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # 1. Lista de opções possíveis
    opcoes = ["Cachorro", "Peixe", "Gato"]
    
    # Variável que guardará o objetivo da rodada atual
    # Usamos uma lista de um item para poder alterá-la dentro das funções
    estado = {"correto": random.choice(opcoes)}

    # Texto para feedback
    mensagem = ft.Text(
        f"Qual é o {estado['correto']}?",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        
        if imagem_selecionada == estado["correto"]:
            e.control.bgcolor = ft.Colors.GREEN_200
            e.control.image.opacity = 0.3
            e.control.content.value = "👍"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou."
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "👎"
            e.control.content.size = 40
            mensagem.value = f"Ops! Não era o {estado['correto']}. Tente de novo."
        
        # Desativa cliques após jogar
        container_gato.on_click = None
        container_cachorro.on_click = None
        container_peixe.on_click = None
        btn_jogar_novamente.visible = True
        page.update()
    
    # Função Jogar Novamente (Muda o bicho sorteado)
    def jogar_novamente(e):
        # Sorteia um novo objetivo
        estado["correto"] = random.choice(opcoes)
        
        btn_jogar_novamente.visible = False
        mensagem.value = f"Qual é o {estado['correto']}?"

        # Reset Gato
        container_gato.image.opacity = 1.0
        container_gato.bgcolor = ft.Colors.GREY_200
        container_gato.on_click = jogar
        container_gato.content.size = 0
        container_gato.content.value = "Gato"

        # Reset Cachorro
        container_cachorro.image.opacity = 1.0
        container_cachorro.bgcolor = ft.Colors.GREY_200
        container_cachorro.on_click = jogar
        container_cachorro.content.size = 0
        container_cachorro.content.value = "Cachorro"
        
        # Reset Peixe
        container_peixe.image.opacity = 1.0
        container_peixe.bgcolor = ft.Colors.GREY_200
        container_peixe.on_click = jogar
        container_peixe.content.size = 0
        container_peixe.content.value = "Peixe"
        
        page.update()

    # --- Containers ---
    container_gato = ft.Container(
        content=ft.Text("Gato", size=0),
        image=ft.DecorationImage(src="images/gato.webp", fit=ft.BoxFit.COVER),
        width=120, height=120, margin=10, bgcolor=ft.Colors.GREY_200,
        border_radius=10, alignment=ft.Alignment(0, 0), ink=True, on_click=jogar
    )

    container_cachorro = ft.Container(
        content=ft.Text("Cachorro", size=0),
        image=ft.DecorationImage(src="images/cachorro.webp", fit=ft.BoxFit.COVER),
        width=120, height=120, margin=10, bgcolor=ft.Colors.GREY_200,
        border_radius=10, alignment=ft.Alignment(0, 0), ink=True, on_click=jogar
    )

    container_peixe = ft.Container(
        content=ft.Text("Peixe", size=0),
        image=ft.DecorationImage(src="images/peixe.webp", fit=ft.BoxFit.COVER),
        width=120, height=120, margin=10, bgcolor=ft.Colors.GREY_200,
        border_radius=10, alignment=ft.Alignment(0, 0), ink=True, on_click=jogar
    )

    btn_jogar_novamente = ft.ElevatedButton(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text("Selecione a imagem certa", size=24, weight="bold"),
                mensagem,
                ft.Row(
                    [container_gato, container_cachorro, container_peixe],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)