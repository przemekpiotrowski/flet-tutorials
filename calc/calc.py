import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text


def main(page: Page):
    page.title = "Calc App"
    result = Text(value="0")

    def do_calc(e):
        if e.data == "AC":
            result.value = "0"
        else:
            result.value = e.data

        result.update()

    def build_button(text, expand=1):
        return ElevatedButton(
            text=text,
            expand=expand,
            on_click=do_calc,
            data=text,
        )

    page.add(
        Container(
            width=300,
            content=Column(
                controls=[
                    Row(controls=[result], alignment="end"),
                    Row(
                        controls=[
                            build_button("AC"),
                            build_button("+/-"),
                            build_button("%"),
                            build_button("/"),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("7"),
                            build_button("8"),
                            build_button("9"),
                            build_button("*"),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("4"),
                            build_button("5"),
                            build_button("6"),
                            build_button("-"),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("1"),
                            build_button("2"),
                            build_button("3"),
                            build_button("+"),
                        ]
                    ),
                    Row(
                        controls=[
                            build_button("0", expand=2),
                            build_button("."),
                            build_button("="),
                        ]
                    ),
                ]
            ),
        )
    )


flet.app(target=main)
