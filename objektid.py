import customtkinter as ctk
import tkinter.filedialog

class Window(ctk.CTk):
    def __init__(self, geom, name, **kwargs):
        ctk.CTk.__init__(self, **kwargs)
        self.geometry(geom)
        self.title(name)
        self.obj = []


    def addframe(self, tingi):
        self.obj.append(tingi)
        for asi in self.obj:
            asi.pack(padx=10, pady=10)

    def killframe(self):
        self.obj = []

class Nupp(ctk.CTkButton):
    sorcepath = ''
    logpath = ''
    exitpath = ''

    def __init__(self, origin, txt, cmd=None):
        ctk.CTkButton.__init__(self, master=origin, text=txt, command=cmd)

class Editpress(Nupp):
    def __init__(self, origin, txt):
        Nupp.__init__(self, origin, txt, cmd=self.startedit)
        self.origin = origin

    def startedit(self):
        self.configure(text='vajuta veel')
        self.origin.killinit()
        print('tere')

def killinit(frame):
    origin.after(1000, lambda: print('tere'))
    frame.killframe()

r = Window('800x800', 'testnimi')
n1 = Editpress(r, 'homho')
r.addframe(n1)
r.mainloop()