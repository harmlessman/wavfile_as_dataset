import json
import os

import set
import set as s
import shutil

def readkey():
    with open('key.json', 'r', encoding="utf-8") as f:
        key = json.load(f)
        s.path=key['path']
        if key['path']=="":
            s.path = '.\\'
        s.azure_key = key['azure_key']

# 여러개의 json파일 통합해서 set.textsetname에 집어넣음.
# 나머지 json파일은 삭제
def combine():
    os.chdir(s.path)
    dic = {}
    jlist = [j for j in os.listdir(s.path) if j.endswith(".json")]

    if s.textsetname not in jlist:
        print(f'{set.textsetname} 파일이 존재하지 않습니다. STT작업을 먼저 시행하신 후 combine을 해주십시오.')
        return

    jlist.remove(s.textsetname)
    if len(jlist) == 0:
        print(f'combine작업을 진행 할 {set.textsetname}이외의 json파일이 존재하지 않으므로 이 작업은 넘어갑니다.')
        return

    with open(s.textsetname, 'r', encoding='UTF8') as f:
        dic = json.load(f)

    for i in jlist:
        with open(i, 'r', encoding='UTF8') as f:
            dic.update(json.load(f))

    print(dic)
    with open(s.textsetname, 'w', encoding='UTF8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)

    for i in jlist:
        os.remove(i)

# trans폴더에서 직접 상태가 안좋은 wav파일 골라낸 후 실행하는 함수
# 실행하면 json파일에서 삭제한 파일에 해당하는 "wavfile" : text를 삭제시킴
def delete():
    t_path = s.path + "\\trans\\"
    os.chdir(s.path)

    filelist = s.wavlist(t_path)

    print(f'trans dir filelist => {filelist}')

    with open(s.textsetname, 'r', encoding='UTF8') as f:
        clean = json.load(f)

    delist = []

    for i in clean.keys():
        if i not in filelist:
            delist.append(i)

    for i in delist:
        del clean[i]

    for i in clean:
        clean[i] = clean[i].strip()

    print(f'delete wavfile => {delist}')
    print(f'text.json => {clean.keys()}')

    with open(s.textsetname, 'w', encoding='UTF8') as f:
        json.dump(clean, f, ensure_ascii=False, indent=2)

# set.textsetname의 json파일에서 key부분을 path+wavfile로  바꿔줌
# 그리고 dataset이 있어야 하는 path로 보냄
def target():
    t_path = s.path + "\\trans\\"
    print(f'wavfile 과 text셋인 json파일을 위치시킬 path를 입력해주세요')
    targetpath = input("targetpath => ")
    print(f'targetpath => {targetpath}')

    print(f'폴더의 이름을 정해주세요')
    dirname = input("dirname => ")
    print(f'dirname => {dirname}')

    path = targetpath + "\\" + dirname + "\\" + "audio" + "\\"
    jpath = targetpath + "\\" + dirname+ "\\" + s.textsetname
    try:
        shutil.copytree(t_path, path)
    except FileExistsError:
        shutil.rmtree(path)
        shutil.copytree(t_path, path)

    shutil.copy(s.path+"\\"+s.textsetname, jpath)

    with open(jpath, 'r', encoding='UTF8') as f:
        jsondic = json.load(f)
    filelist = s.wavlist(path)

    print(filelist)
    print(jsondic)

    if filelist==list(jsondic.keys()):
        dic = {}
        with open(jpath, 'w', encoding='UTF8') as f:
            for i in jsondic:
                dic[path + i] = jsondic[i]
            json.dump(dic, f, ensure_ascii=False, indent=2)
        print("DONE")
    else:
        print("wavfile들과 json의 data가 일치하지 않음!")
        if len(set(filelist)-set(list(jsondic.keys())))!=0:
            print(f'{set(filelist)-set(list(jsondic.keys()))}이 json파일에 데이터가 존재하지 않습니다.')
        if len(set(list(jsondic.keys()))-set(filelist))!=0:
            print(f'{set(list(jsondic.keys()))-set(filelist)}이 wav파일이 존재하지 않습니다.')
        print("확인 후 다시 실행해주세요")



if __name__ == '__main__':
    readkey()
    target()
