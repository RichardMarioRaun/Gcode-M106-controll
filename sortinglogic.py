path = r"C:\Users\Jan Markus\Documents\GitHub\Gcode-M106-controll\testmaterial\karlireket_0.2mm_PETG_8h55m.gcode"
fail = open(path, encoding = "UTF-8")

txt = []
typenr = set()

for rida in fail:
    txt.append(rida.strip('\n'))
fail.close()

for rida in txt:
    if rida.find(';TYPE:') == 0:
        typenr.add(str(rida[6:]))

print(typenr)