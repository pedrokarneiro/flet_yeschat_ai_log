import flet as ft

def main(page: ft.Page):
    """
    A simple Flet app demonstrating the use of Row layout.
    """

    # Set the title of the application window.
    page.title = "Flet Row Example"

    # Create three Text controls, each with a different label and font size.
    text1 = ft.Text("Item 1", size=20)  # Creates a Text control displaying "Item 1" with size 20.
    text2 = ft.Text("Item 2", size=20)  # Creates a Text control displaying "Item 2" with size 20.
    text3 = ft.Text("Item 3", size=20)  # Creates a Text control displaying "Item 3" with size 20.

    # Create a Row layout and add the Text controls to it.
    # The Row layout arranges its child controls horizontally.
    row = ft.Row(controls=[text1, text2, text3])

    # Add the Row layout to the page, making it visible in the application window.
    page.add(row)

# Start the Flet application.
# The `target` argument specifies the main function that will be executed when the application starts.
ft.app(target=main)