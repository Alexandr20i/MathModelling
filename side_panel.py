import flet as ft

# from main import run_simulation


def create_side_panel(page: ft.Page):
    # Функция для создания строки ввода данных для каждой планеты
    def create_planet_input(index):
        return ft.Row(
            [
                ft.Text(value=f"Planet {index + 1}:", width=65),
                ft.TextField(label="X", width=50),
                ft.TextField(label="Y", width=50),
                ft.TextField(label="V_x", width=55),
                ft.TextField(label="V_y", width=55),
                ft.TextField(label="Mass", width=70),
            ],
            spacing=5
        )

    # Количество планет (по умолчанию 2)
    num_planets_field = ft.TextField(label="Количество планет", value="2", width=200)

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
            print("корректное количество планет")
        except ValueError:
            print("Некорректное количество планет")


    def validate_inputs(e):
        valid = True

        if num_planets_field.value is None or num_planets_field.value == "" or num_planets_field.value == "0":
            num_planets_field.border_color = "red"
            valid = False
        else:
            num_planets_field.border_color = "black"

        # Проверка поля "разностная схема"
        if scheme_dropdown.value is None or scheme_dropdown.value == "":
            scheme_dropdown.border_color = "red"
            valid = False
        else:
            scheme_dropdown.border_color = "black"

        # Проверка поля "шаг по времени"
        if time_step_field.value == "" or time_step_field.value is None:
            time_step_field.border_color = "red"
            valid = False
        else:
            time_step_field.border_color = "black"

        # Проверка поля "время моделирования"
        if sim_time_field.value == "" or sim_time_field.value is None:
            sim_time_field.border_color = "red"
            valid = False
        else:
            sim_time_field.border_color = "black"

        # Проверка каждого поля ввода для планет
        for control in planet_inputs_container.controls:
            for field in control.controls[1:]:
                if field.value == "" or field.value is None:
                    field.border_color = "red"
                    valid = False
                else:
                    field.border_color = "black"

        # Если есть незаполненные поля, показать ошибку
        if not valid:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Ошибка"),
                content=ft.Text("Заполните все поля!")
            )
            page.dialog.open = True

        # else:
        #     run_simulation(page, num_planets_field.value, scheme_dropdown.value)

        page.update()

    # Кнопка для подтверждения ввода
    submit_button = ft.ElevatedButton(
        text="Ввести",
        on_click=lambda e: validate_inputs(e)
    )

    # Кнопка для подтверждения ввода
    submit_button = ft.ElevatedButton(text="Ввести", on_click=validate_inputs)
    # submit_button = ft.ElevatedButton(
    #     text="Ввести",
    #     on_click=lambda e: run_simulation(scheme_dropdown.value, positions, velocities, accelerations,
    #                                       prev_accelerations, dt)
    # )

    # # Добавляем обработчик для обновления количества строк при изменении числа планет
    num_planets_field.on_change = update_planet_inputs

    # Боковая панель
    side_panel = ft.Container(
        content=ft.Column(
            [
                ft.Text(value="Выберите количество планет:"),
                num_planets_field,
                scheme_dropdown,
                time_step_field,
                sim_time_field,
                ft.Text(value="Начальные параметры планет"),
                planet_inputs_container,  # Контейнер для ввода данных планет
                submit_button
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
