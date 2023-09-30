import os
# Teeb faili gcode'ist txt failiks
old_full_path = "/Users/ricky.raun/Documents/GitHub/Gcode-M106-controll/testmaterial/30cube_0.2mm_ABS_39m.gcode"
new_file_name = "30cube_0.2mm_ABS_39m.txt"
directory = os.path.dirname(old_full_path)
new_full_path = os.path.join(directory, new_file_name)
try:
    os.rename(old_full_path, new_full_path)
    print(f"File '{old_full_path}' renamed to '{new_full_path}'.")
except OSError as e:
    print(f"Error renaming file: {e}")



# Avab faili
path = '/Users/ricky.raun/Documents/GitHub/Gcode-M106-controll/testmaterial/30cube_0.2mm_ABS_39m.txt'
fail = open(path, encoding = "UTF-8")

phonebook=[]
muutustvajavad=[]

failiKirjutamiseReaLugeja=0
muutustvajavadindeks=0

soovitudTekst="M106 S126"

# Loeb andmed failist listi
realugeja=0
for rida in fail:
    ajutine=[]
    realugeja+=1
    ajutine.append(realugeja)
    if rida == """;TYPE:External perimeter\n""":
        muutustvajavad.append(realugeja)
    rida = rida.strip("\n").split(":")
    for sone in rida:
        ajutine.append(sone)
        if sone == ";TYPE":
            print(f"rida: {realugeja} ja sone on {sone}")
    phonebook.append(ajutine)
fail.close()

# Kirjutab andmed listist faili


with open(path,"w+", encoding = "UTF-8") as fail:
    for rida in fail:
        if (failiKirjutamiseReaLugeja == muutustvajavad[muutustvajavadindeks]+1):
            muutustvajavadindeks+=1
            fail.write(soovitudTekst+"""\n""")
        else:
            ajutine2=""
            for element in phonebook[failiKirjutamiseReaLugeja]:
                ajutine2+=element
            fail.write(ajutine2+"""\n""")
            failiKirjutamiseReaLugeja+=1







print(muutustvajavad)
# Teeb faili txt failist gcode'iks
old_full_path = "/Users/ricky.raun/Documents/GitHub/Gcode-M106-controll/testmaterial/30cube_0.2mm_ABS_39m.txt"
new_file_name = "30cube_0.2mm_ABS_39m.gcode"
directory = os.path.dirname(old_full_path)
new_full_path = os.path.join(directory, new_file_name)
try:
    os.rename(old_full_path, new_full_path)
    print(f"File '{old_full_path}' renamed to '{new_full_path}'.")
except OSError as e:
    print(f"Error renaming file: {e}")