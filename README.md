# Wavefile_as_dataset
동영상에서 뽑아낸 음성데이터를 배경음악 제거, transform, STT과정을 통해 (음성, text)쌍으로 만들어주는 project입니다. 



## This Project
* 동영상에서 뽑아낸 음성데이터를 사용하여 (음성, text)쌍으로 만드는 것이 목표입니다.
* 제작자는 음성합성에 필요한 데이터를 확보하기 위해 이 프로젝트를 시작하게 되었습니다. 
* 작업 순서는 배경음 제거, 음성파일 변형, STT(speech-to-text), 후처리 작업 순으로 진행합니다.
* 배경음 제거에서는 [spleeter](https://github.com/deezer/spleeter)라이브러리를 사용했습니다.
* 음성파일 변형에서는 wav파일의 channel과 sampling rate를 변형합니다.
* STT에서는 [google_web](https://wicg.github.io/speech-api/), [google_cloud_stt](https://cloud.google.com/speech-to-text), [azure_stt](https://azure.microsoft.com/services/cognitive-services/speech-to-text/#overview) 총 3개의 api 중 선택해서 사용하실 수 있습니다.
* 음차번역이 적용된 text를 원한다면 별도의 음차번역의 작업을 거쳐야 합니다.[별도 서술]()


## 실행 순서
### Prerequisites
* python==3.7
* spleeter
* pydub
* SpeechRecognition
* azure-cognitiveservices-speech
* google-cloud-speech

```
pip install -r requirements.txt
```

### api key
여기서는 azure stt의 api key를 얻는 법에 대해서 설명합니다.




### 데이터 준비
* 원하는 음성을 편집기를 이용하여 자르고 저장합니다. 제작자는 [shotcut](https://shotcut.org/)을 이용했습니다. 음성을 자를 때, 앞 뒤 공백크기를 적어도 0.3초 정도는 남겨주시길 바랍니다.(공백이 너무 크면 음성합성에 안좋은 영향을 미치고, 너무 작으면 STT작업에서 앞 뒤 말을 잘 알아듣지 못하는 이슈가 있었습니다.)
* 음성의 확장자는 wav입니다.
* 음성 파일의 이름은 (회차) _ (1부터 차례대로 +1).wav 로 통일합니다. 예를들어 3화에 63번째 음성이면 '3_063.wav'
* (회차_1부터 차례대로 +1) 규칙을 지킬 필요는 없지만 숫자_숫자.wav 형식의 이름짓기는 코드 실행에 꼭 필요합니다. 앞의 숫자에 따라 크게 묶어서 데이터를 다룹니다.
* 만약 위의 형식대로 파일이름을 지을 수 없으시다면 set의 code값을 1로 바꿔주시길 바랍니다. 이렇게 하면 정상 이용이 가능하지만 빠른시작(1) 외의 다른 기능은 사용하실 수 없습니다.
* 데이터들은 하나의 dir에 저장해주십시오.
* 배경음악이 말소리가 들어간 음악이라면 그 데이터는 피해주시길 바랍니다. 배경음악을 잘 제거하지 못합니다.


### 실행
* key.json 파일에 wav파일들이 들어있는 경로(path)와 api_key를 입력합니다. 툴을 실행할 때 입력하는 것도 가능합니다.
* main.py실행 후, 툴에서 설명하는 대로 따라가시면 됩니다.
* 빠른 시작(1번)을 선택하시면 한번에 path의 모든 wav파일들을 dataset으로 만듭니다.
* wav파일들은 trans폴더, text는 path에 저장됩니다. text는 json파일입니다.("wav파일이름" : "text" 로 구성됩니다.)
* 배경음 제거, 음성파일 변형, STT(speech-to-text) 3가지 작업을 각각 따로하고 싶거나 세부적으로 컨트롤을 하고싶으시다면 2번, 3번, 4번을 선택하시면 됩니다. 자세한 내용은 main파일을 실행해주시면 알 수 있습니다.


### 후처리 작업
* 위의 작업을 끝냈다면 trans폴더에 wav파일, path에 json파일들이 존재 할 것입니다.
* 후처리 작업은 크게 combine, delete, target작업으로 구성됩니다.
* combine작업은 stt작업으로 생긴 json파일들을 한 json파일로 합쳐서 저장하는 작업입니다.
* delete작업은 사용자가 적합하지 않은 wav파일을 삭제하면, 그에 맞게 json파일을 수정하는 작업입니다.
* target작업은 trans폴더의 wav파일들과 path의 json파일(text.json)을 위치해야 하는 위치로 이동시킵니다. json파일의 key값을 이동 위치를 반영해서 수정합니다.


## Dataset Structure
dataset은 ('음성','text')구조이다.
'음성'은 wav파일들이고, 'text'는 각 음성의 절대경로 : 음성의 text값 이다. 'text'는 json파일이다.
```
ex) '음성'
1_001_spl.wav
1_002_spl.wav
1_003_spl.wav
    .
    .
    .
13_091_spl.wav


ex) 'text'
text.json
"D:\\Users\\Desktop\\voicesynthesispath\\1_001_spl.wav" : "나는 밥을 먹는다",
"D:\\Users\\Desktop\\voicesynthesispath\\1_002_spl.wav" : "걷는 중이다",
"D:\\Users\\Desktop\\voicesynthesispath\\1_003_spl.wav" : "만화보고 있다",
                                 .
                                 .
                                 .
"D:\\Users\\Desktop\\voicesynthesispath\\13_091_spl.wav" : "끝이다아아"
```






## Code Structure
```
# 대략적인 구조를 설명하기 위한 Code Structure


Example

# 초기 구조
# path에 wav파일들만 넣어두면 됩니다.
Path
╠═ 1_001.wav
╠═ 1_002.wav
╚═ ...  


    .
    .
    .

# spleeter, trans, STT작업을 모두 거친 후의 구조
# 직접 폴더를 만들거나 json파일을 생성할 필요x 자동으로 생성됩니다.
Path
 ║
 ╠═ pretrained_models                   <- spleeter사용을 위한 model, spleeter작업 시 자동으로 설치됨
 ╠═ spleeter_out                        <- spleeter작업의 결과물을 저장하는 폴더
 ║    ├── 1_001_spl.wav
 ║    ├── 1_002_spl.wav
 ║    └── ...
 ╠═ trans                               <- trans작업의 결과물을 저장하는 폴더. dataset의 음성
 ║    ├── 1_001_spl.wav
 ║    ├── 1_002_spl.wav
 ║    └── ...
 ╠═ text.json                           <- stt의 결과물을 json파일 형태로 저장. 처음 stt작업시 또는 json파일이 하나도 없을 때 생성.       
 ║                                         dataset을 만들 때 이 json파일을 기준으로 제작. dataset의 text
 ║ 
 ╠═ google_web_2022-04-20_16-55-47.json <- stt작업의 결과물들은 "api이름+시간"을 이름으로 하는 json파일로 저장  
 ╠═ azure_stt_2022-04-21_18-21-20.json
 ╠═ ...
 ╠═ 1_001.wav                           <- wav파일들
 ╠═ 1_002.wav
 ╠═ ...                   
 ╚═ info.txt                            <- spleeter작업 후 wav파일들의 대략적인 정보를 저장(총 길이, 용량 등)



```

```
#후처리 작업 중 target작업에서 targetpath와 dirname을 입력하면 그에 따라 dataset을 위치시키고 디렉토리 이름을 정함
targetpath
     ╚═══ dirname
             ├── audio
             │   ├── 1_001_spl.wav
             │   ├── 1_002_spl.wav
             │   └── ...
             │
             └── text.json
             
```


### Result
* 배경음악을 지우는데 사용한 라이브러리인 spleeter는 배경음악에 가사가 없다는 전제 하에, 탁월한 성능을 보여주었습니다. 다만, 시간이 조금 오래 걸린다는 단점이 있었습니다. 제 노트북 기준 wav파일(약 3초) 1개당 20초 정도 소요되었습니다.
* 앞에서는 사용가능한 STT api로 google web, google cloud stt, azure stt 총 3가지를 제시했습니다. 하지만 google web은 정확도가 많이 떨어졌고, google cloud stt는 정확도는 높았지만 문장 사이에 공백이 약간이라도 길면 뒤의 문장을 text로 변환하지 않는 이슈가 있었습니다. azure stt는 높은 정확도를 보여주었으며, wav파일의 공백에 대한 이슈도 거의 없었습니다. 사용 할 api로는 azure stt를 추천드립니다. (한 달에 5시간 무료인 점도 장점) 


~~### 추가예정 (soon)~~
~~* 음차번역기능 추가 예정(microsoft사의 transliteration api를 사용 할 예정)~~



###수정예정
코드를 조금 다듬은 다음, 라이브러리로 배포 할 예정.











