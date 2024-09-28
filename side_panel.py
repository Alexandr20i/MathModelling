import flet as ft

def create_side_panel(page: ft.Page):
    # Боковая панель с кнопками
    side_panel = ft.Container(
        content=ft.Column(
            [
                ft.ElevatedButton(text="Button 1"),
                ft.ElevatedButton(text="Button 2"),
                ft.ElevatedButton(text="Button 3"),
                ft.ElevatedButton(text="Button 4"),
            ],
            alignment=ft.MainAxisAlignment.START,  # Выравнивание по вертикали (вверху)
            spacing=10  # Расстояние между кнопками
        ),
        width=250,  # Ширина боковой панели
        padding=10,
        bgcolor=ft.colors.LIGHT_BLUE_500,  # Фон для наглядности
        alignment=ft.alignment.center_right,  # Выравнивание по правому краю
        expand=False,  # Панель не растягивается по горизонтали
    )

    return side_panel
