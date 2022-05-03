
# -*- coding: cp949 -*-
'''
    1. wav_spleeter에서 spleeter수행
    2. wav_transform에서 wav파일 변형
    3. speech에 대한 text 구하기
    끝

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
    print("안녕하세요. wavfile을 tts용 데이터 셋 으로 만들어 드리는 프로그램입니다.")
    readkey()
    while(True):
        print("굈굈원하시는 작업을 선택 하십시오.")
        print("1. 빠른 시작")
        print("2. 배경음악 제거")
        print("3. 파일 변형")
        print("4. STT작업")
        print("5. japanese to korean(예정)")
        print("0. 나가기")
        menu = input("작업을 선택하세요 ==> ")
        task = int(menu) if menu.isdigit() else -1
        if task ==1:
            print("빠른시작을 실시합니다.")

            print("dataset이 들어있는 디렉토리의 경로를 입력해주세요.")
            print("enter를 누르면 key.json에 있는 경로에서 작업이 진행됩니다.")
            p = input("path : ")
            if p!='':
                set.path = p
            print(f'path : {set.path}')

            print("STT작업에서 사용할 api의 key가 있다면 key를 입력해주세요")
            print("enter를 누르면 key.json에 있는 key값을 가져옵니다.")
            k = input("api_key : ")
            if k != '':
                set.azure_key = k
            print(f'api_key : {set.azure_key}')

            fir = spl.wav_spleeter()
            input("배경음악 제거작업(spleeter)에는 시간이 다소 소요됩니다. 인지하셨으면 엔터를 눌러주세요")
            fir.folderinfo()
            fir.spleeter(0)
            fir.spldata_to_path()
            print("배경음악 제거 작업이 완료되었습니다.")
            print("배경음악이 제거된 wav파일은 spleeter_out파일에 들어있습니다.")

            print("wav파일 변환작업을 시작합니다.")
            print("변환작업에서는 wav파일의 channels와 sampling rate를 변환합니다.")
            rate = input("원하는 sampling rate를 입력하세요. 엔터를 누르시면 default값인 22050으로 변환합니다.")
            sec = trans.transform()
            sec.trans() if rate is '' else sec.trans(rate)
            print("변환이 완료되었습니다.")

            print("STT작업을 시작합니다.")
            print("STT작업에서는 wav파일들의 음성을 text로 변환하여 json파일에 저장합니다.")
            print("사용할 api를 선택하세요. 1번은 별도의 key가 필요없습니다.")
            print("1. google web speech")
            print("2. google cloud speech")
            print("3. azure stt")
            api = input("==>")
            thr = stt.wav_to_text(choose_api = int(api))
            print("stt작업이 완료되었습니다.")
            print("json파일을 확인해주세요.")




        elif task ==2:
            pass
        elif task ==3:
            pass
        elif task ==4:
            pass
        elif task ==5:
            pass
        elif task ==0:
            print("이용해주셔서 감사합니다. ㅂㅂ")
            exit()
        elif task == -1:
            print("숫자를 입력해주세요")
        else:
            prnit("0 ~ 5 중에서 하나 선택해주세요")





