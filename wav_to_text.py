import speech_recognition as sr
import librosa
import os
import json

class wav_to_text():
    def __init__(self, path):
        self.path = path
        self.spl_path = path+"\\spleeter_out\\"
        self.spl_list = [wav for wav in os.listdir(self.spl_path) if wav.endswith(".wav")]
        self.speechtext = {}
        print(self.spl_list)


    def speech_to_text(self):
        r = sr.Recognizer()
        self.spl_list = ['4_002_spl.wav']
        print(self.spl_list)
        for l in self.spl_list:
            sample_wav, rate = librosa.core.load(self.spl_path + l)
            korean_audio = sr.AudioFile(self.spl_path + l)
            with korean_audio as source:
                audio = r.record(source)
            text = r.recognize_google(audio_data=audio, language='ja-JP')
            self.speechtext[l]=text
            #r.recognize_google_cloud(audio_data=audio, language='ja-JP')

    def rite_json(self):
        with open('spl_text.json', 'w', encoding="utf-8") as f:
            json.dump(self.speechtext, f, ensure_ascii=False, indent='\t')




if __name__=='__main__':
    a = wav_to_text('C:\\Users\\82109\\Desktop\\dataset_emilia')

    a.speech_to_text()
    a.write_json()
