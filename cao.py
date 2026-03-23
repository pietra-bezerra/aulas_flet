import flet as ft 

def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(
            ft.Text("AU, AU")
        ),
    page.add(ft.Text("Oque o cachorro faz?"),
             ft.Image(src='images/dogs.jpg', height=200),
             ft.Button(
                 content="descubra o som",
                 on_click=mostrar_mensagem
             )
             )
ft.run(main)