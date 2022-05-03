
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

import wav_spleeter as spl
import wav_to_text as stt
import wav_transform as trans


def readkey():
    with open('key.json', 'r', encoding="utf-8") as f:
        key = json.load(f)
        set.path=key['path']
        set.azure_key = key['azure_key']

def intro():
    pass


if __name__=='__main__':
    print("�ȳ��ϼ���. wavfile�� tts�� ������ �� ���� ����� �帮�� ���α׷��Դϴ�.")
    readkey()
    while(True):
        print("�n�n���Ͻô� �۾��� ���� �Ͻʽÿ�.")
        print("1. ���� ����")
        print("2. ������� ����")
        print("3. ���� ����")
        print("4. STT�۾�")
        print("5. japanese to korean(����)")
        print("0. ������")
        menu = input("�۾��� �����ϼ��� ==> ")
        task = int(menu) if menu.isdigit() else -1
        if task ==1:
            print("���������� �ǽ��մϴ�.")

            print("dataset�� ����ִ� ���丮�� ��θ� �Է����ּ���.")
            print("enter�� ������ key.json�� �ִ� ��ο��� �۾��� ����˴ϴ�.")
            p = input("path : ")
            if p!='':
                set.path = p
            print(f'path : {set.path}')

            print("STT�۾����� ����� api�� key�� �ִٸ� key�� �Է����ּ���")
            print("enter�� ������ key.json�� �ִ� key���� �����ɴϴ�.")
            k = input("api_key : ")
            if k != '':
                set.azure_key = k
            print(f'api_key : {set.azure_key}')

            fir = spl.wav_spleeter()
            input("������� �����۾�(spleeter)���� �ð��� �ټ� �ҿ�˴ϴ�. �����ϼ����� ���͸� �����ּ���")
            fir.folderinfo()
            fir.spleeter(0)
            fir.spldata_to_path()
            print("������� ���� �۾��� �Ϸ�Ǿ����ϴ�.")
            print("��������� ���ŵ� wav������ spleeter_out���Ͽ� ����ֽ��ϴ�.")

            print("wav���� ��ȯ�۾��� �����մϴ�.")
            print("��ȯ�۾������� wav������ channels�� sampling rate�� ��ȯ�մϴ�.")
            rate = input("���ϴ� sampling rate�� �Է��ϼ���. ���͸� �����ø� default���� 22050���� ��ȯ�մϴ�.")
            sec = trans.transform()
            sec.trans() if rate is '' else sec.trans(rate)
            print("��ȯ�� �Ϸ�Ǿ����ϴ�.")

            print("STT�۾��� �����մϴ�.")
            print("STT�۾������� wav���ϵ��� ������ text�� ��ȯ�Ͽ� json���Ͽ� �����մϴ�.")
            print("����� api�� �����ϼ���. 1���� ������ key�� �ʿ�����ϴ�.")
            print("1. google web speech")
            print("2. google cloud speech")
            print("3. azure stt")
            api = input("==>")
            thr = stt.wav_to_text(choose_api = int(api))
            print("stt�۾��� �Ϸ�Ǿ����ϴ�.")
            print("json������ Ȯ�����ּ���.")




        elif task ==2:
            pass
        elif task ==3:
            pass
        elif task ==4:
            pass
        elif task ==5:
            pass
        elif task ==0:
            print("�̿����ּż� �����մϴ�. ����")
            exit()
        elif task == -1:
            print("���ڸ� �Է����ּ���")
        else:
            prnit("0 ~ 5 �߿��� �ϳ� �������ּ���")





