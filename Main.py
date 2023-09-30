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

    rida = rida.replace("'", "\\'").replace('"', '\\"')
    rida = rida.strip("\n").split(":")

    for sone in rida:
        sone = sone.replace("'", "\\'").replace('"', '\\"')
        ajutine.append(str(sone))
    phonebook.append(ajutine)
fail.close()

# Kirjutab andmed listist faili

y=0
with open(path,"w+", encoding = "UTF-8") as fail:
    while (y< len(phonebook) + len(muutustvajavad)):
        if (len(muutustvajavad)>muutustvajavadindeks):
            if (failiKirjutamiseReaLugeja == muutustvajavad[muutustvajavadindeks]):
                muutustvajavadindeks+=1
                fail.write(soovitudTekst+"\n")
            else:
                ajutine2=""
                for element in range(len(phonebook[failiKirjutamiseReaLugeja])):
                    if element==0:
                        continue
                    else:
                        if (phonebook[failiKirjutamiseReaLugeja][element]==";TYPE" and phonebook[failiKirjutamiseReaLugeja][element+1]=="External perimeter"):
                            ajutine2 += (phonebook[failiKirjutamiseReaLugeja][element]+";")
                        else:
                            ajutine2+=phonebook[failiKirjutamiseReaLugeja][element]
                fail.write(ajutine2+"\n")
                failiKirjutamiseReaLugeja+=1
        else:
            ajutine2=""
            for element in range(len(phonebook[failiKirjutamiseReaLugeja])):
                if element==0:
                    continue
                else:
                    ajutine2+=phonebook[failiKirjutamiseReaLugeja][element]
            fail.write(ajutine2+"\n")
            failiKirjutamiseReaLugeja+=1
        y+=1



print(f"Muutust vajas {muutustvajavad} elementi!")
"""
hasti=0
jama=0

for el in (phonebook):
    for i in range(len(el)):
        if i ==0:
            continue
        elif type(el[i]) != str:
            jama+=1
        else:
            hasti+=1

print(jama)
print(hasti)
"""

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