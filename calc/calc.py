import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, colors

BUTTON_REGULAR = 1
BUTTON_GREY = 2
BUTTON_ORANGE = 3


class CalculatorApp(UserControl):
    def do_calc(self, e):
        if e.data == "AC":
            self.result.value = float(0)

        elif e.data == "+/-":
            self.result.value = 0 - float(self.result.value)

        else:
            try:
                self.result.value = float(e.data)
            except ValueError:
                self.result.value = e.data

        self.result.update()

    def build_button(self, text, expand=1, type=BUTTON_REGULAR):
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
            on_click=self.do_calc,
            data=text,
        )

    def build(self):
        self.result = Text(value=float(0), color=colors.WHITE, size=20)

        return Container(
            width=300,
            bgcolor=colors.BLACK,
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(
                        controls=[
                            self.build_button("AC", type=BUTTON_GREY),
                            self.build_button("+/-", type=BUTTON_GREY),
                            self.build_button("%", type=BUTTON_GREY),
                            self.build_button("/", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            self.build_button("7"),
                            self.build_button("8"),
                            self.build_button("9"),
                            self.build_button("*", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            self.build_button("4"),
                            self.build_button("5"),
                            self.build_button("6"),
                            self.build_button("-", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            self.build_button("1"),
                            self.build_button("2"),
                            self.build_button("3"),
                            self.build_button("+", type=BUTTON_ORANGE),
                        ]
                    ),
                    Row(
                        controls=[
                            self.build_button("0", expand=2),
                            self.build_button("."),
                            self.build_button("=", type=BUTTON_ORANGE),
                        ]
                    ),
                ]
            ),
        )


def main(page: Page):
    page.title = "Calc App"

    page.add(CalculatorApp())
    # page.add(CalculatorApp())


flet.app(target=main)
