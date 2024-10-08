# import flet as ft
#
# def create_side_panel(page: ft.Page):
#     # Боковая панель с кнопками
#     side_panel = ft.Container(
#         content=ft.Column(
#             [
#                 ft.ElevatedButton(text="Button 1"),
#                 ft.ElevatedButton(text="Button 2"),
#                 ft.ElevatedButton(text="Button 3"),
#                 ft.ElevatedButton(text="Button 4"),
#             ],
#             alignment=ft.MainAxisAlignment.START,  # Выравнивание по вертикали (вверху)
#             spacing=10  # Расстояние между кнопками
#         ),
#         width=250,  # Ширина боковой панели
#         padding=10,
#         bgcolor=ft.colors.LIGHT_BLUE_500,  # Фон для наглядности
#         alignment=ft.alignment.center_right,  # Выравнивание по правому краю
#         expand=False,  # Панель не растягивается по горизонтали
#     )
#
#     return side_panel


import flet as ft

def create_side_panel(page: ft.Page):
    # Функция для создания строки ввода данных для каждой планеты
    def create_planet_input(index):
        return ft.Row(
            [
                ft.Text(value=f"Planet {index + 1}:", width=65),
                ft.TextField(label="X", width=60),
                ft.TextField(label="Y", width=60),
                ft.TextField(label="V_x", width=60),
                ft.TextField(label="V_y", width=60),
                ft.TextField(label="Mass", width=60),
            ],
            spacing=5
        )

    # Функция для обновления количества строк ввода данных для планет
    def update_planet_inputs(e):
        num_planets = int(num_planets_field.value)
        planet_inputs_container.controls = [
            create_planet_input(i) for i in range(num_planets)
        ]
        page.update()


    # Контейнер для динамического добавления строк ввода данных для планет
    planet_inputs_container = ft.Column([], spacing=10)

    # Количество планет (по умолчанию 2)
    num_planets_field = ft.TextField(label="Количество планет", value="2", width=200)

    # # Кнопка для обновления количества планет
    # update_button = ft.ElevatedButton(text="Обновить количество планет", on_click=update_planet_inputs)

    # Кнопка для обновления количества строк
    update_planets_button = ft.ElevatedButton(text="Обновить", on_click=None)


    # Разностная схема
    scheme_dropdown = ft.Dropdown(
        label="Выберите разностную схему",
        options=[
            ft.dropdown.Option("Эйлера"),
            ft.dropdown.Option("Верле"),
            ft.dropdown.Option("Эйлера-Крамера"),
            ft.dropdown.Option("Бимана"),
        ],
        width=200
        # expand = True

    )

    # Ввод шага времени и времени моделирования
    time_step_field = ft.TextField(label="Шаг по времени (с)", width=200)
    sim_time_field = ft.TextField(label="Время моделирования (с)", width=200)

    # Контейнер для динамического добавления строк ввода данных для планет
    planet_inputs_container = ft.Column(
        [create_planet_input(i) for i in range(2)],  # По умолчанию 2 планеты
        spacing=10
    )

    # Функция для обновления количества строк ввода данных для планет
    def update_planet_inputs(e):
        try:
            num_planets = int(num_planets_field.value)
            planet_inputs_container.controls = [
                create_planet_input(i) for i in range(num_planets)
            ]
            page.update()
        except ValueError:
            print("Некорректное количество планет")

    # Привязка кнопки к функции обновления
    update_planets_button.on_click = update_planet_inputs

    # Кнопка для подтверждения ввода
    submit_button = ft.ElevatedButton(text="Ввести", on_click=lambda e: print("Данные введены"))

    # Добавляем обработчик для обновления количества строк при изменении числа планет
    num_planets_field.on_change = update_planet_inputs

    # Боковая панель
    side_panel = ft.Container(
        content=ft.Column(
            [
                ft.Text(value="Выберите количество планет:"),
                ft.Row([num_planets_field, update_planets_button], spacing=10), # Поле для количества планет и кнопка "Обновить"

                # ft.Row(
                #     [
                #         ft.Text(value="Выберите количество планет:"),
                #         num_planets_field,  # Поле ввода количества планет
                #         update_planets_button  # Кнопка "Обновить"
                #     ],
                #     spacing=10,
                #     expand=True
                # ),

                # num_planets_field,
                scheme_dropdown,
                time_step_field,
                sim_time_field,
                ft.Text(value="Начальные параметры планет"),
                planet_inputs_container,  # Контейнер для ввода данных планет
                submit_button,
                # ft.ElevatedButton(text="Ввести", on_click=lambda e: print("Данные введены"))

            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10
        ),
        width=None,  # Ширина боковой панели
        padding=10,
        bgcolor=ft.colors.LIGHT_BLUE_800,  # Цвет фона панели
        alignment=ft.alignment.center_right,
        expand=False
    )

    return side_panel
