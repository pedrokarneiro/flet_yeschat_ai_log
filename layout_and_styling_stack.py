import flet as ft

def main(page: ft.Page):
    '''
    A simple Flet app demonstrating the use of Stack layout.
    '''

    # Set the title of the application window.
    page.title = "Flet Stack Example"

    # Create the first rectangle (Container) as the base layer.
    rect1 = ft.Container(
        width=150,  # Set the width of the rectangle to 150 pixels.
        height=150, # Set the height of the rectangle to 150 pixels.
        bgcolor=ft.colors.BLUE, # Set the background color of the rectangle to blue.
    )

    # Create the second rectangle (Container) to be placed on top of the first.
    rect2 = ft.Container(
        width=100,  # Set the width of the rectangle to 100 pixels.
        height=100, # Set the height of the rectangle to 100 pixels.
        bgcolor=ft.colors.RED, # Set the background color of the rectangle to red.
        top=50,     # Position the top edge of the rectangle 50 pixels from the top of the Stack.
        left=50,    # Position the left edge of the rectangle 50 pixels from the left of the Stack.
    )

    # Create a Stack layout and add the two rectangles to it.
    # The Stack layout will place the rectangles on top of each other,
    # with rect2 appearing on top of rect1 due to the order in the controls list.
    stack = ft.Stack(controls=[rect1, rect2])

    # Add the Stack layout to the page, making it visible in the application window.
    page.add(stack)

# Start the Flet application.
# The `target` argument specifies the main function that will be executed when the application starts.
ft.app(target=main)