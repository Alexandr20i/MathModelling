import flet as ft

def create_header(page: ft.Page):
    return ft.Container(
        content=ft.Row(
            [
                ft.TextButton("Начать"),  # Кнопка "Начать"
                ft.TextButton("Закрыть"),  # Кнопка "Закрыть"
                ft.TextButton("Настройки", on_click=lambda e: print("Настройки")),
                ft.TextButton("Помощь", on_click=lambda e: print("Помощь")),
                ft.TextButton("О программе", on_click=lambda e: print("О программе"))
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,  # Размещаем кнопки равномерно по ширине
            expand=True  # Делаем панель адаптивной
        ),
        padding=0,      # Убираем отступы
        margin=0,       # Убираем поля
        bgcolor=ft.colors.BLUE_800,  # Пример фона для верхней панели
    )