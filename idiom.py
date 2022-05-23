import json
import os
import jieba
import srt
# 根据数据集，提取字幕里的成语
idioms = []
with open('idiom.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())
    for item in data:
        idioms.append(item['word'])
allIdiom = []        
for filepath,dirnames,filenames in os.walk('/home/indigo6a/Documents/projects/orc/srt'):
    for filename in filenames:
        abspath = os.path.join(filepath,filename)
        if not os.path.isfile(abspath):
            continue
        print(abspath,filename)
        print(abspath)
        with open(abspath,"r",encoding='utf-8') as f:
            subtitles = srt.parse(f.read())
            for subtitle in subtitles:
                words = jieba.cut(subtitle.content)
                # print(list(words))
                for word in words:
                    if word in idioms and len(word)==4:
                        has = False
                        for allIdiomItem in allIdiom:
                            if allIdiomItem['word']==word:
                                has=True
                                break
                        if has:
                            continue
                        print(word)
                        allIdiom.append({
                            'file':abspath,
                            'start':str(subtitle.start),
                            'word':word
                        })    


with open('duplicate_word.json','w',encoding='utf-8') as f:
    f.write(json.dumps(allIdiom,ensure_ascii=False))
        # words = jieba.cut(