
# -*- coding: cp949 -*-
'''
    1. wav_spleeter���� spleeter����
    2. wav_transform���� wav���� ����
    3. speech�� ���� text ���ϱ�
    ��

'''

from set import azure_key, path
import set
import json
import os
import datetime

def readkey():
    with open('.��key.json', 'r', encoding='UTF8') as f:
        key = json.load(f)
        set.path=key[path]
        set.azure_key = key[azure_key]

def split(num):
    l = ""
    list = l.split("����")
    print(list)
    print(len(list))

    for i in range(len(list)):
        print(str(i+1) + list[i])
    dic = {}
    namelist=[]

    # �����̸� �̾Ƴ��°�
    with open('azure_stt.json', 'r', encoding='UTF8') as f:
        l = json.load(f)
        for i in l:
            if i.split("_")[0]==str(num):
                namelist.append(i)
    print(namelist)

    with open('kor_text.json', 'r', encoding='UTF8') as f:
        dic = json.load(f)
        for i in range(len(namelist)):
            dic[namelist[i]] = list[i]


    with open('kor_text.json', 'w', encoding='UTF8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)



def alltxt(num):
    with open('azure_stt.json', 'r', encoding='UTF8') as f:
        l = json.load(f)
        for i in l:
            if i.split("_")[0] == str(num):
                #print(i.split("_")[1] + " : " + l[i])
                #print(i+l[i]+" ��ǳ��")
                print(l[i] + " Ŀ��")


if __name__=='__main__':
    pass
    #os.chdir("..")

    #alltxt(13)
    #split(13)





