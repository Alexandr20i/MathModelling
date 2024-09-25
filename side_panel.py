import flet as ft

def create_side_panel(page: ft.Page):
    return ft.Column(
        [
            ft.TextButton("Кнопка 1", on_click=lambda e: print("Кнопка 1")),
            ft.TextButton("Кнопка 2", on_click=lambda e: print("Кнопка 2")),
            ft.TextButton("Кнопка 3", on_click=lambda e: print("Кнопка 3")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True  # Панель займет всю вертикальную зону
    )