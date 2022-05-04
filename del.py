import os
import json
os.chdir('C:\\Users\\82109\\Desktop\\emilia')

def wavlist(p):
    return sorted([wav for wav in os.listdir(p) if wav.endswith(".wav")], key=lambda x: int(x.split('_')[0]))

filelist = wavlist('.\\audio')


with open('emilia-recognition-All.json', 'r', encoding='UTF8') as f:
    clean = json.load(f)


delist = []

for i in clean.keys():
    if i not in filelist:
        delist.append(i)

for i in delist:
    del clean[i]

for i in clean:
    clean[i] = clean[i].strip()

print(delist)
print(clean)

with open('emilia-recognition-Allr.json', 'w', encoding='UTF8') as f:
    json.dump(clean, f, ensure_ascii=False, indent=2)



dic={}
with open('emilia-recognition-Allr.json', 'r', encoding='UTF8') as f:
    pl = json.load(f)


with open('emilia-recognition-Allr.json', 'w', encoding='UTF8') as ff:
    for i in pl:
        dic["./datasets/emilia/audio/"+i] = pl[i]
    json.dump(dic, ff, ensure_ascii=False, indent=2)
