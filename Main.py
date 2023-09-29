path = '/Users/ricky.raun/Documents/GitHub/Gcode-M106-controll/testmaterial/30cube_0.2mm_ABS_39m.txt'
fail = open(path, encoding = "UTF-8")

realugeja=0
for rida in fail:
    realugeja+=1
    rida = rida.strip("\n").split(":")
    for sone in rida:
        if sone == "Overhang perimeter":
            print(f"rida: {realugeja} ja sone on {sone}")



fail.close()

