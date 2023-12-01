import tkinter.filedialog

def sorceing(path):
    fail = open(path, encoding="UTF-8")
    txt = []
    for rida in fail:
        txt.append(rida.strip('\n'))
    fail.close()

    txtwmuted106n107 = []

    for rida in txt:
        RN = rida.replace('M106', ';M106 removed by script')
        RN = RN.replace('M107', ';M107 removed by script')
        txtwmuted106n107.append(RN)
    return txtwmuted106n107

def converting(arv):
    if arv == 0:
        return 'M107 ;lisatud scriptipoolt'
    else:
        return f'M106 S{round((float(arv)) / 100 * 255, ndigits=1)} ;lisatud scriptipoolt'
class Kiht:
    def __init__(self, start, end, externalperimeter, perimeter, overhangperimeter, internalinfill, topsolidinfill, solidinfill, supportmaterialinterface, supportmaterial, skirtbrim, bridgeinfill):
        self.start = start
        self.end = end
        self.externalperimeter = converting(int(externalperimeter))
        self.perimeter = converting(int(perimeter))
        self.overhangperimeter = converting(int(overhangperimeter))
        self.internalinfill = converting(int(internalinfill))
        self.topsolidinfill = converting(int(topsolidinfill))
        self.solidinfill = converting(int(solidinfill))
        self.supportmaterialinterface = converting(int(supportmaterialinterface))
        self.supportmaterial = converting(int(supportmaterial))
        self.skirtbrim = converting(int(skirtbrim))
        self.bridgeinfill = converting(int(bridgeinfill))

    #hiljem tuleb teha ka kihiconf valja kirjutamine def

class Conf:
    def __init__(self, path):
        self.path = path
        self.kihid = []
    def logread(self):
        fail = open(self.path, encoding = 'UTF-8')
        ridan = 0
        for rida in fail:
            if ridan == 0: ridan += 1
            else:
                string = rida.strip('\n')
                RN = string.split(',')
                vahemik = []
                if RN[0] == '-': #and len(self.kihid) == 0:
                    vahemik.extend(['-', '-'])
                elif RN[0][-1] == '-':
                    vahemik.extend([float(RN[0].strip('-')), '-'])
                elif RN[0][0] == '-':
                    vahemik.extend(['-', float(RN[0].strip('-'))])
                else:
                    vahemik.extend(RN[0].split('-'))
                    vahemik[0] = float(vahemik[0])
                    vahemik[1] = float(vahemik[1])
                kiht = Kiht(vahemik[0], vahemik[1], RN[1], RN[2], RN[3], RN[4], RN[5], RN[6], RN[7], RN[8], RN[9], RN[10])
                self.kihid.append(kiht)

    def sliceselector(self, gslicepot):
        guide = []
        RN = []
        layers = self.kihid.copy()

        if layers[0].start != '-':
            start = layers[0].start
        elif len(guide) == 0:
            start = 0
        else:
            start = guide[-1][0].start
        if layers[0].end != '-':
            end = layers[0].end
        else:
            end = gslicepot[-1].zcord + 10

        for gslice in gslicepot:
            if start <= gslice.zcord < end:
                RN.append(gslice)
            else:
                guide.append([layers[0], RN])
                layers.remove(layers[0])

                if layers[0].start != '-':
                    start = layers[0].start

                if layers[0].end != '-':
                    end = layers[0].end
                else:
                    end = gslicepot[-1].zcord + 10
                RN = []
                RN.append(gslice)

        return guide

class Gslice:
    def __init__(self, zcord):
        self.zcord = float(zcord)
        self.data = []
def gcodeslice(txt):
    gsliceRN = []
    zcord = float(0)
    gslicepot = []
    for rida in txt:
        if rida[0:4] == 'G1 Z':
            RN = Gslice(zcord)
            RN.data.extend(gsliceRN)
            gslicepot.append(RN)
            if rida[4] == '.':
                zcord = float((rida.split(' ')[1]).strip('Z.'))/10
            else:
                zcord = float((rida.split(' ')[1]).strip('Z'))
        gsliceRN.append(rida)
    return gslicepot
def m106editor(gslice, conf):

    Externalperimeter = conf.externalperimeter
    Perimeter = conf.perimeter
    Overhangperimeter = conf.overhangperimeter
    Internalinfill = conf.internalinfill
    Topsolidinfill = conf.topsolidinfill
    Solidinfill = conf.solidinfill
    Supportmaterialinterface = conf.supportmaterialinterface
    Supportmaterial = conf.supportmaterial
    SkirtBrim = conf.skirtbrim
    Bridgeinfill = conf.bridgeinfill

    txtwchanged106n107 = []


    for i in gslice:
        for rida in i.data:
            txtwchanged106n107.append(rida)
            if rida.find(';TYPE:') == 0 and ('Custom' not in rida):
                if ('External perimeter' in rida):
                    txtwchanged106n107.append(Externalperimeter)
                elif ('Perimeter' in rida):
                    txtwchanged106n107.append(Perimeter)
                elif ('Overhang perimeter' in rida):
                    txtwchanged106n107.append(Overhangperimeter)
                elif ('Internal infill' in rida):
                    txtwchanged106n107.append(Internalinfill)
                elif ('Top solid infill' in rida):
                    txtwchanged106n107.append(Topsolidinfill)
                elif ('Solid infill' in rida):
                    txtwchanged106n107.append(Solidinfill)
                elif ('Support materjal interface' in rida):
                    txtwchanged106n107.append(Supportmaterialinterface)
                elif ('Support material' in rida):
                    txtwchanged106n107.append(Supportmaterial)
                elif ('Skirt/Brim' in rida):
                    txtwchanged106n107.append(SkirtBrim)
                elif ('Bridge infill' in rida):
                    txtwchanged106n107.append(Bridgeinfill)
                else:
                    print('Error: type not specified: ', rida)
    print('koik sai edukalt muudetud')
    return txtwchanged106n107

def director():
    print('vali gcode mida soovid muuta...')
    pathnimi = str(tkinter.filedialog.askopenfile())
    path = pathnimi.split("'")[1]

    print('vali preset fail...')
    logpathnimi = str(tkinter.filedialog.askopenfile())
    logpath = logpathnimi.split("'")[1]

    print('vali targetfile millele muudatsed salvestatakse...')
    exitpathname = str(tkinter.filedialog.askopenfile())
    exitpath = exitpathname.split("'")[1]

    conf = Conf(logpath)
    conf.logread()
    gpot = gcodeslice(sorceing(path))

    paarid = conf.sliceselector(gpot)

    exitgcode = []

    for paar in paarid:
        exitgcode.extend(m106editor(paar[1], paar[0]))

    exitfail = open(exitpath, 'w', encoding="UTF-8")
    exitfail.write('\n'.join(exitgcode))
    exitfail.close()

director()