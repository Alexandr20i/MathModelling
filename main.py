import flet as ft
from header_view import create_header
from side_panel import create_side_panel
from animations import create_animation_view
from razn_schemes import beeman, euler, werle, euler_kramer

def main(page: ft.Page):
    page.title = "Space Simulation"
    page.theme_color = "Blue"

    # Установка адаптивного выравнивания
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    # Создание верхней панели
    header = create_header(page)

    # Центральная область для анимации
    animation_view, start_animation, close_animation = create_animation_view(page)

    # Боковая панель с кнопками
    side_panel = create_side_panel(page)

    # Добавляем элементы на страницу
    page.add(
        ft.Column(
            [
                header,  # Верхняя панель
                ft.Row(
                    [
                        ft.Container(
                            animation_view,  # Центральная анимация
                            expand=True,  # Центральный блок занимает всё доступное пространство
                        ),
                        side_panel  # Боковая панель справа
                    ],
                    expand=True,  # Растягиваем строку на всю ширину
                    alignment=ft.MainAxisAlignment.START,  # Расположение сверху
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH  # Панель растягивается по высоте
                ),
            ],
            expand=True
        )
    )

    # Привязываем функции анимации к кнопке "Начать"
    header.content.controls[0].on_click = lambda e:  start_animation()  # Кнопка "Начать"

    # Привязываем функцию закрытия анимации
    header.content.controls[1].on_click = lambda e: close_animation()  # Первая кнопка в шапке для закрытия анимации

    # Устанавливаем адаптивное поведение для всего
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=None, port=44051)


