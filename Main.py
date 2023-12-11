import customtkinter as ctk
import tkinter.filedialog
#import editor

class Pathnupp:
    def __init__(self):
        self.path = 'vajuta, et valida fail'
        self.sorcetrue = False

    def getsorce(self):
        pathnimi = str(tkinter.filedialog.askopenfile())
        self.path = pathnimi.split("'")[1]
        self.sorcetrue = True

def edit():
    print('tere')
    editwin = ctk.CTk()
    editwin.geometry('800x400')
    editwin.title('Failide valik')

    introrida = ctk.CTkFrame(editwin)
    introtekst = ctk.CTkLabel(introrida, text='Vali vastavad failid ja vajuta start')
    introtekst.pack(pady=5, side='left')
    introrida.pack(pady=5)

    sorcepath = Pathnupp()

    esimenerida = ctk.CTkFrame(editwin)
    sorcefailtekst = ctk.CTkLabel(esimenerida, text='algne fail:')
    sorcefailtekst.pack(padx=10, side='left')
    sorcenupp = ctk.CTkButton(esimenerida, text=sorcepath.path, command=sorcepath.getsorce)
    sorcenupp.pack(padx=10)
    esimenerida.pack()

    print(sorcepath.path)

    editwin.mainloop()


pea = ctk.CTk()
pea.geometry('400x400')

teade = ctk.CTkLabel(pea, text="Mis sa teha soovid?", fg_color="transparent")

editstartnupp = ctk.CTkButton(pea, text='Moondata Gcode faili valmis seadetega', command=edit)
editstartnupp.pack(padx=10, pady=10)

pea.mainloop()