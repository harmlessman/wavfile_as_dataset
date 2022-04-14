
import os



path = ''

# code가 0이면 x_xxx.wav 형식으로 wav파일이름을 지어야 한다.
# code가 1이면 상관없음
code =1


class initial():
    def __init__(self):
        self.code = code
        if code==0:
            self.path = path
            self.spl_path = path + "\\spleeter_out\\"
            self.filelist = [wav for wav in os.listdir(path) if wav.endswith(".wav")]
            self.filelist = sorted(self.filelist, key=lambda x: int(x.split('_')[0]))
            self.filenum = len(self.filelist)
            self.partnum = list(set(int(i.split('_')[0]) for i in self.filelist))
            self.partnum.sort()
            os.chdir(self.path)
            self.mono_path = self.path + "\\mono\\"
            self.spl_list = [wav for wav in os.listdir(self.spl_path) if wav.endswith(".wav")]
            self.spl_list = sorted(self.spl_list, key=lambda x: int(x.split('_')[0]))
            self.mono_list = [wav for wav in os.listdir(self.mono_path) if wav.endswith(".wav")]
            self.mono_list = sorted(self.mono_list, key=lambda x: int(x.split('_')[0]))
            print(self.filenum)
        elif code==1:
            self.path = path
            self.spl_path = path + "\\spleeter_out\\"
            self.filelist = [wav for wav in os.listdir(path) if wav.endswith(".wav")]
            self.filenum = len(self.filelist)
            self.partnum = None
            os.chdir(self.path)
            self.mono_path = self.path + "\\mono\\"
            self.spl_list = [wav for wav in os.listdir(self.spl_path) if wav.endswith(".wav")]
            self.mono_list = [wav for wav in os.listdir(self.mono_path) if wav.endswith(".wav")]
            print(self.filenum)


a = [i for i in os.listdir(os.getcwd()) if os.path.isdir(i)]
print(a)