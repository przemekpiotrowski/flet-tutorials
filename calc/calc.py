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

    page.add(
        Container(
            width=300,
            content=Column(
                controls=[
                    Row(controls=[result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(text="AC", on_click=do_calc, data="AC"),
                            ElevatedButton(text="+/-", on_click=do_calc, data="+/-"),
                            ElevatedButton(text="%", on_click=do_calc, data="%"),
                            ElevatedButton(text="/", on_click=do_calc, data="/"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="7", on_click=do_calc, data="7"),
                            ElevatedButton(text="8", on_click=do_calc, data="8"),
                            ElevatedButton(text="9", on_click=do_calc, data="9"),
                            ElevatedButton(text="*", on_click=do_calc, data="*"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="4", on_click=do_calc, data="4"),
                            ElevatedButton(text="5", on_click=do_calc, data="5"),
                            ElevatedButton(text="6", on_click=do_calc, data="6"),
                            ElevatedButton(text="-", on_click=do_calc, data="-"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="1", on_click=do_calc, data="1"),
                            ElevatedButton(text="2", on_click=do_calc, data="2"),
                            ElevatedButton(text="3", on_click=do_calc, data="3"),
                            ElevatedButton(text="+", on_click=do_calc, data="+"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="0", on_click=do_calc, data="0", expand=2),
                            ElevatedButton(text=".", on_click=do_calc, data="."),
                            ElevatedButton(text="=", on_click=do_calc, data="="),
                        ]
                    ),
                ]
            ),
        )
    )


flet.app(target=main)
