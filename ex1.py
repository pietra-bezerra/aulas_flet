import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Text("Container com padding, margin e borda"),
            bgcolor="lightblue",
            padding=20,
            margin=15,
            border=ft.Border(
                top=ft.BorderSide(3, ft.Colors.BLACK),
                right=ft.BorderSide(3, ft.Colors.BLACK),
                bottom=ft.BorderSide(3, ft.Colors.BLACK),
                left=ft.BorderSide(3, ft.Colors.BLACK)
            ),
            border_radius=10,
            width=300,
            height=100
        )
    )

ft.run(main)