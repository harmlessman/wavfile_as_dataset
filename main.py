
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

def readkey():
    with open('.굚key.json', 'r', encoding="utf-8") as f:
        key = json.load(f)
        set.path=key[path]
        set.azure_key = key[azure_key]

def intro():
    pass


if __name__=='__main__':
    print("안녕하세요. wavfile을 tts용 데이터 셋 으로 만들어 드리는 프로그램입니다.")
    while(True):
        print("원하시는 작업을 선택 하십시오.")
        print("1. 빠른 시작")
        print("2. 배경음악 제거")
        print("3. 파일 변형")
        print("4. STT작업")
        print("5. japanese to korean(예정)")
        print("0. 나가기")
        menu = input("작업을 선택하세요 ==> ")




