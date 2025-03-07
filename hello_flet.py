import flet as ft

def main(page):
    '''
    This function is the entry point for the Flet application.

    Args:
        page (ft.Page): The Flet page object representing the application window.
    '''
    # Add a Text control to the page.
    # The Text control displays the string "Hello, Flet!" on the screen.
    page.add(ft.Text("Hello, Flet!"))

# Start the Flet application.
# The `target` argument specifies the main function that will be executed when the application starts.
ft.app(target=main)

'''
Key points:
- flet.app(): This is the main function to start the Flet application.
              You pass it a function (like main()) that defines the layout and logic of your app.
- page.add(): This adds widgets (UI elements) to the page.
              In this example, we are adding a simple Text widget that says "Hello, Flet!".
- ft.Text(): This creates a text widget.
             You can customize the text with different properties like size, color, and alignment.
'''