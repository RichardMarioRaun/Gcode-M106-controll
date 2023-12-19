import customtkinter as ctk
import tkinter.filedialog
import editor as BE

class App(ctk.CTk):
    def __init__(self, name, geom, **kwargs):
        ctk.CTk.__init__(self,**kwargs)
        self.title(name)
        self.geometry(geom)
        self.sorcepath = ''
        self.logpath = ''
        self.exitpath = ''
        self.internal = []
        introtxt = ctk.CTkLabel(self, text='Mis sa teha soovid?')
        self.internal.append(introtxt)
        editinitB = ctk.CTkButton(self, text='Moondata Gcode faili valmis seadetega', command=self.editbutton)
        self.internal.append(editinitB)
        confwizB = ctk.CTkButton(self, text='Teha uued seaded', command=self.confwiz)
        self.internal.append(confwizB)
        self.repack()


        self.sorceN = PathselectFr(self, 'Vali alusfail')
        self.logN = PathselectFr(self, 'Vali seadete CSV fail')
        self.exitN = PathselectFr(self, 'Vali väljundi fail')
    def repack(self):
        for asi in self.internal:
            asi.pack(pady=10)
    def depack(self):
        for asi in self.internal:
            asi.pack_forget()
        self.internal = []

    def restore(self):
        self.depack()
        self.sorcepath = ''
        self.logpath = ''
        self.exitpath = ''
        introtxt = ctk.CTkLabel(self, text='Mis sa teha soovid?')
        self.internal.append(introtxt)
        editinitB = ctk.CTkButton(self, text='Moondata Gcode faili valmis seadetega', command=self.editbutton)
        self.internal.append(editinitB)
        confwizB = ctk.CTkButton(self, text='Teha uued seaded', command=self.confwiz)
        self.internal.append(confwizB)
        self.repack()
    def editbutton(self):
        self.depack()
        exp = ctk.CTkLabel(self, text='Vali vastavad failid ja vajuta start')
        self.internal.append(exp)
        self.internal.append(self.sorceN)
        self.internal.append(self.logN)
        self.internal.append(self.exitN)
        loppvalik = ctk.CTkFrame(self)
        tagasiN = ctk.CTkButton(loppvalik, text='tagasi...', command=self.restore)
        tagasiN.pack(padx=10, side='left')
        startN = ctk.CTkButton(loppvalik, text='START', command=self.editstart)
        startN.pack(padx=10, side='left')
        self.internal.append(loppvalik)
        self.repack()
    def editstart(self):
        self.sorcepath = self.sorceN.getpath()
        self.logpath = self.logN.getpath()
        self.exitpath = self.exitN.getpath()
        valmis = ctk.CTkLabel(self, text='Valmis!')
        viga = ctk.CTkLabel(self, text='Kõik failid pole valitud')

        if len(self.internal) == 6:
            (self.internal[-1]).pack_forget()
            self.internal.remove(self.internal[-1])

        if self.sorcepath and self.logpath and self.exitpath:
            BE.director(self.sorcepath, self.logpath, self.exitpath)
            self.internal.append(valmis)
            valmis.pack(pady=10)

            self.after(1000, self.editbutton)

        else:
            self.internal.append(viga)
            viga.pack(pady=10)
            self.after(1000, self.editbutton)
            #if valmis in self.internal:
                #self.internal.remove(valmis)
    def confwiz(self):
        self.depack()
        self.repack()
class PathselectFr(ctk.CTkFrame):
    def __init__(self, master, note, **kwargs):
        super().__init__(master, **kwargs)
        self.path = ''
        self.txt = ctk.CTkLabel(self, text=note)
        self.txt.pack(padx=10, side = 'left')
        self.B1 = ctk.CTkButton(self, text='Vajuta siia ja vali fail', command=self.pathselect)
        self.B1.pack(padx=10, side = 'left')
    def pathselect(self):
        pathnimi = str(tkinter.filedialog.askopenfile())
        self.path = pathnimi.split("'")[1]
        line = self.path.split('/')[-1]
        self.B1.configure(text=line)
    def restorename(self):
        self.B1.configure(text='Vajuta siia ja vali fail')

    def getpath(self):
        return self.path

class Conftabel(ctk.CTkFrame):
    jarg = ['Vahemik', 'External perimeter', 'Perimeter', 'Overhang perimeter', 'Internal infill', 'Top solid infill', 'Solid infill', 'Support material interface', 'Support material', 'Skirt/Brim,Bridge infill']
    def __init__(self, master, logipath=None, **kwargs):
        super().__init__(master, **kwargs)
        self.logipath = logipath
        self.conftxt = []
    def readconf(self):
        logi = BE.Conf(self.logipath)
        self.conftxt = []
        for kiht in logi.kihid:
            RN = []
            RN.append(kiht.start)
            Rn.append(kiht.end)
            RN.append(BE.deconvert(kiht.externalperimeter))
            RN.append(BE.deconvert(kiht.perimeter))
            RN.append(BE.deconvert(kiht.overhangperimeter))
            RN.append(BE.deconvert(kiht.internalinfill))
            RN.append(BE.deconvert(kiht.topsolidinfill))
            RN.append(BE.deconvert(kiht.solidinfill))
            RN.append(BE.deconvert(kiht.supportmaterialinterface))
            RN.append(BE.deconvert(kiht.supportmaterial))
            RN.append(BE.deconvert(kiht.skirtbrim))
            RN.append(BE.deconvert(kiht.bridgeinfill))
            self.conftxt.append(RN)

    def confrend(self):

class confcolm(ctk.CTkFrame):
    def __init__(self, master, defa=True, discr, values, **kwargs):
        super().(master, **kwargs)
        self.tyyp=defa
        self.discr=discr
        self.values=values
        self.sisu = []

    def ty1in(self):


win = App('M106 editor', '800x300')
win.mainloop()