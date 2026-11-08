# ----- Module Imports -----
import math

import flet as ft


# ----- Main Function -----
def main(page: ft.Page):
    page.title = "My Calculator v0.1"
    page.window.width = 350
    page.window.height = 450
    page.window.center()
    page.window.maximizable = False
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.DARK

    def handle_button_click(e):
        value = e.control.data

        if value in "123456789" and len(value) == 1:
            if display.value == "0":
                display.value = value
            else:
                display.value += value

        elif value == "0":
            if display.value != "0":
                display.value += "0"

        elif value == "c":
            display.value = "0"

        elif value == "del":
            display.value = display.value[:-1] or "0"

        elif value in ["+", "-", "*", "/"]:
            if display.value and display.value[-1] not in ["+", "-", "*", "/"]:
                display.value += value

        elif value == "=":
            if display.value and display.value[-1] in ["+", "-", "*", "/"]:
                display.value = "Please enter the next number."
            else:
                try:
                    # Only calculator arithmetic expressions are evaluated.
                    result = eval(display.value, {"__builtins__": {}}, {})
                    display.value = str(result)
                except ZeroDivisionError:
                    display.value = "Cannot divide by zero."
                except (SyntaxError, NameError, TypeError, ValueError):
                    display.value = "Invalid expression."

        elif value == "fac":
            try:
                number = int(display.value)
                if number < 0:
                    display.value = "Factorial requires a non-negative number."
                else:
                    display.value = str(math.factorial(number))
            except ValueError:
                display.value = "Factorial requires an integer."

        elif value == "sqrt":
            try:
                number = float(display.value)
                if number < 0:
                    display.value = "Cannot calculate square root of a negative number."
                else:
                    display.value = str(math.sqrt(number))
            except ValueError:
                display.value = "Invalid number."

        elif value == "pow":
            if display.value and display.value[-1] not in ["+", "-", "*", "/", "*"]:
                display.value += "**"

        page.update()

    # Display
    display = ft.TextField(
        value="0",
        read_only=True,
        bgcolor="#1B1D2B",
        color="#FFFFFF",
    )
    row0 = ft.Row(
        controls=[display],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Row 1
    b7 = ft.ElevatedButton(text="7", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="7")
    b8 = ft.ElevatedButton(text="8", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="8")
    b9 = ft.ElevatedButton(text="9", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="9")
    bplus = ft.ElevatedButton(text="+", bgcolor="#6548C8", color="#050505", width=65, height=55, on_click=handle_button_click, data="+")
    row1 = ft.Row(controls=[b7, b8, b9, bplus], alignment=ft.MainAxisAlignment.CENTER)

    # Row 2
    b4 = ft.ElevatedButton(text="4", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="4")
    b5 = ft.ElevatedButton(text="5", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="5")
    b6 = ft.ElevatedButton(text="6", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="6")
    bmin = ft.ElevatedButton(text="-", bgcolor="#6548C8", color="#050505", width=65, height=55, on_click=handle_button_click, data="-")
    row2 = ft.Row(controls=[b4, b5, b6, bmin], alignment=ft.MainAxisAlignment.CENTER)

    # Row 3
    b1 = ft.ElevatedButton(text="1", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="1")
    b2 = ft.ElevatedButton(text="2", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="2")
    b3 = ft.ElevatedButton(text="3", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="3")
    bmul = ft.ElevatedButton(text="*", bgcolor="#6548C8", color="#050505", width=65, height=55, on_click=handle_button_click, data="*")
    row3 = ft.Row(controls=[b1, b2, b3, bmul], alignment=ft.MainAxisAlignment.CENTER)

    # Row 4
    bclear = ft.ElevatedButton(text="C", bgcolor="#E8435B", color="#050505", width=65, height=55, on_click=handle_button_click, data="c")
    b0 = ft.ElevatedButton(text="0", bgcolor="#292B3C", color="#FFFFFF", width=65, height=55, on_click=handle_button_click, data="0")
    bequal = ft.ElevatedButton(text="=", bgcolor="#00A98F", color="#050505", width=65, height=55, on_click=handle_button_click, data="=")
    bdiv = ft.ElevatedButton(text="/", bgcolor="#6548C8", color="#050505", width=65, height=55, on_click=handle_button_click, data="/")
    row4 = ft.Row(controls=[bclear, b0, bequal, bdiv], alignment=ft.MainAxisAlignment.CENTER)

    # Row 5
    bbackspace = ft.ElevatedButton(text="<--", bgcolor="#E5A52A", color="#050505", width=65, height=55, on_click=handle_button_click, data="del")
    bfactorial = ft.ElevatedButton(text="n!", bgcolor="#087F83", color="#050505", width=65, height=55, on_click=handle_button_click, data="fac")
    bsqrt = ft.ElevatedButton(text="SQRT", bgcolor="#087F83", color="#050505", width=65, height=55, on_click=handle_button_click, data="sqrt")
    bpower = ft.ElevatedButton(text="**", bgcolor="#087F83", color="#050505", width=65, height=55, on_click=handle_button_click, data="pow")
    row5 = ft.Row(controls=[bbackspace, bfactorial, bsqrt, bpower], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row0, row1, row2, row3, row4, row5)
    page.update()


ft.app(main)
