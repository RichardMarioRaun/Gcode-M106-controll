path = r"C:\Users\Jan Markus\Documents\GitHub\Gcode-M106-controll\testmaterial\kylmikuriiul_0.2mm_PETG_15h14m.gcode"
fail = open(path, encoding = "UTF-8")

txt = []
typenr = set()

for rida in fail:
    txt.append(rida.strip('\n'))
fail.close()

for rida in txt:
    if rida.find(';TYPE:') == 0:
        typenr.add(str(rida[6:]))

print('\n'.join(typenr))