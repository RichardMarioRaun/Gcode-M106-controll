import customtkinter as ctk
import tkinter.filedialog

#print('vali gcode mida soovid muuta...')
#pathnimi = str(tkinter.filedialog.askopenfile())
#path = pathnimi.split("'")[1]

def button_callback():
    print("button clicked")

app = ctk.CTk()
app.geometry("400x150")

r = ['a', 'b', 'c', 'd']
y = [1, 2, 3, 4]

for rida in r:
    f = ctk.CTkFrame(app)
    for nr in y:
        e = ctk.CTkLabel(f, text=f'{rida} {nr}')
        e.pack(padx=5, pady=5, side='left')
    f.pack(pady=5)

button = ctk.CTkButton(app, text="my button", command= y[0] = 4)
button.pack(padx=20, pady=20)

app.mainloop()