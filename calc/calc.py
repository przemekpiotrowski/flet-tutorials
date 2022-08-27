import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text


def main(page: Page):
    page.title = "Calc App"
    result = Text(value="0")

    page.add(
        Container(
            width=300,
            content=Column(
                controls=[
                    Row(controls=[result], alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(text="AC"),
                            ElevatedButton(text="+/-"),
                            ElevatedButton(text="%"),
                            ElevatedButton(text="/"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="7"),
                            ElevatedButton(text="8"),
                            ElevatedButton(text="9"),
                            ElevatedButton(text="*"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="4"),
                            ElevatedButton(text="5"),
                            ElevatedButton(text="6"),
                            ElevatedButton(text="-"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="1"),
                            ElevatedButton(text="2"),
                            ElevatedButton(text="3"),
                            ElevatedButton(text="+"),
                        ]
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="0", expand=2),
                            ElevatedButton(text="."),
                            ElevatedButton(text="="),
                        ]
                    ),
                ]
            ),
        )
    )


flet.app(target=main)
