# 简单接龙
import json
from cv2 import add
from pypinyin import pinyin, lazy_pinyin, Style
#[{"file": "/home/indigo6a/Documents/projects/orc/srt/第二部/神探狄仁杰第二部26.srt", "start": "0:04:26.900000", "word": "内外夹攻"}, 
def get(alldata,now):
    result = []
    result.append(now)
    added = set()
    last = now
    while True:
        has=False
        for item in alldata:
            if item['word'] not in added and item['pinyin'][0]==last['pinyin'][-1]:
                result.append(item)
                added.add(item['word'])
                has=True
                last = item
        if has==False:
            break
    return result


# def get
with open('duplicate_word.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())
    print(len(data))
    for item in data:
        item['pinyin'] = lazy_pinyin(item['word'])
    all_result = []
    for item in data:
        result = get(data,item)
        all_result.append(result)
    all_result.sort(reverse=True, key=lambda i:len(i))
    print(len(all_result))
    for item in all_result[0]:
        print(item['word'],' ',item['start'],' ',item['file'].split("/")[-1])
    # for i in range(300):
    #     print(list(map(lambda x:x['word'],all_result[i])))
