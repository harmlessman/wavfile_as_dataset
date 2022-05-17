import os
from set import initial
from pydub import AudioSegment

'''
    speech to text(stt) 작업 전 전처리과정
    만약 wav파일이 스테레오라면 모노로 바꿔주는 편이 stt에 유리하다.
'''


class transform(initial):
    def __init__(self):
        super().__init__()
        if self.code==0:
            self.spl_list = set.wavlist(self.spl_path)
        elif self.code==1:
            self.spl_list = set.wavlistnon(self.spl_path)
    def trans(self,rate=22050):
        try:
            os.mkdir(self.path+'\\trans')
        except FileExistsError:
            pass
        for i in self.spl_list:
            sound = AudioSegment.from_wav(self.spl_path+i)
            sound = sound.set_channels(1)
            sound = sound.set_frame_rate(rate)
            sound.export(self.trans_path+i, format="wav")


if __name__ == '__main__':
    a = transform()
    a.trans()