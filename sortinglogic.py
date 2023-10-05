import tkinter.filedialog
path = tkinter.filedialog.askopenfile()
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