import os
from set import initial
from pydub import AudioSegment

# 만약 wav파일이 스테레오라면 모노로 바꿔주는 편이 stt에 유리하다.
# wav_to_text클래스의 google_cloud_speech에서 사용할 api도 모노를 지원하니
# 모노로 바꿔주자.
class mono_trans(initial):
    def __init__(self):
        super().__init__()

    def mono(self):
        monolist =  [wav for wav in os.listdir(self.spl_path) if wav.endswith(".wav")]
        monolist = sorted(monolist, key=lambda x: int(x.split('_')[0]))
        os.mkdir(self.path+'\\mono')
        print(monolist)
        for i in monolist:
            sound = AudioSegment.from_wav(self.spl_path+i)
            sound = sound.set_channels(1)
            sound.export(self.path+'\\mono\\'+i, format="wav")


if __name__ == '__main__':
    a = mono_trans()
    a.mono()