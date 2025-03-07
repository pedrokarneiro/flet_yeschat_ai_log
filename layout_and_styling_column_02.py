import flet as ft

def main(page: ft.Page):
    """
    A simple Flet app demonstrating the use of Column layout.
    """

    # Set the title of the application window.
    page.title = "Flet Column Example"

    # Create three Text controls, each with a different label and font size.
    text1 = ft.Text("Item 1", size=20)  # Creates a Text control displaying "Item 1" with size 20.
    text2 = ft.Text("Item 2", size=20)  # Creates a Text control displaying "Item 2" with size 20.
    text3 = ft.Text("Item 3", size=20)  # Creates a Text control displaying "Item 3" with size 20.

    # Create a Column layout and add the Text controls to it.
    # The Column layout arranges its child controls vertically.
    column = ft.Column(controls=[text1, text2, text3])

    # Add the Column layout to the page, making it visible in the application window.
    page.add(column)

# Start the Flet application.
# The `target` argument specifies the main function that will be executed when the application starts.
ft.app(target=main)