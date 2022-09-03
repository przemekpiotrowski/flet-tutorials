import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, colors

BUTTON_REGULAR = 1
BUTTON_GREY = 2
BUTTON_ORANGE = 3


class CalculatorApp(UserControl):
    def reset_calc_state(self):
        self.start_new_number = True

    def do_calc(self, e):
        data = e.control.data

        if data == "AC":
            self.result.value = "0"
            self.reset_calc_state()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            if self.result.value == "0" or self.start_new_number is True:
                self.result.value = data
                self.start_new_number = False
            else:
                self.result.value = self.result.value + data

        elif data == ".":
            if self.result.value == "0" or self.start_new_number is True:
                self.result.value = "0" + data
                self.start_new_number = False
            else:
                try:
                    if float(self.result.value + data):
                        self.result.value = self.result.value + data
                except ValueError:
                    pass

        elif data == "%":
            self.result.value = self.format_number(float(self.result.value) / 100)
            self.reset_calc_state()

        elif data == "+/-":
            self.result.value = self.format_number(0 - float(self.result.value))

        else:
            self.result.value = f"TODO: {data}"
            self.reset_calc_state()

        self.result.update()

    def format_number(self, number):
        if number % 1 == 0:
            number = int(number)

        return str(number)

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
        self.result = Text(value="0", color=colors.WHITE, size=20)
        self.reset_calc_state()

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
