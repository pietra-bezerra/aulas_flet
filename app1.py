import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Text("Bem-Vindo ao meu app!!"),
        ft.Text("Este é um texto menor", size=16, color="blue")
    )

    def botao_clicado(e):
        page.add(
            ft.Text("Você clicou no botão!")
        )
    page.add(
        ft.Button(
            content="Botão simples",
            on_click=botao_clicado
        ),
        ft.Button(
            content="Botão colorido",
            bgcolor="blue",
            color="white",
            on_click=botao_clicado
        ),
        ft.Button(
            content="Botão desativado",
            disabled=True,
            on_click=botao_clicado
        ),
        ft.Button(
            content="Botão com ícone",
            icon=ft.Icons.SAVE,
            icon_color=ft.Colors.BLUE_800,
            on_click=botao_clicado
        )

    ),
    page.add(
        ft.Image(
            src="https://www.sp.senai.br/images/senai.svg",
            width=150,
            height=150
        )
    )


ft.run(main)