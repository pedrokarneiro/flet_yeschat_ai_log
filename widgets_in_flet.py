import flet as ft

def main(page):
    '''
    This function creates a simple Flet application with a text input and a button.

    Args:
        page (ft.Page): The Flet page object representing the application window.
    '''

    # Create a TextBox control for user input.
    text_box = ft.TextField(label="Enter your name")
    # The label parameter adds a descriptive label to the text input field.

    # Create a Button control.
    button = ft.ElevatedButton(text="Say Hello",
                       on_click=lambda e: page.add(ft.Text(f"Hello, {text_box.value}!")))
    # The text parameter sets the button's label.
    # The on_click parameter defines an event handler that's triggered when the button is clicked.
    # The lambda function creates an anonymous function that captures the text_box's current value.
    # When clicked, the lambda function adds a Text control to the page, displaying "Hello, [user input]!".
    # text_box.value retrieves the text entered by the user.

    # Add the TextBox and Button controls to the page.
    page.add(text_box, button)
    # The page.add method adds the specified controls to the application's user interface.

ft.app(target=main)
# Starts the Flet application, executing the main function to build the UI.

'''
Key points:
- TextField: The TextField widget allows users to type something in it.
             You can access the text using the .value attribute.
- Button with on_click: The `Button` widget triggers an event (like clicking) and calls a function,
                        where you can define the behavior you want (in this case,
                        showing a personalized greeting).
'''
