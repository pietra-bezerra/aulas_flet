import flet as ft


def main(page: ft.Page):
    # Configurações da janela
    page.title = "Gamer Card"
    page.bgcolor = "1e1e1e"
    page.horizontal_aligment = ft.CrossAxisAlignment.CENTER
    page.vertical_aligment = ft.MainAxisAlignment.CENTER

    # Cabeçalho:Avatar(emoji) e nome do lado

    cabecalho = ft.Row(
        controls=[
            ft.Text("👻", size=60),  # emoji a prova de erros
            ft.Column(
                controls=[
                    ft.Text("Murta", size=24,
                            weight="bold", color="white"),
                    ft.Text("Nível 72 - Furtivo",
                            size=24, color="grey300"),
                ], spacing=2
            )

        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # status: Barra de hp, mp e xp

    status_bar = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(
                    "Hp: 100", text_align=ft.TextAlign.CENTER, weight="bold"),
                bgcolor="red400", padding=10, border_radius=8, expand=4
            ),
            ft.Container(
                content=ft.Text(
                    "XP: 9999", text_align=ft.TextAlign.CENTER, weight="bold"),
                bgcolor="amber400", padding=10, border_radius=8, expand=2
            ),
        ],
        spacing=10
    )

    #BOTÕES: Ações do jogador
    botões_acao = ft.Row(
        controls=[
            ft.Button(
                content="Adicionar Amigo",
                bgcolor="#36628e",
                color="white"
            ),
            ft.Button(
                content="Disputar",
                bgcolor="red",
                color="white"
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20 
    )

    #CARTÃO PRINCIPAL   
    cartao = ft.Container(
        content=ft.Column(
            controls=[cabecalho,status_bar,botões_acao],
            spacing=30
        ),
        bgcolor='#2e2e2e',
        padding=40,
        border_radius=15,
        width=450,
        shadow=ft.BoxShadow(blur_radius=20, color="black") #aqui vai ser um efeito de sombra 
    )

    page.add(cartao)

ft.run(main)