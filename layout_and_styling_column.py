import flet as ft

def main(page):
    '''
    This function defines the main structure of the Flet application.

    Args:
        page (ft.Page): The Flet page object representing the application window.
    '''

    # Add a Column layout to the page.
    # The Column layout will arrange its child controls vertically.
    page.add(
        ft.Column(
            [
                # Add a Text control to the Column.
                # This Text control displays the message "Welcome to Flet!".
                ft.Text("Welcome to Flet!"),

                # Add an ElevatedButton control to the Column.
                # This button has the label "Click Me".
                # The on_click parameter defines an event handler that's triggered when the button is clicked.
                # The lambda function creates an anonymous function that captures the click event.
                # When clicked, the lambda function adds a new Text control to the page, displaying "You clicked the button!".
                ft.ElevatedButton(
                    text="Click Me",
                    on_click=lambda e: page.add(ft.Text("You clicked the button!"))
                ),
            ]
        )
    )

# Start the Flet application.
# The `target` argument specifies the main function that will be executed when the application starts.
ft.app(target=main)
