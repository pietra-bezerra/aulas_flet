import flet as ft
def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Eu vou ser o rei dos piratas.")
        ),
    page.add(ft.Text("Olá meu nome é Monkey D. Luffy!"),
             ft.Image(src="images/luffy.png", height=200),
             ft.Button(
                 content="Clique aqui",
                 on_click=mostrar_mensagem
             )
             )
ft.run(main)