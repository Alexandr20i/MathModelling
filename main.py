import flet as ft
import numpy as np
from header_view import create_header
from side_panel import create_side_panel
from animations import create_animation_view
from razn_schemes.beeman import beeman_method
from razn_schemes.euler import euler_method
from razn_schemes.euler_kramer import euler_cromer_method
from razn_schemes.werle import verlet_method

# Выбор схемы и запуск симуляции
# def run_simulation(scheme, positions, velocities, masses, dt):
#     accelerations = calculate_accelerations(positions, masses)
#     prev_accelerations = np.copy(accelerations)
#
#     if scheme == "Эйлера":
#         return euler_method(positions, velocities, accelerations, dt)
#     elif scheme == "Эйлера-Кромера":
#         return euler_cromer_method(positions, velocities, accelerations, dt)
#     elif scheme == "Верле":
#         return verlet_method(positions, velocities, accelerations, dt)
#     elif scheme == "Бимана":
#         return beeman_method(positions, velocities, accelerations, prev_accelerations, dt)

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


