# 通过文字，成语接龙
import json
from cv2 import add
import csv
from pypinyin import pinyin, lazy_pinyin, Style
#[{"file": "/home/indigo6a/Documents/projects/orc/srt/第二部/神探狄仁杰第二部26.srt", "start": "0:04:26.900000", "word": "内外夹攻"}, 

def get_candicate(alldata,currentdata):
    # print("get:",currentdata[-1])
    added = list(map(lambda i:i['word'],currentdata))
    # print(added)
    result = [] 
    for item in alldata:
        if  len(currentdata) ==0 or (item['word'] not in added and item['word'][0]==currentdata[-1]['word'][-1]):
            result.append(item)
            added.append(item['word'])
    return result
def get(alldata,nowdata):
    candicate = get_candicate(alldata,nowdata)
    if len(candicate)==0:
        return 0
    if  len(nowdata)!=0 and  nowdata[-1]['word'] in memory.keys():
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
    # print('put:',nowdata[-1]['word'],maxcandicate,len(memory.keys()))
    # print(sorted(memory))
       
    return maxcandicate+1

memory={

}

# def get
with open('duplicate_word.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())
    print(len(data))
    for item in data:
        item['pinyin'] = lazy_pinyin(item['word'])
    all_result = []
    maxresult=[]

    memory={}
    result = get(data,[])
    print(result)
    dic2=dict(sorted(memory.items(),key= lambda x:x[1],reverse=True))
    result = []
    last=None
    for i in dic2:
        pin = i
        if last==None or  last[-1]==pin[0]:
            result.append(i)
            last=i
    print(result)           
    with open("result/同字接龙.csv","w",encoding="utf-8") as f:
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
            