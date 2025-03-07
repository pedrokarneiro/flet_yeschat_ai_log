import flet as ft

def main(page: ft.Page):
    '''
    A simple Flet app demonstrating the use of Container layout.
    '''

    # Set the title of the application window.
    page.title = "Flet Container Example"

    # Create a Container with specified properties.
    container = ft.Container(
        # Set the content of the Container to a Text control.
        # The Text control displays "Hello, Container!" with a font size of 20.
        content=ft.Text("Hello, Container!", size=20),

        # Set the width of the Container to 200 pixels.
        width=200,

        # Set the height of the Container to 100 pixels.
        height=100,

        # Set the background color of the Container to light blue (200 shade).
        bgcolor=ft.colors.LIGHT_BLUE_200,

        # Add 20 pixels of padding around the content within the Container.
        padding=20,

        # Align the content to the center of the Container.
        alignment=ft.alignment.center,

        # Add a blue border to the Container with a width of 2 pixels.
        border=ft.border.all(2, ft.colors.BLUE),

        # Round the corners of the Container with a radius of 10 pixels.
        border_radius=10,
    )

    # Add the created Container to the page, making it visible in the application window.
    page.add(container)

# Start the Flet application.
# The `target` argument specifies the main function that will be executed when the application starts.
ft.app(target=main)