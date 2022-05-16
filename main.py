

'''
    1. wav_spleeter에서 spleeter수행
    2. wav_transform에서 wav파일 변형
    3. speech에 대한 text 구하기
    끝

'''


import set
import json
import os
import datetime
import time
import aftermath
import wav_spleeter as spl
import wav_to_text as stt
import wav_transform as trans


spl_time = 20


def readkey():
    with open('key.json', 'r', encoding="utf-8") as f:
        key = json.load(f)
        set.path=key['path']
        if key['path']=="":
            set.path = '.\\'
        set.azure_key = key['azure_key']

def intro():
    pass


if __name__=='__main__':
    print("안녕하세요. wavfile을 tts용 데이터 셋 으로 만들어 드리는 프로그램입니다.")
    readkey()
    while(True):
        print("\n\n원하시는 작업을 선택 하십시오.")
        print("1. 빠른 시작")
        print("2. 배경음악 제거")
        print("3. 파일 변형")
        print("4. STT작업")
        print("5. 후처리 작업")
        print("6. japanese to korean(예정)")
        print("0. 나가기")
        menu = input("작업을 선택하세요 ==> ")
        task = int(menu) if menu.isdigit() else -1

        if task in [1,2,3,4,5]:
            print("dataset이 들어있는 디렉토리의 경로를 입력해주세요.")
            print("enter를 누르면 key.json에 있는 경로에서 작업이 진행됩니다.")
            p = input("path : ")
            if p != '':
                set.path = p

            print(f'path : {set.path}')

            print("\nSTT작업에서 사용할 api의 key가 있다면 key를 입력해주세요")
            print("enter를 누르면 key.json에 있는 key값을 가져옵니다.")
            k = input("api_key : ")
            if k != '':
                set.azure_key = k
            print(f'api_key : {set.azure_key}')

        if task ==1:
            print("빠른시작을 실시합니다.")

            fir = spl.wav_spleeter()
            if fir.filenum == 0:
                print("wav파일이 존재하지 않습니다!")
                print("path가 맞는지 확인하거나 path에 wav파일이 있는지 확인해주세요")
                continue
            print(f'작업해야 할 파일의 수는 {fir.filenum}개 입니다.')
            print(f'배경음악 제거작업(spleeter)에는 시간이 다소 소요됩니다. ')
            print(f'예상 소요시간은 약 {datetime.timedelta(seconds=fir.filenum*spl_time)}입니다.')
            input("인지하셨으면 엔터를 눌러주세요")
            fir.folderinfo()
            fir.spleeter(0)
            fir.spldata_to_path()
            print("\n배경음악 제거 작업이 완료되었습니다.")
            print("배경음악이 제거된 wav파일은 spleeter_out파일에 들어있습니다.")

            print("\nwav파일 변환작업을 시작합니다.")
            print("변환작업에서는 wav파일의 channels와 sampling rate를 변환합니다.")
            rate = input("원하는 sampling rate를 입력하세요. 엔터를 누르시면 default값인 22050으로 변환합니다.")
            sec = trans.transform()
            sec.trans() if rate is '' else sec.trans(rate)

            print("\n변환이 완료되었습니다.")

            print("\nSTT작업을 시작합니다.")
            print("STT작업에서는 wav파일들의 음성을 text로 변환하여 json파일에 저장합니다.")
            print("사용할 api를 선택하세요. 1번은 별도의 key가 필요없습니다.")
            print("1. google web speech")
            print("2. google cloud speech")
            print("3. azure stt")
            api = input("==>")
            if int(api) not in [1,2,3]:
                print("올바른 숫자를 입력해주세요.")
                continue

            print(f'\n언어를 선택해주세요.')
            print(f'https://docs.microsoft.com/ko-kr/azure/cognitive-services/speech-service/language-support?tabs=speechtotext 링크에서 참고하시면 됩니다.')
            print(f'한국어 : ko-KR, 영어 : en-US, 일본어 : ja-JP......')
            lang = input("==>")
            thr = stt.wav_to_text(choose_api = int(api), lang = lang)
            print("\nstt작업이 완료되었습니다.")

            print("\njson파일을 확인해주세요.")

            print("\ncombine작업을 실시합니다.")
            print(f'{set.path}에 존재하는 모든 json파일들을 {set.textsetname}에 update합니다.')
            aftermath.combine()
            print("완료되었습니다.")

            print("\ndelete작업을 실시합니다.")
            print("delete작업에서는 사용자가 적합하지 않은 wav파일을 삭제하면, 그에 맞게 json파일을 수정하는 일을 합니다.")
            print()
            print("우선 path의 trans dir에서 필요없는 wav파일을 삭제한 후 아무 키나 눌러주세요. 삭제 할 파일이 없으면 바로 아무 키나 눌러주세요.")
            input()
            aftermath.delete()
            print("완료되었습니다.")

            print("\ntarget작업을 실시합니다.")
            aftermath.target()

            print("모든 작업이 완료되었습니다.")
            print("추가 작업을 원하시면 2,3,4,5를 선택하여 작업을 수행해주십시오.")
            print("감사합니다.")

        elif task ==2:
            print("배경음악 제거기능을 선택하셨습니다.")
            fir = spl.wav_spleeter()
            print("범위를 선택하세요")
            print("0 -> wav파일 전체\nnum1 -> num1회차만\nnum1 num2 -> num1~num2회차까지 ")
            num = input("범위를 입력하시오.").split()
            if len(num)==1:
                print(f'작업해야 할 파일의 수는 {len([i for i in fir.filelist if int(i.split("_")[0])==int(num[0])])}개 입니다.')
                print(f'배경음악 제거작업(spleeter)에는 시간이 다소 소요됩니다. ')
                print(f'예상 소요시간은 약 {datetime.timedelta(seconds=len([i for i in fir.filelist if int(i.split("_")[0])==int(num[0])]) * spl_time)}입니다.')
                input("인지하셨으면 엔터를 눌러주세요")
                fir.folderinfo()
                fir.spleeter(int(num[0]))
                fir.spldata_to_path()
                print("\n배경음악 제거 작업이 완료되었습니다.")
                print("배경음악이 제거된 wav파일은 spleeter_out파일에 들어있습니다.")
            elif len(num)==2:
                print(f'작업해야 할 파일의 수는 {len([i for i in fir.filelist if int(num[0])<=int(i.split("_")[0])<=int(num[1])])}개 입니다.')
                print(f'배경음악 제거작업(spleeter)에는 시간이 다소 소요됩니다. ')
                print(f'예상 소요시간은 약 {datetime.timedelta(seconds=len([i for i in fir.filelist if int(num[0])<=int(i.split("_")[0])<=int(num[1])]) * spl_time)}입니다.')
                input("인지하셨으면 엔터를 눌러주세요")
                fir.folderinfo()
                fir.spleeter(int(num[0]), int(num[1]))
                fir.spldata_to_path()
                print("\n배경음악 제거 작업이 완료되었습니다.")
                print("배경음악이 제거된 wav파일은 spleeter_out파일에 들어있습니다.")
            else:
                print("범위에 맞게 입력해주세요.")

        elif task ==3:
            print("wav파일 변환 작업을 선택하셨습니다.")
            print("\nwav파일 변환작업을 시작합니다.")
            print("변환작업에서는 wav파일의 channels와 sampling rate를 변환합니다.")
            rate = input("원하는 sampling rate를 입력하세요. 엔터를 누르시면 default값인 22050으로 변환합니다.")
            sec = trans.transform()
            sec.trans() if rate is '' else sec.trans(rate)
            print("\n변환이 완료되었습니다.")

        elif task ==4:
            print("\nSTT작업을 시작합니다.")
            print("STT작업에서는 wav파일들의 음성을 text로 변환하여 json파일에 저장합니다.")

            print("사용할 api를 선택하세요. 1번은 별도의 key가 필요없습니다.")
            print("1. google web speech")
            print("2. google cloud speech")
            print("3. azure stt")
            api = input("==>")
            if int(api) not in [1,2,3]:
                print("올바른 숫자를 입력해주세요.")
                continue
            print(f'\n언어를 선택해주세요.')
            print(f'https://docs.microsoft.com/ko-kr/azure/cognitive-services/speech-service/language-support?tabs=speechtotext 링크에서 참고하시면 됩니다.')
            print(f'한국어 : ko-KR, 영어 : en-US, 일본어 : ja-JP......')
            lang = input("==>")

            print("범위를 선택하세요")
            print("0 -> wav파일 전체\nnum1 -> num1회차만\nnum1 num2 -> num1~num2회차까지 ")
            num = input("범위를 입력하시오.").split()

            if len(num)==1:
                thr = stt.wav_to_text(choose_api=int(api), lang=lang, start=int(num[0]))
                print("\nstt작업이 완료되었습니다.")

                print("\njson파일을 확인해주세요.")
            elif len(num)==2:
                thr = stt.wav_to_text(choose_api=int(api), lang=lang, start=int(num[0]), end=int(num[1]))
                print("\nstt작업이 완료되었습니다.")

                print("\njson파일을 확인해주세요.")
            else:
                print("범위에 맞게 입력해주세요.")

        elif task == 5:
            while(True):
                print("\n\n후처리 작업을 실시합니다.")
                print("후처리 작업은 combine, delete, target작업으로 이루어져 있습니다.")
                print("1. combine작업은 stt작업의 결과물인 json파일들을 하나로 합치는 작업입니다.")
                print("2. delete작업은 데이터로 사용하기 적합하지 않은 데이터를 삭제할 때 사용됩니다.")
                print("이때 적합하지 않은 데이터인지는 본인이 판단해야 합니다.")
                print("3. target작업은 dataset이 위치해야 하는 위치로 이동합니다. json파일에도 반영됩니다.")
                print("0. 후처리 작업을 종료합니다.")
                menu2 = input("작업을 선택하세요 ==> ")
                task2 = int(menu2) if menu2.isdigit() else -1
                if task2 == 1:
                    print("combine작업을 실시합니다.")
                    print(f'{set.path}에 존재하는 모든 json파일들을 {set.textsetname}에 update합니다.')
                    aftermath.combine()
                    print("완료되었습니다.")
                elif task2 == 2:
                    print("delete작업을 실시합니다.")
                    print("delete작업에서는 사용자가 적합하지 않은 wav파일을 삭제하면, 그에 맞게 json파일을 수정하는 일을 합니다.")
                    print()
                    print("우선 path의 trans dir에서 필요없는 wav파일을 삭제한 후 아무 키나 눌러주세요.")
                    input()
                    aftermath.delete()
                    print("완료되었습니다.")
                elif task2 == 3:
                    print("target작업을 실시합니다.")
                    aftermath.target()
                elif task2 == 0:
                    break
                elif task2 == -1:
                    print("숫자를 입력해주세요.")
                else:
                    print("1, 2, 3 중 하나를 선택해주세요.")

        elif task ==6:
            print("문서 참조 부탁드립니다.")

        elif task ==0:
            print("이용해주셔서 감사합니다. ㅂㅂ")
            exit()

        elif task == -1:
            print("숫자를 입력해주세요")

        else:
            print("0 ~ 5 중에서 하나 선택해주세요")





