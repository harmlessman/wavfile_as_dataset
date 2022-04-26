
import speech_recognition as sr
import os
from google.cloud import speech_v1
import io
import azure.cognitiveservices.speech as speechsdk
import json
from set import initial
import sys
from set import azure_key
import datetime

'''
    wavfile 각각의 text를 추출하는 class.
    저장 형식은 json
    사용 가능한 api는 3개로 하고 싶은거 마음대로
    1. google web speech (공짜, 품질 제일 낮음)
    2. google cloud speech (유료, google cloud speech에 직접 들어가서 로그인 후 api 공개 키를 받아야함, 파일 양 끝부분을 잘 못알아먹고 일본어 잘 못함)
    3. azure stt (유료, azure 계정생성 후 '리소스 만들기' 후 키를 받아야함, 제일 성능좋음)
    
'''
class wav_to_text(initial):
    def __init__(self, choose_api, start, end=0):
        super().__init__()
        self.output = {}
        self.mode=''
        self.trans_list = [wav for wav in os.listdir(self.trans_path) if wav.endswith(".wav")]
        self.trans_list = sorted(self.trans_list, key=lambda x: int(x.split('_')[0]))
        print(self.spl_list)

        if choose_api==1:
            self.googleweb()
            self.write_json(1)
        elif choose_api==2:
            self.google_cloud_stt()
            self.write_json(2)
        elif choose_api==3:
            self.azure_stt(start, end)
            self.write_json(3)
        else:
            print("plz choose api -> 1 or 2 or 3")

    # 1. 공짜
    def googleweb(self):
        r = sr.Recognizer()
        print(self.trans_list)
        #self.trans_list = ["9_022_spl.wav"]
        for i in self.trans_list:
            korean_audio = sr.AudioFile(self.trans_path + i)
            with korean_audio as source:
                audio = r.record(source)

            try:
                text = r.recognize_google(audio_data=audio, language='ja-JP')
            except sr.UnknownValueError:
                text = 'this file is too short'
            self.output[i]=text
            print(f'googleweb : {i} = {text}')


    # 2.
    def google_cloud_stt(self, start, end=0):
        """Transcribe the given audio file."""

        if start == 0:
            list = self.trans_list
        elif end==0 and (start in self.partnum):
            list = [wav for wav in self.trans_list if start==int(wav.split('_')[0])]
        elif start!=0 and end!=0:
            list = [wav for wav in self.trans_list if start <= int(wav.split('_')[0]) <= end]

        for i in list:
            text = ""
            client = speech_v1.SpeechClient()
            with io.open(self.trans_path+i, "rb") as audio_file:
                content = audio_file.read()

            audio = speech_v1.RecognitionAudio(content=content)

            config = speech_v1.RecognitionConfig(
                encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=22050,
                language_code="ja-JP",
                audio_channel_count=1,
            )

            response = client.recognize(config=config, audio=audio)
            print(response.results)
            if response.results == []:
                text = "None"
                self.output[i] = text
            # Each result is for a consecutive portion of the audio. Iterate through
            # them to get the transcripts for the entire audio file.
            for result in response.results:
                # The first alternative is the most likely one for this portion.
                text = format(result.alternatives[0].transcript)
                print(f'google_cloud_speech: {i} = {text}')
                self.output[i] = text




    # 3.
    def azure_stt(self, start=0, end=0):
        if start == 0:
            list = self.trans_list
        elif end==0 and (start in self.partnum):
            list = [wav for wav in self.trans_list if start==int(wav.split('_')[0])]
        elif start!=0 and end!=0:
            list = [wav for wav in self.trans_list if start <= int(wav.split('_')[0]) <= end]
        speech_config = speechsdk.SpeechConfig(subscription=azure_key, region="koreacentral")
        speech_config.speech_recognition_language = "ja-JP"

        for i in list:
            # To recognize speech from an audio file, use `filename` instead of `use_default_microphone`:
            text=""
            audio_config = speechsdk.audio.AudioConfig(
                filename=self.trans_path+i)
            # audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
            speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

            speech_recognition_result = speech_recognizer.recognize_once_async().get()
            text = speech_recognition_result.text
            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("Azure: {} = {}".format(i,text))
                self.output[i] = text
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
                self.output[i] = 'nomatch error'
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                self.output[i] = 'cancellation error'
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
                    self.output[i] = 'cancellation error2'


    def write_json(self, mode):
        dtime = datetime.datetime.now()
        dformat = "%Y-%m-%d_%H-%M-%S"
        modic = {
            1 : "google_web",
            2 : "google_cloud_stt",
            3 : "azure_stt"
        }
        with open(f'{modic[mode]}_{dtime.strftime(dformat)}.json', 'w+', encoding="utf-8") as f:
            json.dump(self.output, f, ensure_ascii=False, indent='\t')


if __name__=='__main__':
    wav_to_text(3, 14, 38)
