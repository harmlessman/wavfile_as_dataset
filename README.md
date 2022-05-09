# Wavefile_as_dataset
동영상에서 뽑아낸 음성데이터를 (음성, text)쌍으로 만들어주는 project입니다. 

## Based on
* https://github.com/deezer/spleeter


## This Project
* 동영상에서 뽑아낸 음성데이터를 사용하여 (음성, text)쌍으로 만드는 것이 목표입니다.
* 제작자는 음성합성에 필요한 데이터를 확보하기 위해 이 프로젝트를 시작하게 되었습니다. 
* 작업 순서는 배경음 제거, 음성파일 변형, STT(speech-to-text)순으로 진행합니다.
* 배경음 제거에서는 [spleeter](https://github.com/deezer/spleeter)라이브러리를 사용했습니다.
* 음성파일 변형에서는 wav파일의 channel과 sampling rate를 변형합니다.
* STT에서는 [google_web](https://wicg.github.io/speech-api/), [google_cloud_stt](https://cloud.google.com/speech-to-text), [azure_stt](https://azure.microsoft.com/services/cognitive-services/speech-to-text/#overview) 총 3개의 api 중 선택해서 사용하실 수 있습니다.
* 음차번역이 적용된 text를 원한다면 별도의 음차번역의 작업을 거쳐야 합니다.[별도 서술]()


## 실행 순서
### 데이터 준비
* 원하는 음성을 편집기를 이용하여 자르고 저장합니다. 편집기 선택은 자유지만 제작자는 [shotcut](https://shotcut.org/)을 이용했습니다. 음성을 자를 때, 앞 뒤 공백크기를 적어도 0.3초 정도는 남겨주시길 바랍니다.(공백이 너무 크면 음성합성에 안좋은 영향을 미치고, 너무 작으면 STT작업에서 앞 뒤 말을 잘 알아듣지 못하는 이슈가 있었습니다.)
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
* wav파일들과 text는 spleeter_out 폴더에 저장됩니다. text는 json파일입니다.("wav파일이름" : "text" 로 구성됩니다.)
* 배경음 제거, 음성파일 변형, STT(speech-to-text) 3가지 작업을 각각 따로하고 싶거나 세부적으로 컨트롤을 하고싶으시다면 2번, 3번, 4번을 선택하시면 됩니다. 자세한 내용은 main파일을 실행해주시면 알 수 있습니다.

### 결과
* 배경음악을 지우는데 사용한 라이브러리인 spleeter는 배경음악에 가사가 없다는 전제 하에, 탁월한 성능을 보여주었습니다. 다만, 시간이 조금 오래 걸린다는 단점이 있었습니다. 제 노트북 기준 wav파일(약 3~4초) 1개당 15~20초 정도 소요되었습니다.
* 앞에서는 사용가능한 STT api로 google web, google cloud stt, azure stt 총 3가지를 제시했습니다. 하지만 google web은 정확도가 많이 떨어졌고, google cloud stt는 정확도는 높았지만 문장 사이에 공백이 약간이라도 길면 뒤의 문장을 text로 변환하지 않는 이슈가 있었습니다. azure stt는 높은 정확도를 보여주었으며, wav파일의 공백에 대한 이슈도 거의 없었습니다. 사용 할 api로는 azure stt를 추천드립니다. (한 달에 5시간 무료인 점도 장점) 













