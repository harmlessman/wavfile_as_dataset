# Wavefile_as_dataset
동영상에서 뽑아낸 음성데이터를 (음성, text)쌍으로 만들어주는 project입니다. 

## Based on
* https://github.com/deezer/spleeter


## This Project
* 동영상에서 뽑아낸 음성데이터를 사용하여 (음성, text)쌍으로 만드는 것이 목표입니다.
* 제작자는 음성합성에 필요한 데이터를 확보하기 위해 이 프로젝트를 시작하게 되었습니다. 
* 작업 순서는 배경음 제거, 음성파일 변형, STT(speech-to-text)순으로 진행합니다.
* 배경음 제거에서는 [spleeter](https://github.com/deezer/spleeter)라이브러리를 사용했습니다.
* STT에서는 [google_web](https://wicg.github.io/speech-api/), [google_cloud_stt](https://cloud.google.com/speech-to-text), [azure_stt](https://azure.microsoft.com/services/cognitive-services/speech-to-text/#overview) 총 3개의 api 중 선택해서 사용하실 수 있습니다.
* 음차번역이 적용된 text를 원한다면 별도의 음차번역의 작업을 거쳐야 합니다.[별도 서술]()
* 










