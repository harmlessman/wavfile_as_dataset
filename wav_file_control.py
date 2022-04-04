import os
import wave
import datetime


# filelist -> wav file list (str)
# filenum -> wav file count (int)
# partnum -> ani part num list (int)
# path -> dataset path (str)
# total_time -> wav file total time
class wav_file_control():
    def __init__(self, path):
        self.path = path
        self.spl_path = path+"\\spleeter_out\\"
        self.filelist = [wav for wav in os.listdir(path) if wav.endswith(".wav")]
        self.filenum = len(self.filelist)
        self.partnum = list(set(int(i[0]) for i in self.filelist))
        self.partnum.sort()
        self.total_time = 0

        print(self.partnum)
        os.chdir(self.path)
        print(self.filelist)
        print(f'파일이 {self.filenum}개 있습니다.')

        for i in self.filelist:
            a = wave.open(i, 'rb')
            self.total_time += a.getnframes() / a.getframerate()

        print(self.total_time)
        print(f'total time : {datetime.timedelta(seconds=self.total_time)}')



    """
    start = 0이면 path안의 모든 wav파일을 spleeter
    start = n이면 n으로 시작하는 wav파일을 spleeter
    start와 end값이 둘 다 입력되면 start~end까지의 wav파일을 spleeter
    """

    def spleeter(self, start, end=0):
        spl_command = 'spleeter separate -p spleeter:2stems -o spleeter_out '
        if start==0:
            for i in self.filelist:
                os.system(spl_command+i)
            print("Done")
        elif end==0 and (start in self.partnum):
            for i in self.filelist:
                if int(i[0])==start:
                    os.system(spl_command+i)
            print("Done")
        elif start!=0 and end!=0:
            if start not in self.partnum or end not in self.partnum:
                print("RangeError!1")
            if start>end:
                print("end must large then start!")
            for i in self.filelist:
                if i[0]>=start and i[0]<=end:
                    os.system(spl_command+i)
            print("Done")
        else:
            print("RangeError!2")


    """
    실행 하면 spleeter함수 실행 후 나온 파일들 중 vocal파일을 
    spleeter_out 디렉토리에 배치한다. 그 후 mr파일과 디렉토리는 삭제
    """

    def spldata_to_path(self):
        if not (os.path.exists(self.spl_path)):
            print("plz execute spleeter def!")
            return 0
        os.chdir(self.spl_path)
        spl_dir = [i for i in os.listdir(os.getcwd()) if os.path.isdir(i)]
        print(spl_dir)
        if len(spl_dir)==0:
            print("spleeter 먼저 실행해 주세요. ")
        for l in spl_dir:
            try:
                os.rename(self.spl_path + l + "\\vocals.wav", self.spl_path + l + "_spl.wav")
            except FileNotFoundError:
                print(l+"폴더에 vocals.wav 파일이 없습니다.")
            except FileExistsError:
                os.remove(self.spl_path + l + "_spl.wav")
                os.rename(self.spl_path + l + "\\vocals.wav", self.spl_path + l + "_spl.wav")

        for l in spl_dir:
            try:
                os.remove(self.spl_path + l + "\\accompaniment.wav")
                os.rmdir(self.spl_path + l)
            except FileNotFoundError:
                pass



    def folderinfo(self):
        info = os.popen('dir').read()
        f = open("info.txt", 'w')
        print(info)
        f.write(f'wav file total time : {datetime.timedelta(seconds=self.total_time)}\n\n')
        f.write(f'file_num = {self.filenum}\n\n')
        f.write(info)
        f.close()


if __name__ == '__main__':
    path = 'C:\\Users\\82109\\Desktop\\dataset_emilia'
    wavfile = wav_file_control(path)
    wavfile.folderinfo()
    wavfile.spleeter(0)
    #wavfile.spldata_to_path()

