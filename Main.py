#failidest valja lugemine ja algne andme tootlus
path = r"C:\Users\Jan Markus\gcodetest\30cube_0.5mm_ABS_13m.gcode"
fail = open(path, encoding = "UTF-8")

txt = []
typenr = []

for rida in fail:
    txt.append(rida.strip('\n'))
fail.close()

logpath = r"C:\Users\Jan Markus\gcodetest\M106config_ABSwhite.txt"
logfail = open(logpath, encoding = "UTF-8")

logtxt = []

for rida in logfail:
    if rida != str('\n'):
        logtxt.append(rida.strip('\n'))

logfail.close()

#ebavajalikud M106 ja M107 neutraliseerimised

txtwmuted106n107 = []

for rida in txt:
    RN = rida.replace('M106', ';M106 edited')
    RN = RN.replace('M107', ';M107 edited')
    txtwmuted106n107.append(RN)

#logidest saadud info sisestamine



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



print(count)
#vastus = []
#for i in typenr:
    #RN = ''
    #RN = str('. real on'.join(i))
    #vastus.append(RN)
#print(txtwmuted106n107)
print(logtxt)

