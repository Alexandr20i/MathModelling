import flet as ft

def create_animation_view(page: ft.Page):
    # Контейнер для анимации
    central_view = ft.Container(
        content=ft.Column(
            [
                ft.Text("Приветствую!", size=30, color=ft.colors.WHITE),
                # Другие компоненты могут быть добавлены здесь
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLUE_600,  # Фоновый цвет
        border_radius=ft.border_radius.all(20),
        opacity=0,  # Изначально прозрачное
        animate_opacity=500,  # Настройка анимации появления
        animate_size=300       # Настройка анимации масштабирования
    )

    def start_animation():
        central_view.opacity = 1  # Анимация появления
        central_view.scale = 1     # Масштабирование
        central_view.update()

    def close_animation():
        central_view.opacity = 0  # Закрытие анимационного окна
        central_view.scale = 1   # Можно изменить на необходимое значение
        central_view.update()

    return central_view, start_animation, close_animation  # Возвращаем центральное окно и функции анимации