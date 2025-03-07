import flet as ft

def main(page):
    '''
    This function creates a simple Flet application with a text element and a button.
    Clicking the button changes the text element's value.
    '''

    # Create a Text control with an initial message.
    text = ft.Text("Click the button to change me!")

    def change_text(e):
        '''
        This function is called when the button is clicked.
        It changes the value of the Text control and updates the page.

        Args:
            e: The event object (not used in this case).
        '''
        # Change the value of the Text control.
        text.value = "You changed the text!"
        # Update the page to reflect the change.
        page.update()

    # Create a Button control with a label and an event handler.
    button = ft.ElevatedButton(text="Change Text", on_click=change_text)

    # Add the Text and Button controls to the page.
    page.add(text, button)

# Start the Flet application, executing the main function to build the UI.
ft.app(target=main)
