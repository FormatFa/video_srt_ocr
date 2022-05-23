# 通过拼音，成语接龙. 动态算法(?)
import json
from cv2 import add
from pypinyin import pinyin, lazy_pinyin, Style
import csv
#[{"file": "/home/indigo6a/Documents/projects/orc/srt/第二部/神探狄仁杰第二部26.srt", "start": "0:04:26.900000", "word": "内外夹攻"}, 

def get_candicate(alldata,currentdata):
    added = list(map(lambda i:i['word'],currentdata))
    result = [] 
    for item in alldata:
        if item['word'] not in added and item['pinyin'][0]==currentdata[-1]['pinyin'][-1]:
            result.append(item)
            added.append(item['word'])
    return result
def get(alldata,nowdata):
    candicate = get_candicate(alldata,nowdata)
    if len(candicate)==0:
        return 0
    if nowdata[-1]['word'] in memory.keys():
        return memory[nowdata[-1]['word']]
    maxcandicate = -1
    maxitem=None
    for item in candicate:
            
        nowdata.append(item)
        size = get(alldata,nowdata)
        nowdata.pop()
        if size>maxcandicate:
            maxcandicate=size
            maxitem=item

    memory[maxitem['word']]=maxcandicate

    return maxcandicate+1

memory={

}
with open('idiom.json','r',encoding='utf-8') as f:
    idioms = json.loads(f.read())

# def get
with open('duplicate_word.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())
    print(len(data))
    for item in data:

        item['pinyin'] = lazy_pinyin(item['word'])

    print(get_candicate(data,[data[2]]))
    result = get(data,[data[0]])
    print(result)
    dic2=dict(sorted(memory.items(),key= lambda x:x[1],reverse=True))
    result = []
    last=None
    for i in dic2:
       print(i,dic2[i]) 
       pin = lazy_pinyin(i)
       if last==None or  lazy_pinyin(last)[-1]==pin[0]:
           result.append(i)
           last=i
    print(result)           
    # 保存结果

    with open("result/同音接龙.csv","w",encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=['word','pinyin','start','file'])
        writer.writeheader()
        for word in result:
            item = list(filter(lambda x:x['word']==word,data))[0]
            writer.writerow({
                'word':item['word'],
                'start':item['start'],
                'file':item['file'],
                'pinyin':item['pinyin']
            })
            
