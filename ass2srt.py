# 字幕转换
import os
import pysubs2
import srt
from datetime import timedelta
import re
def process(infile):
    
    subs = pysubs2.load(infile,encoding='utf-8')
    results = []
    i = 0
    for line in subs:
        print(line)
        print(line.start)
        content = re.sub("\{.*?\}","",line.text)
        print(srt.Subtitle(i,timedelta(milliseconds=line.start),timedelta(milliseconds=line.end),content))
        results.append(srt.Subtitle(i,timedelta(milliseconds=line.start),timedelta(milliseconds=line.end),content))
        i+=1
    with open(infile.replace('.ass','.srt'),'w',encoding='utf-8') as f:
        print(srt.compose(results))
        f.write(srt.compose(results))
# infile = 'srt/第一部/[神探狄仁杰1无台标版].Shen.Tan.Di.Ren.Jie.Complete.01.1080P.PPTV原画.x264.ass'
dir = "srt/第一部"
for file in os.listdir(dir):
    abspath = os.path.join(dir,file)
    if abspath.endswith(".ass"):
        process(abspath)