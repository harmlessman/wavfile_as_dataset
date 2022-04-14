import speech_recognition
import speech_recognition as sr
import librosa
import os
from google.cloud import speech_v1p1beta1
from google.cloud import speech_v1
from google.cloud import speech
import io

import json
from set import initial
class wav_to_text(initial):
    def __init__(self):
        super().__init__()
        self.speechtext = {}
        self.monotext = {}
        print(self.spl_list)


    def googleweb(self):
        r = sr.Recognizer()
        print(self.spl_list)
        for l in self.spl_list:
            sample_wav, rate = librosa.core.load(self.spl_path + l)
            korean_audio = sr.AudioFile(self.spl_path + l)
            with korean_audio as source:
                audio = r.record(source)

            try:
                text = r.recognize_google(audio_data=audio, language='ja-JP')
            except sr.UnknownValueError:
                text = 'this file is too short'
            self.speechtext[l]=text
            print(text)


    def write_json(self):
        with open('spl_googleweb.json', 'w+', encoding="utf-8") as f:
            json.dump(self.speechtext, f, ensure_ascii=False, indent='\t')

    def google_cloud_speech(self):
        """Transcribe the given audio file."""
        self.mono_list = ["9_016_spl.wav"]
        for i in self.mono_list:
            text = ""
            client = speech_v1.SpeechClient()
            with io.open(self.mono_path+i, "rb") as audio_file:
                content = audio_file.read()

            audio = speech_v1.RecognitionAudio(content=content)

            config = speech_v1.RecognitionConfig(
                encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=22050,
                language_code="ja-JP",
                audio_channel_count=1,
            )

            response = client.recognize(config=config, audio=audio)
            # print(response.results)
            # Each result is for a consecutive portion of the audio. Iterate through
            # them to get the transcripts for the entire audio file.
            for result in response.results:
                # The first alternative is the most likely one for this portion.
                text = format(result.alternatives[0].transcript)
                print(f'{i} = {text}')
                self.monotext[i] = text

    def writemono_json(self):
        with open('spl_google_cloud.json', 'w+', encoding="utf-8") as f:
            json.dump(self.monotext, f, ensure_ascii=False, indent='\t')

if __name__=='__main__':
    a = wav_to_text()
    a.google_cloud_speech()
    #a.googleweb()
    #a.writemono_json()
    #a.speech_to_text()
    #a.write_json()
