import customtkinter as ctk
import tkinter.filedialog
import tkinter

class Pathnupp:
    def __init__(self, button):
        self.path_var = tkinter.StringVar()
        self.path_var.set('vajuta, et valida fail')
        self.sorcetrue = False
        self.button = button

    def update_label(self):
        self.button.config(text=self.path_var.get())

    def getsorce(self):
        pathnimi = str(tkinter.filedialog.askopenfile())
        self.path_var.set(pathnimi.split("'")[1])
        self.sorcetrue = True
        self.update_label()

def edit():
    editwin = ctk.CTk()
    editwin.geometry('800x400')
    editwin.title('Failide valik')

    introrida = ctk.CTkFrame(editwin)
    introtekst = ctk.CTkLabel(introrida, text='Vali vastavad failid ja vajuta start')
    introtekst.pack(pady=5, side='left')
    introrida.pack(pady=5)

    sorcepath = Pathnupp(None)

    esimenerida = ctk.CTkFrame(editwin)
    sorcefailtekst = ctk.CTkLabel(esimenerida, text='algne fail:')
    sorcefailtekst.pack(padx=10, side='left')

    sorcenupp = ctk.CTkButton(esimenerida, textvariable=sorcepath.path_var, command=sorcepath.getsorce)
    sorcepath.button = sorcenupp  # Pass the button to the Pathnupp instance
    sorcenupp.pack(padx=10)
    esimenerida.pack()

    editwin.mainloop()

pea = ctk.CTk()
pea.geometry('400x400')

teade = ctk.CTkLabel(pea, text="Mis sa teha soovid?", fg_color="transparent")

editstartnupp = ctk.CTkButton(pea, text='Moondata Gcode faili valmis seadetega', command=edit)
editstartnupp.pack(padx=10, pady=10)

pea.mainloop()