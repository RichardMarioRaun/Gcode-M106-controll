import customtkinter as ctk
import tkinter.filedialog

#print('vali gcode mida soovid muuta...')
#pathnimi = str(tkinter.filedialog.askopenfile())
#path = pathnimi.split("'")[1]

import tkinter as tk

class CustomButton(ctk.CTkButton):
    def __init__(self, master=None, **kwargs):
        ctk.CTkButton.__init__(self, master, command=self.on_button_press, **kwargs)
        self.default_text = kwargs.get('text', 'Click me!')
        self.set_default_text()

    def on_button_press(self):
        current_text = self.cget('text')
        if current_text == self.default_text:
            new_text = 'Button Pressed!'
        else:
            new_text = self.default_text
        self.configure(text=new_text)

    def set_default_text(self):
        self.configure(text=self.default_text)

# Create the main application window
root = ctk.CTk()
root.title("Custom Button Example")

# Create a custom button
custom_button = CustomButton(root, text="Click me!", width=15)
custom_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()