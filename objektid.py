import customtkinter as ctk
import tkinter.filedialog
import editor as BE


class Mainwin(ctk.CTk):
    def __init__(self, name, geom, **kwargs):
        ctk.CTk.__init__(self, **kwargs)
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
            # if valmis in self.internal:
            # self.internal.remove(valmis)

    def confwiz(self):
        self.depack()
        self.repack()


class PathselectFr(ctk.CTkFrame):
    def __init__(self, master, note, **kwargs):
        super().__init__(master, **kwargs)
        self.path = ''
        self.txt = ctk.CTkLabel(self, text=note)
        self.txt.pack(padx=10, side='left')
        self.B1 = ctk.CTkButton(self, text='Vajuta siia ja vali fail', command=self.pathselect)
        self.B1.pack(padx=10, side='left')

    def pathselect(self):
        pathnimi = str(tkinter.filedialog.askopenfile())
        self.path = pathnimi.split("'")[1]
        line = self.path.split('/')[-1]
        self.B1.configure(text=line)

    def restorename(self):
        self.B1.configure(text='Vajuta siia ja vali fail')

    def getpath(self):
        return self.path


class Confwiztabl(ctk.CTkFrame):
    def __init__(self, master, logipath=None, defal=None, **kwargs):
        super().__init__(master, **kwargs)
        self.logipath = logipath
        self.conftxt = []
        self.tablinternal = []
        self.defal = defal
        self.defffa = [['-', '-'], [self.defal], [self.defal], [self.defal], [self.defal], [self.defal], [self.defal],
                       [self.defal], [self.defal], [self.defal]]
        self.jarg = ('External perimeter', 'Perimeter', 'Overhang perimeter', 'Internal infill', 'Top solid infill',
                     'Solid infill', 'Support material interface', 'Support material', 'Skirt/Brim,Bridge infill')
        if self.logipath != None:
            defakys = ctk.CTkInputDialog(text='Vali oma tavaline õguvoolu protsernt', title="Default")
            self.defal = defakys.get_input()

    def readconf(self):
        logi = BE.Conf(self.logipath)
        self.conftxt = []
        for kiht in logi.kihid:
            RN = []
            RNd = []
            RNd.append(kiht.start)
            RNd.append(kiht.end)
            RN.append(RNd)
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
        self.depack
        rangeframe = Confrangecolm(self)
        self.tablinternal.append(rangeframe)
        for tyyp in self.jarg:
            frame =
        if self.logipath != None:
            self.readconf()
            for kiht in self.conftxt

    def depack(self):
        for asi in self.tablinternal:
            asi.pack_forget()

    def repack(self):
        for asi in self.tablinternal:
            asi.pack(padx=5, side='left')


class Confrangecolm(ctk.CTkFrame):
    def __init__(self, master, values=[['-', '-']], **kwargs):
        super().__init__(master, **kwargs)
        self.values = values  # list kiht[], kiht[], kiht[value, value]
        self.sisu = []
        self.default()

    def default(self):
        self.depack()
        dis = ctk.CTkLabel(self, text='Vahemik')
        dis.pack(pady=5)
        for kiht in self.values:
            RN = Rangerow(self, kiht[0], kiht[1])
            self.sisu.append(RN)
        self.repack()

    def repack(self):
        for element in self.sisu:
            element.pack(pady=5)

    def depack(self):
        for element in self.sisu:
            element.pack_forget()
        self.sisu = []


class Rangerow(ctk.CTkFrame):
    def __init__(self, master, alg=None, lopp=None, **kwargs):
        super().__init__(master, **kwargs)
        self.alg = alg
        self.lopp = lopp
        self.algEnt = ctk.CTkEntry(self, placeholder_text='Algus')
        self.algEnt.pack(padx=5, side='left')
        self.loppEnt = ctk.CTkEntry(self, placeholder_text='Lõpp')
        self.algEnt.pack(padx=5, side='left')
        if self.alg != None and self.lopp != None:
            self.algEnt.insert(self.alg)
            self.loppEnt.insert(self.lopp)


class Confcolm(ctk.CTkFrame):
    def __init__(self, master, discr, values, defa=None, **kwargs):
        super().__init__(master, **kwargs)
        self.discr = discr
        self.values = values
        self.sisu = []
        self.defa = defa
        self.deffa()

    def deffa(self):
        self.depack()
        nimi = ctk.CTkLabel(self, text=self.discr)
        nimi.pack(pady=5)
        for val in self.values:
            RN = ctk.CTkEntry(self)
            if defa != None:
                RN.insert(str(defa))
            self.sisu.append(RN)
        self.repack()

    def depack(self):
        for asi in self.sisu:
            asi.pack_forget()
        self.sisu = []

    def repack(self):
        for asi in self.sisu:
            asi.pack(pady=5)


win = Mainwin('M106 editor', '800x300')
win.mainloop()