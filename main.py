
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
    with open('.��key.json', 'r', encoding="utf-8") as f:
        key = json.load(f)
        set.path=key[path]
        set.azure_key = key[azure_key]

def intro():
    pass


if __name__=='__main__':
    print("�ȳ��ϼ���. wavfile�� tts�� ������ �� ���� ����� �帮�� ���α׷��Դϴ�.")
    while(True):
        print("���Ͻô� �۾��� ���� �Ͻʽÿ�.")
        print("1. ���� ����")
        print("2. ������� ����")
        print("3. ���� ����")
        print("4. STT�۾�")
        print("5. japanese to korean(����)")
        print("0. ������")
        menu = input("�۾��� �����ϼ��� ==> ")




