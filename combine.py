# 노트북 박살로 깃허브에서 코드 짜는중
# 대충 구도만 잡고 집에서 마저 만들어야 할 듯

import json
import os
import set


def combinejson():
  spl_path = set.path + "\\spleeter_out"
  os.chdir(spl_path)

  dic = {}
  jlist = [j for j in os.listdir(spl_path) if j.endswith(".json")]

  if set.textsetname not in jlist:
    print("STT작업을 먼저 시행하신 후 combine을 해주십시오.")

  jlist.remove(set.textsetname)
  if len(jlist) == 0:
    print("combine 작업을 진행 할 json파일이 없습니다.")

  with open(set.textsetname, 'r', encoding='UTF8') as f:
    dic = json.load(f)

  for i in jlist:
    with open(i, 'r', encoding='UTF8') as f:
      dic.update(json.load(f))

  print(dic)
  with open(set.textsetname, 'w', encoding='UTF8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=2)

  for i in jlist:
    os.remove(i)
