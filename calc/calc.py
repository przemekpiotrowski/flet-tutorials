import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, colors

BUTTON_REGULAR = 1
BUTTON_GREY = 2
BUTTON_ORANGE = 3


def main(page: Page):
    page.title = "Calc App"
    result = Text(value=float(0), color=colors.WHITE, size=20)

    def do_calc(e):
        if e.data == "AC":
            result.value = float(0)

        elif e.data == "+/-":
            result.value = 0 - float(result.value)

        else:
            try:
                result.value = float(e.data)
            except ValueError:
                result.value = e.data

        result.update()

    def build_button(text, expand=1, type=BUTTON_REGULAR):
        if type == BUTTON_GREY:
            bgcolor = colors.BLUE_GREY_100
            color = colors.BLACK
        elif type == BUTTON_ORANGE:
            bgcolor = colors.ORANGE
            color = colors.WHITE
        else:  # BUTTON_REGULAR
            bgcolor = colors.WHITE24
            color = colors.WHITE

        return ElevatedButton(
            text=text,
            bgcolor=bgcolor,
            color=color,
            expand=expand,
            on_click=do_calc,
            data=text,
        )

    page.add(
        Container(
            width=300,
            bgcolor=colors.BLACK,
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[result], alignment="end"),
                    Row(
                        controls=[
                            build_button("AC", type=BUTTON_GREY),
                            build_button("+/-", type=BUTTON_GREY),
                            build_button("%", type=BUTTON_GREY),
                            build_button("/", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("7"),
                            build_button("8"),
                            build_button("9"),
                            build_button("*", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("4"),
                            build_button("5"),
                            build_button("6"),
                            build_button("-", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("1"),
                            build_button("2"),
                            build_button("3"),
                            build_button("+", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("0", expand=2),
                            build_button("."),
                            build_button("=", type=BUTTON_ORANGE),
                        ]
                    ),
                ]
            ),
        )
    )


flet.app(target=main)
