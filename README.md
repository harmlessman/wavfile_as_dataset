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
* 데이터들은 하나의 dir에 저장해주십시오.
* 배경음악이 말소리가 들어간 음악이라면 그 데이터는 피해주시길 바랍니다. 배경음악을 잘 제거하지 못합니다.
###












