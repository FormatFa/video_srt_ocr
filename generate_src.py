# 生成字幕文件
import srt
import os
import json
paths = ['/media/indigo6a/TOSHIBA EXT/迅雷下载/[§极度空间原创§][国产][神探狄仁杰]1,2,3部合集/神探狄仁杰第三部/crop','/media/indigo6a/TOSHIBA EXT/迅雷下载/[§极度空间原创§][国产][神探狄仁杰]1,2,3部合集/神探狄仁杰第二部/crop']
from datetime import timedelta
def parseJson(path):
    pass
    subtitles = []
    subtitles.append(
        srt.Subtitle(0,timedelta(seconds=10),timedelta(seconds=20),'本字幕由格格字幕组制作 2022-05-14 可能会有些错别字')
    )
    subtitles.append(
        srt.Subtitle(0,timedelta(seconds=25),timedelta(seconds=30),'欢迎访问 http://bbs.indigo6a.top 了解更多')
    )
    data = json.loads(open(path,'r',encoding='utf-8').read())
    for i in range(0,len(data)):
        item = data[i]
        
        if i<len(data)-1:
            end = timedelta(milliseconds=data[i+1]['time'])
        if len(item['ocr'])==0:
            continue
        line = item['ocr'][0]
        content = ''.join(line[0])
        start = timedelta(milliseconds=item['time'])
        print(start,end,content)
        subtitles.append(
            srt.Subtitle(i,start,end,content)
        )

    outfile = path.split(".")[0]+".srt"
    print(outfile)
    with open(outfile,'w',encoding='utf-8') as out:
        out.write(srt.compose(subtitles))

parseJson('/media/indigo6a/TOSHIBA EXT/迅雷下载/[§极度空间原创§][国产][神探狄仁杰]1,2,3部合集/神探狄仁杰第三部/crop/神探狄仁杰3-01.rmvb_crop.mp4.json')

for path in paths:
    for file in os.listdir(path):
        abspath = os.path.join(path,file)
        if abspath.endswith(".json"):
            parseJson(abspath)
            
