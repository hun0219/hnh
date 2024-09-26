## 가장 높은 스코어를 가진 prediction을 찾는 함수
#def get_max_score(predictions):
#    highest = predictions[0]  # 첫 번째 예측을 기본으로 설정
#    for pred in predictions[1:]:  # 나머지 예측들과 비교
#        if pred['score'] > highest['score']:
#            highest = pred
#    return highest['label']

def get_max_score(p):
  max_score = 0
  max_label = ""
  for item in p:
      if item['score'] > max_score:
          max_score = item['score']
          max_label = item['label']
  return max_label


def get_score(item):
  return item['score']


def get_max_score2(p):
  max_p = max(p, key=get_score)
  return max_p['label']


def get_max_score3(p):
  max_p = max(p, key=lambda x: x['score'])
  return max_p['label']
