import os



path = 'C:\\Users\\82109\\Desktop\\wavfile_as_dataest\\dataset_emilia'
azure_key = ''
# code가 0이면 x_xxx.wav 형식으로 wav파일이름을 지어야 한다.
# code가 1이면 상관없음
code =0

def wavlist(p):
    return sorted([wav for wav in os.listdir(p) if wav.endswith(".wav")], key=lambda x: int(x.split('_')[0]))

# filelist -> wav file list (str)
# filenum -> wav file count (int)
# partnum -> ani part num list (int)
# path -> dataset path (str)
# total_time -> wav file total time
class initial():
    def __init__(self):
        self.code = code
        if code==0:
            self.path = path
            self.spl_path = path + "\\spleeter_out\\"
            self.filelist = wavlist(self.path)
            self.filenum = len(self.filelist)
            self.partnum = list(set(int(i.split('_')[0]) for i in self.filelist))
            self.partnum.sort()
            self.trans_path = self.path + "\\trans\\"

        elif code==1:
            self.path = path
            self.spl_path = path + "\\spleeter_out\\"
            self.filelist = [wav for wav in os.listdir(path) if wav.endswith(".wav")]
            self.filenum = len(self.filelist)
            self.partnum = None
            os.chdir(self.path)
            self.trans_path = self.path + "\\trans\\"
            self.spl_list = [wav for wav in os.listdir(self.spl_path) if wav.endswith(".wav")]


initial()
