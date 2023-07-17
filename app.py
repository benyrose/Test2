# Import necessary modules
import tkinter as tk

# Create a class for your app
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")
        
        # Create and configure your GUI elements
        self.label = tk.Label(root, text="Welcome to My App!")
        self.label.pack()
        
        self.button = tk.Button(root, text="Click Me", command=self.button_click)
        self.button.pack()
        
    def button_click(self):
        # Define the functionality when the button is clicked
        self.label.config(text="Button clicked!")

# Create the main application window
root = tk.Tk()

# Create an instance of your app class
app = MyApp(root)

# Start the application event loop
root.mainloop()
