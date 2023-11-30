import tkinter.filedialog

print('vali gcode mida soovid muuta...')
pathnimi = str(tkinter.filedialog.askopenfile())
path = pathnimi.split("'")[1]

print('vali preset fail...')
logpathnimi = str(tkinter.filedialog.askopenfile())
logpath = logpathnimi.split("'")[1]

print('vali targetfile millele muudatsed salvestatakse...')
exitpathname = str(tkinter.filedialog.askopenfile())
exitpath = exitpathname.split("'")[1]

class kiht:
    def __init__(self, start, end, externalperimeter, perimeter, overhangperimeter, internalinfill, topsolidinfill, solidinfill, supportmaterialinterface, supportmaterial, skirtbrim, bridgeinfill):
        self.start = float(start)
        self.end = floar(end)
        self.externalperimeter = externalperimeter
        self.perimeter = perimeter
        self.overhangperimeter = overhangperimeter
        self.internalinfill = internalinfill
        self.topsolidinfill = topsolidinfill
        self.solidinfill = solidinfill
        self.supportmaterialinterface = supportmaterialinterface
        self.supportmaterial = supportmaterial
        self.skirtbrim = skirtbrim
        self.bridgeinfill = bridgeinfill

class conf:
    def __init__(self, path):
        self.path = path
        self.kihid = []
    def logread(self, path):
        fail = open(path, encoding = 'UTF-8')
        ridan = 0
        for rida in fail:
            if ridan == 0: ridan += 1 and continue
            string = rida.strip('\n')
            RN = string.split(',')

def logide_lugemine(logpath):
def m106editor(path, logpath, exitpath):
    fail = open(path, encoding = "UTF-8")

    txt = []
    typenr = []

    for rida in fail:
        txt.append(rida.strip('\n'))
    fail.close()

    #logpath = r"C:\Users\Jan Markus\gcodetest\M106config_ABSwhite.txt"
    #logpath = r'C:\Users\Jan Markus\Documents\GitHub\Gcode-M106-controll\testmaterial\M106config_ABSwhite.txt'
    logfail = open(logpath, encoding = "UTF-8")

    logtxt = []

    for rida in logfail:
        if rida != str('\n'):
            logtxt.append(rida.strip('\n'))

    logfail.close()

    #ebavajalikud M106 ja M107 neutraliseerimised

    txtwmuted106n107 = []

    for rida in txt:
        RN = rida.replace('M106', ';M106 removed by script')
        RN = RN.replace('M107', ';M107 removed by script')
        txtwmuted106n107.append(RN)

    #logidest saadud info sisestamine
    logid = []

    for rida in logtxt:
        if rida.find('$') != 0:
            logid.append(rida.split(' = ')[1])

    #logide muutmine Gcodeile loetavaks formaadiks
    index = 0
    for i in logid:
        if i == '0':
            logid[index] = 'M107 ;lisatud scriptipoolt'
        else:
            logid[index] = f'M106 S{round((float(i))/100*255, ndigits=1)} ;lisatud scriptipoolt'
        index += 1

    Externalperimeter = logid[0]
    Perimeter = logid[1]
    Overhangperimeter = logid[2]
    Internalinfill = logid[3]
    Topsolidinfill = logid[4]
    Solidinfill = logid[5]
    Supportmaterialinterface = logid[6]
    Supportmaterial = logid[7]
    SkirtBrim = logid[8]
    Bridgeinfill = logid[9]

    #logide rakendamine

    txtwchanged106n107 = []

    for rida in txtwmuted106n107:
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

    count = 0
    parandusliige = 0
    index = 1
    for rida in txt:
        index += 1
        RN = []
        if rida.find(';TYPE:') == 0:
            RN.append(str(index))
            RN.append(rida)
            count += 1
            #print(rida)
            typenr.append(RN)

    editedgcode = '\n'.join(txtwchanged106n107)

    exitfail = open(exitpath,'w', encoding = "UTF-8")
    exitfail.write(editedgcode)
    exitfail.close()
    #print(count)
    #vastus = []
    #for i in typenr:
        #RN = ''
        #RN = str('. real on'.join(i))
        #vastus.append(RN)
    #print(txtwmuted106n107)
    #print(Infill)
    #print(logid)
    #print(editedgcode)
    return print('koik sai edukalt muudetud')

m106editor(path, logpath, exitpath)