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

# Teeb oma programmi sisu
realugeja=0
for rida in fail:
    realugeja+=1
    rida = rida.strip("\n").split(":")
    for sone in rida:
        if sone == "Overhang perimeter":
            print(f"rida: {realugeja} ja sone on {sone}")
fail.close()

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