import os
from set import initial
from pydub import AudioSegment

'''
    speech to text(stt) 작업 전 전처리과정
    만약 wav파일이 스테레오라면 모노로 바꿔주는 편이 stt에 유리하다.
    wav_to_text클래스의 google_cloud_speech에서 사용할 api도 모노를 지원하니 모노로 바꿔주자.
'''
def wavlist(p):
    return sorted([wav for wav in os.listdir(p) if wav.endswith(".wav")], key=lambda x: int(x.split('_')[0]))

class transform(initial):
    def __init__(self):
        super().__init__()

    def trans(self):
        try:
            os.mkdir(self.path+'\\trans')
        except FileExistsError:
            print("")
        for i in self.spl_list:
            sound = AudioSegment.from_wav(self.spl_path+i)
            sound = sound.set_channels(1)
            sound = sound.set_frame_rate(22050)
            sound.export(self.trans_path+i, format="wav")


if __name__ == '__main__':
    a = transform()
    a.trans()