import flet as ft

def main(page: ft.Page):
    def clicou(e):
        page.add(
            ft.Text(f"Clicou no container: {e.control.content.value}")
        )

        page.scroll= ft.ScrollMode.AUTO


    page.add(
      ft.Row(
        [
            ft.Container(
                content=ft.Text("Container com padding, margin e borda"),
                bgcolor=ft.Colors.AMBER,
                padding=10,
                margin=10,
                border_radius=10,
                width=150,
                height=150,
                alignment=ft.Alignment(0,0)
               ),
            ft.Container(
                content=ft.Text("Container não Clicável"),
                bgcolor=ft.Colors.GREEN_200,
                padding=10,
                margin=10,
                border_radius=10,
                width=150,
                height=150,
                alignment=ft.Alignment(0,0),
                on_click=clicou,
               ),
            ft.Container(
                content=ft.Text("Container Clicável"),
                bgcolor=ft.Colors.TRANSPARENT,
                padding=10,
                margin=10,
                border_radius=10,
                width=150,
                height=150,
                alignment=ft.Alignment(0,0),
                on_click=clicou,
               ),
            ],
            scroll=ft.ScrollMode.ALWAYS
        )
    )


ft.run(main)