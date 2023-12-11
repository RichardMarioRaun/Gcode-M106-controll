import customtkinter
import tkinter.filedialog

def confwizzardstart():
    print("button clicked")

def editorstart():
    print('m106edit')

app = customtkinter.CTk()
app.geometry("400x200")

teatetekst = customtkinter.CTkLabel(app, text="Mis sa teha soovid?", fg_color="transparent")
teatetekst.pack(padx=20, pady=20)

editornupp = customtkinter.CTkButton(app, text="Moondata Gcode faili valmis seadetega", fg_color=("#DB3E39", "#821D1A"), command=editorstart())
#button = customtkinter.CTkButton(app, fg_color=("#DB3E39", "#821D1A"))  # tuple color
editornupp.pack(padx=20, pady=10)

confwizzardnupp = customtkinter.CTkButton(app, text="Teha uued seaded", command=confwizzardstart())
#button = customtkinter.CTkButton(app, fg_color=("#DB3E39", "#821D1A"))  # tuple color
confwizzardnupp.pack(padx=20, pady=10)

app.mainloop()