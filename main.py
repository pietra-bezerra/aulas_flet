import flet as ft
# IMPPORTA A BIBLIOTECA FLET PARA CRIAR UM APILIDO (ALIAS)

def main(page: ft.Page):
    page.title = "Meu primeiro app com Flet" # define o titulo da janela
    page.bgcolor = "blue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Alinha os itens no centro da tela
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER # Alinha os itens no centro da tela
    page.add(
        ft.Text("Bem-vindo ao meu app!"),
        ft.Text("Aqui você pode criar o que quiser!!")
    )

ft.run(main)